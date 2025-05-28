#!/bin/bash
cd /home/kavia/workspace/code-generation/eventease-22648-c4a6b9ee/eventease_backend
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

