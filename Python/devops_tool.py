import os
import subprocess
import json
from pathlib import Path
from datetime import datetime

print("--- Running DevOps System Check ---")

# 1. [datetime] Get current system timestamp for logs
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Timestamp: {current_time}")

# 2. [os] Gather system environment details
username = os.getlogin() if hasattr(os, 'getlogin') else "Cloud-Engineer"
current_pid = os.getpid()
print(f"User: {username} | Python Process ID: {current_pid}")

# 3. [subprocess] Check connection to a public DNS server (Ping)
print("Testing network connectivity via Subprocess...")
# Using 1 packet (-c 1 for Mac/Linux, -n 1 for Windows)
ping_flag = "-n" if os.name == "nt" else "-c"
ping_response = subprocess.run(["ping", ping_flag, "1", "8.8.8.8"], capture_output=True, text=True)

network_status = "Connected" if ping_response.returncode == 0 else "Disconnected"
print(f"Network Status: {network_status}")

# 4. [pathlib] Setup a backup/log directory safely
output_dir = Path("./logs")
output_dir.mkdir(exist_ok=True) # Creates 'logs' folder if it doesn't exist
report_file = output_dir / "system_report.json"

# 5. [json] Structure the data and export it as a cloud configuration file
report_data = {
    "scan_time": current_time,
    "operator": username,
    "network": network_status,
    "os_type": os.name
}

with open(report_file, "w") as file:
    json.dump(report_data, file, indent=4)

print(f"✅ Success! Report exported to: {report_file.resolve()}")