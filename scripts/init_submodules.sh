#!/bin/sh
# Initialize and update git submodules recursively.
set -e
if [ ! -f .gitmodules ]; then
  echo "No submodules defined." >&2
  exit 1
fi
# Sync submodule URLs in case they've changed
git submodule sync --recursive
# Initialize and update
git submodule update --init --recursive
