# -Infrastructure-Watchdog

Infrastructure Watchdog is a proactive observability agent preventing system crashes by monitoring finite server resources. Built with Python for metric calculation (Disk/CPU) and Bash for log management and scheduling, it alerts users before thresholds are hit. This hybrid automation ensures service uptime through real-time alerts.

Problem Statement: Server resources (Disk/CPU) are finite. If they hit 100% capacity, services crash.

Problem Interpretation: We need Observability. A proactive agent that checks metrics against thresholds and alerts us before a crash.

Solution Planning:

Python: Calculates the math (Disk % and CPU Load) using standard libraries.

Bash: Schedules the run, manages the log file (append mode), and handles the final Alerting logic.

Usage: run the bash script via; ./run_monitor.sh

If permission is is encountered, resolve via; chmod a+x run_monitor.sh
