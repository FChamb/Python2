#!/bin/bash
# Setup the python virtual environment
# To activate the virtual environment (before running any python files)
#  > source code/.venv/bin/activate
python3 -m venv code/.venv && \
code/.venv/bin/pip install -r code/requirements.txt

