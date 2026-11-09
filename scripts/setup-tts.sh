#!/bin/sh
set -eu
project_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
python_bin=${TTS_PYTHON:-python3.12}
"$python_bin" -c 'import sys; assert sys.version_info[:2] == (3, 12), "Use Python 3.12"'
"$python_bin" -m venv "$project_dir/.local-tts/py312"
"$project_dir/.local-tts/py312/bin/python" -m pip install -r "$project_dir/requirements/tts-macos-py312.lock.txt"
printf '%s\n' 'Setup complete. Use scripts/narrate.sh with --download for initial model acquisition.'
