#!/bin/bash
# Directly install flake8 into the user site-packages to help lint in restrictive environments

python3 -m pip install --user flake8
echo "flake8 installed to user environment."
