#!/bin/bash
# Usage: ./install.sh [skill-name]
# With no args: installs all skills
# With a name: installs just that skill (e.g. ./install.sh doc-review)

COMMANDS_DIR="$HOME/.claude/commands"
mkdir -p "$COMMANDS_DIR"

install_skill() {
  local name=$1
  local src="skills/$name/SKILL.md"
  if [ -f "$src" ]; then
    cp "$src" "$COMMANDS_DIR/$name.md"
    echo "Installed /$name → $COMMANDS_DIR/$name.md"
  else
    echo "Skill not found: $name"
  fi
}

KNOWN_SKILLS=("doc-review" "prd-draft" "generate-tasks" "decision-log" "meeting-brief" "status-update" "sprint-plan" "retro-synthesis")

if [ -z "$1" ]; then
  for name in "${KNOWN_SKILLS[@]}"; do
    install_skill "$name"
  done
else
  install_skill "$1"
fi
