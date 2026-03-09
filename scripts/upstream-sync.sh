#!/usr/bin/env bash
# upstream-sync.sh — Helps sync with vial-qmk, qmk, and holykeebs upstreams
# Usage: ./scripts/upstream-sync.sh [check|sync-vial|sync-holykeebs|status]

set -euo pipefail

VIAL_REMOTE="https://github.com/vial-kb/vial-qmk.git"
QMK_REMOTE="https://github.com/qmk/qmk_firmware.git"
HK_REMOTE="https://github.com/holykeebs/qmk_firmware.git"

# Files we care about from each upstream
VIAL_PATHS="quantum/via quantum/vial keyboards/*/keymaps/vial"
QMK_DRIVER_PATHS="drivers/sensors/azoteq_iqs5xx* drivers/sensors/cirque_pinnacle* drivers/sensors/pimoroni_trackball* drivers/sensors/pmw33xx*"
HK_PATHS="users/holykeebs/"

case "${1:-check}" in
  check)
    echo "=== Checking for upstream updates ==="
    echo "This script checks what's new in each upstream."
    echo "Remotes needed:"
    echo "  git remote add vial-upstream $VIAL_REMOTE"
    echo "  git remote add qmk-upstream $QMK_REMOTE"
    echo "  git remote add hk-upstream $HK_REMOTE"
    echo ""
    echo "Then: git fetch --all"
    echo "Then: git log HEAD..vial-upstream/master --oneline -- $VIAL_PATHS"
    echo "Then: git log HEAD..qmk-upstream/master --oneline -- $QMK_DRIVER_PATHS"
    echo "Then: git log HEAD..hk-upstream/main --oneline -- $HK_PATHS"
    ;;
  
  status)
    echo "=== Upstream sync status ==="
    git remote -v | grep -E "vial|qmk|hk" || echo "No upstream remotes configured. Run: ./scripts/upstream-sync.sh check"
    ;;
    
  sync-drivers)
    echo "=== Syncing QMK sensor drivers ==="
    echo "Cherry-picking driver updates from qmk-upstream..."
    echo "Review each commit carefully before applying."
    git log HEAD..qmk-upstream/master --oneline -- $QMK_DRIVER_PATHS 2>/dev/null || echo "Add remote first: git remote add qmk-upstream $QMK_REMOTE"
    ;;
    
  sync-holykeebs)
    echo "=== Syncing HolyKeebs userspace ==="
    git log HEAD..hk-upstream/main --oneline -- users/holykeebs/ 2>/dev/null || echo "Add remote first: git remote add hk-upstream $HK_REMOTE"
    ;;
esac
