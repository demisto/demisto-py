#!/bin/bash

# exit on errors
set -e

# Script to run extra verifications after tox build completes

# Verify that code-gen.sh doesn't generate a diff
bash -x ./gen-code.sh 
DIFF_OUT=$(git diff --stat)

echo "========================================="
echo ""

if [[ -n "$DIFF_OUT" ]]; then
    echo "./gen-code.sh modified the source code. gen-code.sh should not modify the source code. If needed, run gen-code.sh before committing."
    echo "git diff --stat output:"
    echo "$DIFF_OUT"
    exit 1
fi

echo "All is good"