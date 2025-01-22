#!/bin/bash

git clone https://github.com/ShivangSrivastava/pylings.git

cd pylings

if ! command -v uv &> /dev/null
then
    echo "uv is not installed. Installing..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

uv run main.py --help
