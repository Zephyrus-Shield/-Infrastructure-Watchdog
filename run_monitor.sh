#!/bin/bash

# --- BLOCK 1: CONFIGURATION ---
PYTHON_SCRIPT="monitor.py"
LOG_FILE="system_health.log"

# --- BLOCK 2: EXECUTION & LOGGING ---
python3 "$PYTHON_SCRIPT" >> "$LOG_FILE" 2>&1

# --- BLOCK 3: ALERT SYSTEM ---
if [ $? -ne 0 ]; then
    echo "WARNING: System usage is critical! Check $LOG_FILE"
else
    echo "System Healthy."
fi