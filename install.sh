#!/bin/bash
# Usage: ./install.sh [skill-name]
# With no args: registers all skills for this repo checkout
# With a name: registers just that skill (e.g. ./install.sh doc-review)
# These commands are not self-contained installs; they still depend on this repo's
# references/ and company/ files resolving from the current checkout.

COMMANDS_DIR="$HOME/.claude/commands"
mkdir -p "$COMMANDS_DIR"

install_skill() {
  local name=$1
  local src="skills/$name/SKILL.md"
  if [ -f "$src" ]; then
    cp "$src" "$COMMANDS_DIR/$name.md"
    echo "Registered /$name → $COMMANDS_DIR/$name.md"
  else
    echo "Skill not found: $name"
  fi
}

KNOWN_SKILLS=("doc-review" "prd-draft" "generate-tasks" "decision-log" "meeting-brief" "status-update" "sprint-plan" "retro-synthesis" "launch-checklist" "user-feedback" "data-analysis" "competitive-intel" "business-case" "presentation-deck")

if [ -z "$1" ]; then
  for name in "${KNOWN_SKILLS[@]}"; do
    install_skill "$name"
  done
else
  install_skill "$1"
fi
