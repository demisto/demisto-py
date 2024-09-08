#!/bin/bash

# exit on errors
set -e

# Script to run extra verifications

# Verify that code-gen.sh doesn't generate a diff
bash ./gen-code.sh  # Removed the '-x' for verbosity in CI
# we diff only the code
DIFF_OUT=$(git diff -- demisto_client)

echo "========================================="
echo ""

if [[ -n "$DIFF_OUT" ]]; then
    echo "./gen-code.sh modified the source code. gen-code.sh should not modify the source code. If needed, run gen-code.sh before committing."
    echo "git diff -- demisto_client output:"
    echo "$DIFF_OUT"
    exit 1
fi

echo "All is good"