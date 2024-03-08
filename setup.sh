#!/bin/bash
# Setup the python virtual environment
# To activate the virtual environment (before running any python files)
python3 -m venv code/.venv && \
code/.venv/bin/pip install -r code/requirements.txt && \
echo "====================================" && \
echo "Virtual environment successfully created" && \
echo "Remember to activate with:" && \
echo "> source code/.venv/bin/activate"
