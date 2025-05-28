#!/bin/bash
# Setup Python virtual environment and install dependencies, including flake8 for linting

set -e

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

echo "Virtual environment setup complete. To activate, run: source venv/bin/activate"
