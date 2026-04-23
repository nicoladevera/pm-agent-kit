#!/usr/bin/env python3
"""Validate and apply safe formatting fixes to presentation-deck outputs."""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import re
import sys
import zipfile
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


DEFAULT_BRAND_VARS = {
    "--brand-primary": "#2D3142",
    "--brand-secondary": "#4F5D75",
    "--brand-accent": "#E07A5F",
    "--brand-background": "#FAFAF8",
    "--brand-text": "#2D3142",
    "--brand-text-light": "#FFFFFF",
    "--color-positive": "#4A7C59",
    "--color-negative": "#C1442E",
    "--color-caution": "#D4A843",
    "--color-neutral": "#9A9BA3",
    "--font-heading": "'Georgia', serif",
    "--font-body": "'Helvetica Neue', 'Arial', sans-serif",
    "--slide-padding": "5% 6%",
}

WORD_BUDGETS = {
    "live": 25,
    "pre-read": 60,
    "standalone": 80,
}

TIER_MIN_REM = {
    ".tier-title": 2.25,
    ".tier-headline": 1.75,
    ".tier-supporting": 1.5,
    ".tier-caption": 0.875,
}

COPY_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "figcaption"}
COPY_CLASS_PREFIXES = (
    "tier-",
    "nextstep-",
    "data-note",
    "def-name",
    "def-text",
    "def-threshold",
    "watch-bar",
)
EXCLUDED_WORD_COUNT_TAGS = {"svg", "style", "script"}
EXCLUDED_WORD_COUNT_CLASSES = {
    "speaker-notes",
    "chart-frame",
    "slide-nav",
}

ASSET_ATTRS = {
    "img": "src",
    "script": "src",
    "link": "href",
}

REMOTE_SCHEMES = ("http://", "https://", "//")
INLINE_SCHEMES = ("data:", "#", "javascript:")
SLIDE_FIX_MARKER_BEGIN = "<!-- slides_postprocessing:begin -->"
SLIDE_FIX_MARKER_END = "<!-- slides_postprocessing:end -->"
SLIDE_FIX_STYLE_ID = "slides-postprocessing-fixes"
PPTX_16_9 = (12188952, 6858000)


@dataclass
class SlideSummary:
    slide_id: str | None
    classes: list[str]
    text_chunks: list[str] = field(default_factory=list)
    data_img_count: int = 0
    data_svg_count: int = 0
    divider_num_text: str | None = None  # text inside .divider-num on .slide-divider slides

    @property
    def word_count(self) -> int:
        text = " ".join(self.text_chunks)
        return len(re.findall(r"\b[\w%+.-]+\b", text))


@dataclass
class HtmlAssetRef:
    tag: str
    attr: str
    value: str
    classes: list[str] = field(default_factory=list)


@dataclass
class CssFontSizeInfo:
    comparable_rem: float
    source: str


@dataclass
class CheckResult:
    file: str
    format: str
    status: str
    fixes_applied: list[str]
    warnings: list[str]
    errors: list[str]
    metadata: dict[str, Any]

    def to_json(self) -> str:
        payload = {
            "file": self.file,
            "format": self.format,
            "status": self.status,
            "fixes_applied": self.fixes_applied,
            "warnings": self.warnings,
            "errors": self.errors,
            "metadata": self.metadata,
        }
        return json.dumps(payload, indent=2, sort_keys=True)


class DeckHtmlParser(HTMLParser):
    """Collects structural metadata from a generated slide deck."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.slide_sections: list[SlideSummary] = []
        self.asset_refs: list[HtmlAssetRef] = []
        self._current_slide: SlideSummary | None = None
        self._current_slide_depth = 0
        self._ignore_depth = 0
        self._style_depth = 0
        self._script_depth = 0
        self._tag_stack: list[tuple[str, list[str]]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key.lower(): (value or "") for key, value in attrs}
        class_names = attr_map.get("class", "").split()
        tag = tag.lower()
        self._tag_stack.append((tag, class_names))

        if tag == "section":
            if self._current_slide is None and "slide" in class_names:
                self._current_slide = SlideSummary(
                    slide_id=attr_map.get("id") or None,
                    classes=class_names,
                )
                self.slide_sections.append(self._current_slide)
                self._current_slide_depth = 1
            elif self._current_slide is not None:
                self._current_slide_depth += 1

        if tag == "aside" and "speaker-notes" in class_names:
            self._ignore_depth += 1

        if tag == "style":
            self._style_depth += 1

        if tag == "script":
            self._script_depth += 1

        if tag in ASSET_ATTRS:
            attr_name = ASSET_ATTRS[tag]
            value = attr_map.get(attr_name)
            if value:
                self.asset_refs.append(
                    HtmlAssetRef(tag=tag, attr=attr_name, value=value, classes=class_names)
                )

        if self._current_slide and "slide-data" in self._current_slide.classes:
            if tag == "img":
                self._current_slide.data_img_count += 1
            if tag == "svg":
                self._current_slide.data_svg_count += 1

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "aside" and self._ignore_depth:
            self._ignore_depth -= 1
        if tag == "style" and self._style_depth:
            self._style_depth -= 1
        if tag == "script" and self._script_depth:
            self._script_depth -= 1
        if tag == "section" and self._current_slide is not None:
            self._current_slide_depth -= 1
            if self._current_slide_depth <= 0:
                self._current_slide = None
                self._current_slide_depth = 0
        if self._tag_stack:
            self._tag_stack.pop()

    def _has_copy_context(self) -> bool:
        for tag, classes in self._tag_stack:
            if tag in EXCLUDED_WORD_COUNT_TAGS:
                return False
            if any(class_name in EXCLUDED_WORD_COUNT_CLASSES for class_name in classes):
                return False
        for tag, classes in reversed(self._tag_stack):
            if tag in COPY_TAGS:
                return True
            if any(
                class_name == prefix or class_name.startswith(prefix)
                for class_name in classes
                for prefix in COPY_CLASS_PREFIXES
            ):
                return True
        return False

    def handle_data(self, data: str) -> None:
        if self._current_slide is None:
            return
        if self._ignore_depth or self._style_depth or self._script_depth:
            return
        text = data.strip()
        if text and self._has_copy_context():
            self._current_slide.text_chunks.append(text)
        # Capture ghost number text on section divider slides
        if (
            text
            and "slide-divider" in self._current_slide.classes
            and any("divider-num" in classes for _, classes in self._tag_stack)
        ):
            self._current_slide.divider_num_text = text


def is_remote_ref(value: str) -> bool:
    return value.startswith(REMOTE_SCHEMES)


def is_inline_ref(value: str) -> bool:
    return value.startswith(INLINE_SCHEMES)


def is_local_ref(value: str) -> bool:
    return not is_remote_ref(value) and not is_inline_ref(value)


def load_html_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_style_blocks(html_text: str) -> str:
    blocks = re.findall(r"<style\b[^>]*>(.*?)</style>", html_text, flags=re.IGNORECASE | re.DOTALL)
    return "\n".join(blocks)


def parse_html(html_text: str) -> DeckHtmlParser:
    parser = DeckHtmlParser()
    parser.feed(html_text)
    return parser


def has_css_property(style_text: str, selector: str, property_name: str, pattern: str) -> bool:
    block_pattern = re.compile(
        rf"{re.escape(selector)}\s*\{{(?P<body>.*?)\}}", flags=re.IGNORECASE | re.DOTALL
    )
    for match in block_pattern.finditer(style_text):
        body = match.group("body")
        if re.search(rf"{re.escape(property_name)}\s*:\s*{pattern}", body, flags=re.IGNORECASE):
            return True
    return False


def has_slide_aspect_ratio(style_text: str) -> bool:
    return has_css_property(style_text, ".slide", "aspect-ratio", r"16\s*/\s*9")


def has_slide_max_width(style_text: str) -> bool:
    return has_css_property(style_text, ".slide", "max-width", r"1200px")


def has_slide_width_100vw(style_text: str) -> bool:
    return has_css_property(style_text, ".slide", "width", r"100vw")


def has_slide_height_100vh(style_text: str) -> bool:
    return has_css_property(style_text, ".slide", "height", r"100vh")


def has_deck_scroll_snap(style_text: str) -> bool:
    return has_css_property(style_text, ".deck", "scroll-snap-type", r"y\s+mandatory")


def has_deck_height_100vh(style_text: str) -> bool:
    return has_css_property(style_text, ".deck", "height", r"100vh")


def has_fixed_stage_model(style_text: str) -> bool:
    return has_slide_aspect_ratio(style_text) and has_slide_max_width(style_text)


def has_viewport_slide_model(style_text: str) -> bool:
    return (
        has_slide_width_100vw(style_text)
        and has_slide_height_100vh(style_text)
        and has_deck_scroll_snap(style_text)
        and has_deck_height_100vh(style_text)
    )


def has_default_notes_hidden(style_text: str) -> bool:
    return has_css_property(style_text, ".speaker-notes", "display", r"none\b")


def has_print_rules(style_text: str) -> bool:
    if "@media print" not in style_text or "@page" not in style_text:
        return False
    has_note_rule = ".speaker-notes" in style_text
    has_page_break_rule = "page-break-after" in style_text or re.search(
        r"break-after\s*:\s*page\b",
        style_text,
        flags=re.IGNORECASE,
    )
    return bool(has_note_rule and has_page_break_rule)


def missing_brand_vars(style_text: str) -> list[str]:
    missing: list[str] = []
    for name in DEFAULT_BRAND_VARS:
        if name not in style_text:
            missing.append(name)
    return missing


def css_font_size_info(style_text: str, selector: str) -> CssFontSizeInfo | None:
    block_pattern = re.compile(
        rf"{re.escape(selector)}\s*\{{(?P<body>.*?)\}}", flags=re.IGNORECASE | re.DOTALL
    )
    for match in block_pattern.finditer(style_text):
        body = match.group("body")
        clamp_match = re.search(
            r"font-size\s*:\s*clamp\(\s*([0-9.]+)rem\s*,\s*[^,]+\s*,\s*([0-9.]+)rem\s*\)",
            body,
            flags=re.IGNORECASE,
        )
        if clamp_match:
            return CssFontSizeInfo(
                comparable_rem=float(clamp_match.group(2)),
                source="maximum responsive size",
            )
        rem_match = re.search(r"font-size\s*:\s*([0-9.]+)rem", body, flags=re.IGNORECASE)
        if rem_match:
            return CssFontSizeInfo(
                comparable_rem=float(rem_match.group(1)),
                source="declared size",
            )
    return None


def local_asset_path(html_path: Path, value: str) -> Path:
    return (html_path.parent / value).resolve()


def mime_for_path(path: Path) -> str:
    mime, _ = mimetypes.guess_type(path.name)
    return mime or "application/octet-stream"


def encode_data_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_for_path(path)};base64,{encoded}"


def replace_or_insert_fix_block(html_text: str, css: str) -> str:
    block = (
        f"{SLIDE_FIX_MARKER_BEGIN}\n"
        f"<style id=\"{SLIDE_FIX_STYLE_ID}\">\n{css}\n</style>\n"
        f"{SLIDE_FIX_MARKER_END}"
    )
    marker_pattern = re.compile(
        rf"{re.escape(SLIDE_FIX_MARKER_BEGIN)}.*?{re.escape(SLIDE_FIX_MARKER_END)}",
        flags=re.DOTALL,
    )
    if marker_pattern.search(html_text):
        return marker_pattern.sub(block, html_text)
    if "</head>" in html_text:
        return html_text.replace("</head>", f"{block}\n</head>", 1)
    return f"{block}\n{html_text}"


def inject_css_fixes(
    html_text: str,
    *,
    missing_vars_list: list[str],
    fix_notes_hidden: bool,
    fix_print_rules: bool,
) -> tuple[str, list[str]]:
    css_parts: list[str] = []
    fixes: list[str] = []

    if missing_vars_list:
        lines = [":root {"]
        for name in missing_vars_list:
            lines.append(f"  {name}: {DEFAULT_BRAND_VARS[name]};")
        lines.append("}")
        css_parts.append("\n".join(lines))
        fixes.append("Backfilled missing brand CSS custom properties.")

    if fix_notes_hidden:
        css_parts.append(".speaker-notes { display: none !important; }")
        fixes.append("Forced speaker notes to stay hidden by default.")

    if fix_print_rules:
        css_parts.append(
            """
@media print {
  @page {
    size: 13.333in 7.5in;
    margin: 0;
  }
  .slide {
    width: 100% !important;
    height: 100vh !important;
    page-break-after: always;
    break-after: page;
    aspect-ratio: auto !important;
  }
  .speaker-notes,
  .slide-nav {
    display: none !important;
  }
  .deck {
    overflow: visible !important;
    height: auto !important;
  }
}
""".strip()
        )
        fixes.append("Injected print CSS for one-slide-per-page rendering.")

    if not css_parts:
        return html_text, []

    css = "\n\n".join(css_parts)
    return replace_or_insert_fix_block(html_text, css), fixes


def inline_local_images(html_text: str, html_path: Path) -> tuple[str, list[str]]:
    fixes: list[str] = []
    img_pattern = re.compile(r'(<img\b[^>]*\bsrc=)(["\'])([^"\']+)\2', flags=re.IGNORECASE)

    def replacer(match: re.Match[str]) -> str:
        prefix, quote, src = match.groups()
        if not is_local_ref(src):
            return match.group(0)
        asset_path = local_asset_path(html_path, src)
        if not asset_path.exists() or not asset_path.is_file():
            return match.group(0)
        fixes.append(f"Embedded local image asset '{src}' as a data URI.")
        return f"{prefix}{quote}{encode_data_uri(asset_path)}{quote}"

    return img_pattern.sub(replacer, html_text), fixes


def analyze_html(
    html_text: str,
    *,
    html_path: Path,
    delivery_context: str,
    visual_mode: str,
    expected_slide_count: int | None,
) -> tuple[list[str], list[str], dict[str, Any]]:
    errors: list[str] = []
    warnings: list[str] = []
    parser = parse_html(html_text)
    style_text = extract_style_blocks(html_text)
    missing_vars_list = missing_brand_vars(style_text)

    if not parser.slide_sections:
        errors.append("No <section class=\"slide ...\"> elements found in the HTML deck.")

    slide_count = len(parser.slide_sections)
    if expected_slide_count is not None and slide_count != expected_slide_count:
        errors.append(
            f"Expected {expected_slide_count} slides but found {slide_count} slide sections."
        )

    for asset in parser.asset_refs:
        value = asset.value.strip()
        if is_remote_ref(value):
            errors.append(f"HTML is not self-contained: external {asset.tag} reference '{value}'.")
        elif is_local_ref(value):
            if asset.tag == "img":
                errors.append(f"HTML references local image asset '{value}' instead of embedding it.")
            else:
                errors.append(
                    f"HTML is not self-contained: local {asset.tag} reference '{value}' must be inlined."
                )

    if not has_fixed_stage_model(style_text) and not has_viewport_slide_model(style_text):
        errors.append(
            "Missing a supported slide layout model. HTML must use either a fixed 16:9 stage "
            "or full-viewport slides with scroll-snap."
        )

    if not has_default_notes_hidden(style_text):
        errors.append("Speaker notes are not explicitly hidden by default.")

    if not has_print_rules(style_text):
        errors.append("Missing print CSS for one-slide-per-page rendering.")

    if missing_vars_list:
        errors.append(
            "Missing required brand CSS variables: " + ", ".join(sorted(missing_vars_list)) + "."
        )

    if visual_mode == "generated":
        for slide in parser.slide_sections:
            if "slide-data" in slide.classes and slide.data_img_count and not slide.data_svg_count:
                slide_label = slide.slide_id or "(unnamed slide)"
                errors.append(
                    f"Generated chart slide {slide_label} uses raster <img> content instead of inline SVG."
                )

    budget = WORD_BUDGETS[delivery_context]
    soft_limit = int(budget * 1.6)
    for slide in parser.slide_sections:
        if slide.word_count > soft_limit:
            slide_label = slide.slide_id or "(unnamed slide)"
            warnings.append(
                f"Slide {slide_label} appears dense for {delivery_context} delivery "
                f"({slide.word_count} visible words, budget {budget})."
            )

    for selector, minimum in TIER_MIN_REM.items():
        size_info = css_font_size_info(style_text, selector)
        if size_info is not None and size_info.comparable_rem < minimum:
            warnings.append(
                f"{selector} {size_info.source} is {size_info.comparable_rem:.3g}rem, "
                f"below the recommended {minimum:.3g}rem minimum."
            )

    # Section divider ghost number consistency
    divider_slides = [s for s in parser.slide_sections if "slide-divider" in s.classes]
    if divider_slides:
        numbered = [s for s in divider_slides if s.divider_num_text]
        if numbered and len(divider_slides) == 1:
            warnings.append(
                f"Single section divider has a ghost number ('{numbered[0].divider_num_text}'). "
                f"A ghost number on a lone divider implies a multi-section structure that doesn't exist. "
                f"Remove the ghost number or add numbered dividers for every section."
            )
        elif numbered and len(numbered) < len(divider_slides):
            warnings.append(
                f"Section dividers have inconsistent ghost numbering: "
                f"{len(numbered)} of {len(divider_slides)} divider slide(s) have a .divider-num element. "
                f"Either all dividers should be numbered sequentially or none should."
            )

    metadata = {
        "slide_count": slide_count,
        "missing_brand_vars": missing_vars_list,
        "has_fixed_stage_model": has_fixed_stage_model(style_text),
        "has_viewport_slide_model": has_viewport_slide_model(style_text),
        "has_default_notes_hidden": has_default_notes_hidden(style_text),
        "has_print_rules": has_print_rules(style_text),
    }
    return errors, warnings, metadata


def check_html(
    path: Path,
    *,
    delivery_context: str,
    visual_mode: str,
    expected_slide_count: int | None,
    fix: bool,
) -> CheckResult:
    html_text = load_html_text(path)
    fixes_applied: list[str] = []

    if fix:
        style_text = extract_style_blocks(html_text)
        html_text, image_fixes = inline_local_images(html_text, path)
        fixes_applied.extend(image_fixes)

        html_text, css_fixes = inject_css_fixes(
            html_text,
            missing_vars_list=missing_brand_vars(style_text),
            fix_notes_hidden=not has_default_notes_hidden(style_text),
            fix_print_rules=not has_print_rules(style_text),
        )
        fixes_applied.extend(css_fixes)

        if fixes_applied:
            path.write_text(html_text, encoding="utf-8")

    final_text = load_html_text(path)
    errors, warnings, metadata = analyze_html(
        final_text,
        html_path=path,
        delivery_context=delivery_context,
        visual_mode=visual_mode,
        expected_slide_count=expected_slide_count,
    )
    status = "failed" if errors else "passed"
    return CheckResult(
        file=str(path),
        format="html",
        status=status,
        fixes_applied=fixes_applied,
        warnings=warnings,
        errors=errors,
        metadata=metadata,
    )


def count_pdf_pages(path: Path) -> int | None:
    try:
        content = path.read_bytes()
    except OSError:
        return None
    return len(re.findall(rb"/Type\s*/Page\b", content))


def check_pdf(path: Path, expected_slide_count: int | None) -> CheckResult:
    errors: list[str] = []
    warnings: list[str] = []
    metadata: dict[str, Any] = {}

    if not path.exists():
        errors.append(f"Missing PDF output: {path}")
    else:
        page_count = count_pdf_pages(path)
        metadata["page_count"] = page_count
        if expected_slide_count is not None and page_count is not None and page_count != expected_slide_count:
            errors.append(
                f"Expected {expected_slide_count} PDF pages but found {page_count}."
            )
        elif page_count is None:
            warnings.append("Could not determine PDF page count.")

    return CheckResult(
        file=str(path),
        format="pdf",
        status="failed" if errors else "passed",
        fixes_applied=[],
        warnings=warnings,
        errors=errors,
        metadata=metadata,
    )


def pptx_slide_size(path: Path) -> tuple[int, int] | None:
    with zipfile.ZipFile(path) as archive:
        try:
            xml = archive.read("ppt/presentation.xml").decode("utf-8")
        except KeyError:
            return None
    match = re.search(r"<p:sldSz[^>]*cx=\"(\d+)\"[^>]*cy=\"(\d+)\"", xml)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def count_pptx_slides(path: Path) -> int | None:
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
    except (OSError, zipfile.BadZipFile):
        return None
    return len([name for name in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)])


def check_pptx(path: Path, expected_slide_count: int | None) -> CheckResult:
    errors: list[str] = []
    warnings: list[str] = []
    metadata: dict[str, Any] = {}

    if not path.exists():
        errors.append(f"Missing PPTX output: {path}")
    else:
        slide_count = count_pptx_slides(path)
        metadata["slide_count"] = slide_count
        if expected_slide_count is not None and slide_count is not None and slide_count != expected_slide_count:
            errors.append(
                f"Expected {expected_slide_count} PPTX slides but found {slide_count}."
            )
        slide_size = pptx_slide_size(path)
        metadata["slide_size"] = slide_size
        if slide_size is None:
            warnings.append("Could not determine PPTX slide size.")
        elif slide_size != PPTX_16_9:
            warnings.append(
                "PPTX slide size is not 16:9; expected "
                f"{PPTX_16_9[0]}x{PPTX_16_9[1]}, found {slide_size[0]}x{slide_size[1]}."
            )

    return CheckResult(
        file=str(path),
        format="pptx",
        status="failed" if errors else "passed",
        fixes_applied=[],
        warnings=warnings,
        errors=errors,
        metadata=metadata,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    check_parser = subparsers.add_parser("check", help="Validate a generated slide artifact.")
    check_parser.add_argument("--file", required=True, help="Path to the generated artifact.")
    check_parser.add_argument(
        "--format",
        required=True,
        choices=("html", "pdf", "pptx"),
        help="Artifact format to validate.",
    )
    check_parser.add_argument(
        "--delivery-context",
        default="live",
        choices=tuple(WORD_BUDGETS),
        help="How the slides will be consumed.",
    )
    check_parser.add_argument(
        "--visual-mode",
        default="generated",
        choices=("generated", "reused", "mixed"),
        help="Whether visuals were generated or reused from upstream artifacts.",
    )
    check_parser.add_argument(
        "--expected-slide-count",
        type=int,
        default=None,
        help="Optional expected slide count for PDF/PPTX/page validation.",
    )
    check_parser.add_argument(
        "--fix",
        action="store_true",
        help="Apply safe HTML fixes before returning the final check result.",
    )

    return parser.parse_args()


def run_check(args: argparse.Namespace) -> CheckResult:
    path = Path(args.file)
    if args.format == "html":
        return check_html(
            path,
            delivery_context=args.delivery_context,
            visual_mode=args.visual_mode,
            expected_slide_count=args.expected_slide_count,
            fix=args.fix,
        )
    if args.format == "pdf":
        return check_pdf(path, args.expected_slide_count)
    return check_pptx(path, args.expected_slide_count)


def main() -> int:
    args = parse_args()
    result = run_check(args)
    print(result.to_json())
    return 1 if result.status == "failed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
