#!/usr/bin/env bash

cd "$(dirname "$BASH_SOURCE")"

VENV=./venv
deactivate 2>/dev/null
unset PYTHONPATH

python3 -m venv $VENV
source $VENV/bin/activate

echo "## Create virtual environment $VENV"
python3 -m pip install --upgrade pip setuptools wheel

echo "## Install dependencies"
python3 -m pip install -r ./requirements.txt
