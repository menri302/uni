#!/bin/zsh
# Kopiert die aktuellen Zusammenfassungen aus Obsidian und lädt sie auf GitHub hoch.
# Aufruf:  ~/Developer/quartz/veroeffentlichen.sh
set -e
export PATH="$HOME/.local/node/bin:$PATH"
cd "$(dirname "$0")"
python3 -I scripts/sync-vault.py
npx quartz sync
