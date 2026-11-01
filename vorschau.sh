#!/bin/zsh
# Kopiert die aktuellen Zusammenfassungen und startet die lokale Vorschau auf http://localhost:8080
export PATH="$HOME/.local/node/bin:$PATH"
cd "$(dirname "$0")"
python3 -I scripts/sync-vault.py
npx quartz build --serve
