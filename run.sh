#!/bin/bash

# Enter Python virtual environment  
if [ ! -d ".venv" ]; then
    echo 'creating venv'
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
else
    echo 'booting venv'
    source .venv/bin/activate
fi

# Run project
# TODO - replace run example w project
cd example
python3 whoosh_example.py