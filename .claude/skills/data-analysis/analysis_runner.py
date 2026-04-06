#!/usr/bin/env python3
"""Bundle and verify reproducible data-analysis runs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import struct
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ARTIFACT_ROOT = Path("knowledge/data-analyses")
REPORT_FILENAME = "report.md"
CODE_FILENAME = "analysis.py"
CALC_LOG_FILENAME = "calc-log.jsonl"
MANIFEST_FILENAME = "manifest.yaml"
VERIFICATION_FILENAME = "verification.json"
CALC_REF_PATTERN = re.compile(r"\[calc:([A-Za-z0-9_.-]+)\]")


class RunnerError(RuntimeError):
    """Raised when the reproducibility bundle is invalid."""


@dataclass
class ComparisonResult:
    status: str
    mode: str
    details: dict[str, Any]


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def repo_root() -> Path:
    return Path.cwd()


def resolve_repo_path(path: str | Path) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return repo_root() / candidate


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def write_jsonl(path: Path, entries: list[dict[str, Any]]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        for entry in entries:
            handle.write(json.dumps(entry, sort_keys=True))
            handle.write("\n")


def write_yaml_subset(path: Path, payload: dict[str, Any]) -> None:
    ensure_parent(path)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_yaml_subset(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def copy_file(src: Path, dest: Path) -> None:
    if not src.exists():
        raise RunnerError(f"Missing artifact: {src}")
    ensure_parent(dest)
    shutil.copy2(src, dest)


def remove_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)


def sha256sum(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise RunnerError(f"Missing JSONL file: {path}")
    entries: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RunnerError(f"Invalid JSONL in {path}:{line_number}: {exc}") from exc
            if not isinstance(payload, dict):
                raise RunnerError(f"Expected JSON object in {path}:{line_number}")
            entries.append(payload)
    return entries


def calc_log_index(path: Path) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for entry in parse_jsonl(path):
        calc_id = entry.get("calc_id")
        if not calc_id or not isinstance(calc_id, str):
            raise RunnerError(f"Each calc-log row must include string calc_id: {path}")
        if calc_id in index:
            raise RunnerError(f"Duplicate calc_id '{calc_id}' in {path}")
        index[calc_id] = entry
    return index


def extract_calc_refs(report_text: str) -> list[str]:
    return sorted(set(CALC_REF_PATTERN.findall(report_text)))


def normalize_result(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise RunnerError(f"Expected PNG file: {path}")
    return struct.unpack(">II", header[16:24])


def compare_png(original: Path, replayed: Path) -> ComparisonResult:
    original_hash = sha256sum(original)
    replayed_hash = sha256sum(replayed)
    if original_hash == replayed_hash:
        return ComparisonResult(
            status="Passed",
            mode="sha256",
            details={"original_sha256": original_hash, "replayed_sha256": replayed_hash},
        )

    original_width, original_height = png_dimensions(original)
    replayed_width, replayed_height = png_dimensions(replayed)
    size_delta = abs(original.stat().st_size - replayed.stat().st_size)
    size_ratio = size_delta / max(original.stat().st_size, 1)

    if (original_width, original_height) == (replayed_width, replayed_height) and size_ratio <= 0.10:
        return ComparisonResult(
            status="Passed",
            mode="png-metadata",
            details={
                "original_sha256": original_hash,
                "replayed_sha256": replayed_hash,
                "dimensions": [original_width, original_height],
                "size_ratio_delta": round(size_ratio, 6),
            },
        )

    return ComparisonResult(
        status="Failed",
        mode="png-metadata",
        details={
            "original_sha256": original_hash,
            "replayed_sha256": replayed_hash,
            "original_dimensions": [original_width, original_height],
            "replayed_dimensions": [replayed_width, replayed_height],
            "size_ratio_delta": round(size_ratio, 6),
        },
    )


def materialize_text(
    *, inline_text: str | None, source_path: str | None, destination: Path, description: str
) -> None:
    if inline_text is not None and source_path is not None:
        raise RunnerError(f"Provide either inline text or path for {description}, not both")
    if inline_text is None and source_path is None:
        raise RunnerError(f"Missing {description}")

    ensure_parent(destination)
    if inline_text is not None:
        destination.write_text(inline_text, encoding="utf-8")
        return

    copy_file(resolve_repo_path(source_path), destination)


def normalize_artifact_entries(entries: list[Any], prefix: str) -> list[dict[str, Any]]:
    normalized: list[dict[str, Any]] = []
    for index, entry in enumerate(entries, start=1):
        if isinstance(entry, str):
            source_path = resolve_repo_path(entry)
            normalized.append({"path": str(source_path), "dest_name": source_path.name})
            continue
        if not isinstance(entry, dict):
            raise RunnerError(f"{prefix} entries must be strings or objects")
        if "dest_name" not in entry:
            entry = dict(entry)
            suffix = Path(entry.get("path", f"{prefix}_{index}")).suffix
            if prefix == "chart":
                entry["dest_name"] = "chart.png" if index == 1 else f"chart_{index}.png"
            else:
                entry["dest_name"] = f"{prefix}_{index:02d}{suffix}"
        normalized.append(entry)
    return normalized


def materialize_artifact(
    entry: dict[str, Any], destination_root: Path, *, category: str
) -> Path:
    destination = destination_root / entry["dest_name"]
    ensure_parent(destination)
    has_path = "path" in entry and entry["path"] is not None
    has_content = "content" in entry and entry["content"] is not None
    if has_path == has_content:
        raise RunnerError(f"{category} artifact must provide exactly one of path or content")

    if has_path:
        copy_file(resolve_repo_path(entry["path"]), destination)
    else:
        destination.write_text(str(entry["content"]), encoding="utf-8")
    return destination


def relative_to_repo(path: Path) -> str:
    return path.relative_to(repo_root()).as_posix()


def required_file(path: Path, description: str) -> None:
    if not path.exists():
        raise RunnerError(f"Missing {description}: {path}")


def capture(spec_path: Path, overwrite: bool = False) -> Path:
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    date = spec.get("date")
    slug = spec.get("slug")
    if not date or not slug:
        raise RunnerError("Spec must include date and slug")

    run_dir = resolve_repo_path(ARTIFACT_ROOT / f"{date}-{slug}")
    if run_dir.exists():
        if not overwrite:
            raise RunnerError(f"Run directory already exists: {run_dir}")
        remove_dir(run_dir)

    inputs_dir = run_dir / "inputs"
    derived_dir = run_dir / "derived"
    inputs_dir.mkdir(parents=True, exist_ok=True)
    derived_dir.mkdir(parents=True, exist_ok=True)

    report_path = run_dir / REPORT_FILENAME
    materialize_text(
        inline_text=spec.get("report_markdown"),
        source_path=spec.get("report_markdown_path"),
        destination=report_path,
        description="report markdown",
    )
    report_text = report_path.read_text(encoding="utf-8")

    code_path = run_dir / CODE_FILENAME
    materialize_text(
        inline_text=spec.get("analysis_code"),
        source_path=spec.get("analysis_code_path"),
        destination=code_path,
        description="analysis code",
    )

    calc_log_path = run_dir / CALC_LOG_FILENAME
    calc_log_source = spec.get("calc_log_path")
    calc_log_entries = spec.get("calc_log_entries")
    if calc_log_source and calc_log_entries is not None:
        raise RunnerError("Provide either calc_log_path or calc_log_entries, not both")
    if calc_log_source:
        copy_file(resolve_repo_path(calc_log_source), calc_log_path)
    elif calc_log_entries is not None:
        if not isinstance(calc_log_entries, list):
            raise RunnerError("calc_log_entries must be a list")
        write_jsonl(calc_log_path, calc_log_entries)
    else:
        raise RunnerError("Spec must include calc_log_path or calc_log_entries")

    original_calc_index = calc_log_index(calc_log_path)
    cited_calc_ids = extract_calc_refs(report_text)

    numeric_analysis = bool(spec.get("numeric_analysis", True))
    if numeric_analysis and not cited_calc_ids:
        raise RunnerError("Numeric analyses must cite at least one [calc:...] reference in report.md")
    missing_refs = [calc_id for calc_id in cited_calc_ids if calc_id not in original_calc_index]
    if missing_refs:
        raise RunnerError(f"Report cites calc_ids missing from calc-log: {', '.join(missing_refs)}")

    source_entries = normalize_artifact_entries(spec.get("source_artifacts", []), "source")
    derived_entries = normalize_artifact_entries(spec.get("derived_artifacts", []), "table")
    chart_entries = normalize_artifact_entries(spec.get("chart_artifacts", []), "chart")

    source_paths = [
        relative_to_repo(materialize_artifact(entry, inputs_dir, category="source"))
        for entry in source_entries
    ]
    derived_paths = [
        relative_to_repo(materialize_artifact(entry, derived_dir, category="derived"))
        for entry in derived_entries
    ]
    chart_paths = [
        relative_to_repo(materialize_artifact(entry, run_dir, category="chart"))
        for entry in chart_entries
    ]

    if numeric_analysis and not chart_paths:
        raise RunnerError("Numeric analyses must include at least one chart artifact")

    verification_artifact = relative_to_repo(run_dir / VERIFICATION_FILENAME)
    verification_status = "Not Run" if numeric_analysis else "Not Required"

    manifest = {
        "skill": "data-analysis",
        "run_id": f"{date}-{slug}",
        "created_at": now_iso(),
        "analysis_type": spec.get("analysis_type", "Unknown"),
        "question": spec.get("question", ""),
        "run_dir": relative_to_repo(run_dir),
        "report": relative_to_repo(report_path),
        "charts": chart_paths,
        "code_artifact": relative_to_repo(code_path),
        "calc_log_artifact": relative_to_repo(calc_log_path),
        "source_artifacts": source_paths,
        "derived_artifacts": derived_paths,
        "verification_artifact": verification_artifact,
        "verification_status": verification_status,
        "reproducible": "Yes" if numeric_analysis else "Partial",
        "report_calc_ids": cited_calc_ids,
        "numeric_analysis": numeric_analysis,
        "python_version": sys.version.split()[0],
        "dependencies": spec.get("dependencies", ["python3"]),
        "rerun_command": (
            f"python3 .claude/skills/data-analysis/analysis_runner.py verify "
            f"--run-dir {relative_to_repo(run_dir)}"
        ),
    }

    write_yaml_subset(run_dir / MANIFEST_FILENAME, manifest)
    verification_payload = {
        "status": verification_status,
        "verified_at": None,
        "checks_run": [],
        "failures": [],
        "comparison_mode": "not_run",
        "replay_command": replay_command(run_dir) if numeric_analysis else [],
    }
    (run_dir / VERIFICATION_FILENAME).write_text(
        json.dumps(verification_payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return run_dir


def replay_command(run_dir: Path) -> list[str]:
    return [
        sys.executable,
        str(run_dir / CODE_FILENAME),
        "--input-dir",
        str(run_dir / "inputs"),
        "--derived-dir",
        str(run_dir / "replay" / "derived"),
        "--chart-dir",
        str(run_dir / "replay"),
        "--calc-log",
        str(run_dir / "replay" / CALC_LOG_FILENAME),
    ]


def verify(run_dir_arg: str) -> Path:
    run_dir = resolve_repo_path(run_dir_arg)
    manifest_path = run_dir / MANIFEST_FILENAME
    required_file(manifest_path, "manifest")
    manifest = read_yaml_subset(manifest_path)

    verification_path = run_dir / VERIFICATION_FILENAME
    if not manifest.get("numeric_analysis", True):
        payload = {
            "status": "Not Required",
            "verified_at": now_iso(),
            "checks_run": ["non_numeric_analysis"],
            "failures": [],
            "comparison_mode": "not_applicable",
            "replay_command": [],
        }
        verification_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        manifest["verification_status"] = "Not Required"
        write_yaml_subset(manifest_path, manifest)
        return verification_path

    report_path = resolve_repo_path(manifest["report"])
    code_path = resolve_repo_path(manifest["code_artifact"])
    calc_log_path = resolve_repo_path(manifest["calc_log_artifact"])
    required_file(report_path, "report")
    required_file(code_path, "analysis code")
    required_file(calc_log_path, "calc-log")

    replay_dir = run_dir / "replay"
    remove_dir(replay_dir)
    (replay_dir / "derived").mkdir(parents=True, exist_ok=True)

    command = replay_command(run_dir)
    env = os.environ.copy()
    env.update(
        {
            "PM_AGENT_INPUT_DIR": str(run_dir / "inputs"),
            "PM_AGENT_DERIVED_DIR": str(replay_dir / "derived"),
            "PM_AGENT_CHART_DIR": str(replay_dir),
            "PM_AGENT_CALC_LOG": str(replay_dir / CALC_LOG_FILENAME),
        }
    )
    completed = subprocess.run(
        command,
        cwd=repo_root(),
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )

    checks_run: list[str] = ["replay_execution"]
    failures: list[dict[str, Any]] = []
    comparison_mode = "sha256"
    chart_results: dict[str, Any] = {}

    if completed.returncode != 0:
        failures.append(
            {
                "check": "replay_execution",
                "message": "analysis.py exited non-zero during verification",
                "returncode": completed.returncode,
                "stdout": completed.stdout,
                "stderr": completed.stderr,
            }
        )
    else:
        original_calc_index = calc_log_index(calc_log_path)
        replay_calc_path = replay_dir / CALC_LOG_FILENAME
        try:
            replay_calc_index = calc_log_index(replay_calc_path)
        except RunnerError as exc:
            failures.append({"check": "replay_calc_log", "message": str(exc)})
            replay_calc_index = {}

        checks_run.append("report_calc_refs")
        report_text = report_path.read_text(encoding="utf-8")
        cited_ids = extract_calc_refs(report_text)
        if not cited_ids:
            failures.append(
                {
                    "check": "report_calc_refs",
                    "message": "Numeric analyses must cite at least one [calc:...] reference",
                }
            )
        else:
            missing_original = [calc_id for calc_id in cited_ids if calc_id not in original_calc_index]
            missing_replay = [calc_id for calc_id in cited_ids if calc_id not in replay_calc_index]
            if missing_original:
                failures.append(
                    {
                        "check": "report_calc_refs",
                        "message": f"Cited calc_ids missing from original calc-log: {missing_original}",
                    }
                )
            if missing_replay:
                failures.append(
                    {
                        "check": "report_calc_refs",
                        "message": f"Cited calc_ids missing from replay calc-log: {missing_replay}",
                    }
                )

        checks_run.append("manifest_files_exist")
        declared_paths = [
            manifest["report"],
            manifest["code_artifact"],
            manifest["calc_log_artifact"],
            *manifest.get("source_artifacts", []),
            *manifest.get("derived_artifacts", []),
            *manifest.get("charts", []),
        ]
        for declared in declared_paths:
            resolved = resolve_repo_path(declared)
            if not resolved.exists():
                failures.append(
                    {
                        "check": "manifest_files_exist",
                        "message": f"Manifest-declared file is missing: {declared}",
                    }
                )

        checks_run.append("derived_artifacts_match")
        for declared in manifest.get("derived_artifacts", []):
            original = resolve_repo_path(declared)
            replayed = replay_dir / "derived" / Path(declared).name
            if not replayed.exists():
                failures.append(
                    {
                        "check": "derived_artifacts_match",
                        "message": f"Replay did not regenerate derived artifact {Path(declared).name}",
                    }
                )
                continue
            if sha256sum(original) != sha256sum(replayed):
                failures.append(
                    {
                        "check": "derived_artifacts_match",
                        "message": f"Derived artifact hash mismatch for {Path(declared).name}",
                    }
                )

        checks_run.append("calc_results_match")
        if replay_calc_index:
            if set(original_calc_index) != set(replay_calc_index):
                failures.append(
                    {
                        "check": "calc_results_match",
                        "message": "Replay calc-log calc_id set differs from original",
                        "original_only": sorted(set(original_calc_index) - set(replay_calc_index)),
                        "replay_only": sorted(set(replay_calc_index) - set(original_calc_index)),
                    }
                )
            else:
                for calc_id, original_entry in original_calc_index.items():
                    replay_entry = replay_calc_index[calc_id]
                    for field in ("formula", "units"):
                        if original_entry.get(field) != replay_entry.get(field):
                            failures.append(
                                {
                                    "check": "calc_results_match",
                                    "message": f"Replay {field} mismatch for {calc_id}",
                                }
                            )
                    if normalize_result(original_entry.get("result")) != normalize_result(
                        replay_entry.get("result")
                    ):
                        failures.append(
                            {
                                "check": "calc_results_match",
                                "message": f"Replay result mismatch for {calc_id}",
                            }
                        )

        checks_run.append("chart_artifacts_match")
        for declared in manifest.get("charts", []):
            original = resolve_repo_path(declared)
            replayed = replay_dir / Path(declared).name
            if not replayed.exists():
                failures.append(
                    {
                        "check": "chart_artifacts_match",
                        "message": f"Replay did not regenerate chart {Path(declared).name}",
                    }
                )
                continue
            try:
                comparison = compare_png(original, replayed)
            except RunnerError as exc:
                failures.append({"check": "chart_artifacts_match", "message": str(exc)})
                continue
            chart_results[Path(declared).name] = {
                "status": comparison.status,
                "mode": comparison.mode,
                **comparison.details,
            }
            if comparison.status != "Passed":
                failures.append(
                    {
                        "check": "chart_artifacts_match",
                        "message": f"Chart comparison failed for {Path(declared).name}",
                        "details": comparison.details,
                    }
                )
            elif comparison.mode != "sha256":
                comparison_mode = comparison.mode

    status = "Passed" if not failures else "Failed"
    payload = {
        "status": status,
        "verified_at": now_iso(),
        "checks_run": checks_run,
        "failures": failures,
        "comparison_mode": comparison_mode,
        "chart_results": chart_results,
        "replay_command": command,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }
    verification_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    manifest["verification_status"] = status
    write_yaml_subset(manifest_path, manifest)

    if status != "Passed":
        raise RunnerError(f"Replay verification failed for {relative_to_repo(run_dir)}")
    return verification_path


def finalize(spec_path: Path, overwrite: bool = False) -> Path:
    run_dir = capture(spec_path, overwrite=overwrite)
    verify(relative_to_repo(run_dir))
    return run_dir


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    capture_parser = subparsers.add_parser("capture", help="Create the run bundle without replay verification")
    capture_parser.add_argument("--spec", required=True, help="Path to JSON spec file")
    capture_parser.add_argument("--overwrite", action="store_true", help="Replace an existing run directory")

    verify_parser = subparsers.add_parser("verify", help="Replay and verify an existing run bundle")
    verify_parser.add_argument("--run-dir", required=True, help="Run directory under knowledge/data-analyses/")

    finalize_parser = subparsers.add_parser("finalize", help="Capture then verify a run bundle")
    finalize_parser.add_argument("--spec", required=True, help="Path to JSON spec file")
    finalize_parser.add_argument("--overwrite", action="store_true", help="Replace an existing run directory")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "capture":
            run_dir = capture(resolve_repo_path(args.spec), overwrite=args.overwrite)
            print(relative_to_repo(run_dir))
            return 0
        if args.command == "verify":
            verification_path = verify(args.run_dir)
            print(relative_to_repo(verification_path))
            return 0
        if args.command == "finalize":
            run_dir = finalize(resolve_repo_path(args.spec), overwrite=args.overwrite)
            print(relative_to_repo(run_dir))
            return 0
        parser.error(f"Unknown command: {args.command}")
    except RunnerError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
