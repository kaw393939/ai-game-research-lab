#!/bin/sh
set -eu
project_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
exec "$project_dir/.local-tts/py312/bin/python" "$project_dir/scripts/narrate.py" "$@"
