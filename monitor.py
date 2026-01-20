import shutil, os, sys, datetime

# --- BLOCK 1: SETUP ---
DISK_THRESHOLD = 90.0
LOAD_THRESHOLD = 2.0

# --- BLOCK 2: DIAGNOSTIC FUNCTIONS ---
def check_disk():
    total, used, free = shutil.disk_usage("/")
    return (used / total) * 100

def check_cpu():
    load_1min, _, _ = os.getloadavg()
    return load_1min

# --- BLOCK 3: MAIN LOGIC ---
if __name__ == "__main__":
    disk = check_disk()
    cpu = check_cpu()
    now = datetime.datetime.now()
    msg = f"[{now}] Disk: {disk:.2f}% | CPU: {cpu}"

    # --- BLOCK 4: DECISION GATE ---
    if disk > DISK_THRESHOLD or cpu > LOAD_THRESHOLD:
        print(f"CRITICAL ALERT: {msg}")
        sys.exit(1)
    else:
        print(f"HEALTHY: {msg}")
        sys.exit(0)