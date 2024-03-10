#!/bin/bash
# Use the first argument as the port number if given
port=${1:-8888}
source code/.venv/bin/activate && \
jupyter lab notebooks/census2011.ipynb --port "$port"
