#!/bin/sh
set -eu

# CT111 keeps the shared Playwright browser install outside the agent's HOME.
PLAYWRIGHT_BROWSERS_PATH="${PLAYWRIGHT_BROWSERS_PATH:-/opt/ms-playwright}"
export PLAYWRIGHT_BROWSERS_PATH

if [ "$#" -eq 0 ]; then
    echo "usage: with-playwright-browser.sh <command> [args...]" >&2
    exit 2
fi

exec "$@"
