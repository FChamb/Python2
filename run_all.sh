#!/bin/bash
FILE="data/census2011.csv"
CLEAN_FILE="data/census2011-clean.csv"

echo "== RUNNING run_consistency.sh ==" && \
./run_consistency.sh "$FILE" && \
echo "== RUNNING run_summary.sh ==" && \
./run_summary.sh "$CLEAN_FILE" && \
echo "== RUNNING run_queries.sh ==" && \
./run_queries.sh && \
echo "== RUNNING run_plots.sh ==" && \
./run_plots.sh "$CLEAN_FILE" && \
echo "== RUNNING run_performance.sh ==" && \
./run_performance.sh
