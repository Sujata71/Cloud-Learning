import os
import subprocess
import json
from pathlib import Path
from datetime import datetime
import psutil

print("=== 🖥️ Automated Cloud Server Health Monitor ===")

# 1. Gather Chronological Telemetry Timestamp
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 2. Extract Hardware Resource Metrics using psutil
cpu_usage = psutil.cpu_percent(interval=1)
ram_metrics = psutil.virtual_memory()
disk_metrics = psutil.disk_usage('/')

print(f"Timestamp: {current_time}")
print(f"📊 CPU Utilization: {cpu_usage}%")
print(f"📊 RAM Utilization: {ram_metrics.percent}% (Used: {ram_metrics.used // (1024**2)}MB / Total: {ram_metrics.total // (1024**2)}MB)")
print(f"📊 Disk Utilization: {disk_metrics.percent}% (Used: {disk_metrics.used // (1024**3)}GB / Total: {disk_metrics.total // (1024**3)}GB)")

# 3. Execute Network Connectivity Ping Check via Subprocess
print("📡 Auditing core network gateway connectivity...")
# Using 1 test packet (-n 1 for Windows, -c 1 for Mac/Linux)
ping_flag = "-n" if os.name == "nt" else "-c"
# Ping Google Public DNS to verify external internet accessibility
ping_proc = subprocess.run(["ping", ping_flag, "1", "8.8.8.8"], capture_output=True, text=True)

network_status = "Healthy / Connected" if ping_proc.returncode == 0 else "Degraded / Disconnected"
print(f"📡 Network Interface Status: {network_status}")

# 4. Compile and Structure the System Health Metrics Payload
health_report = {
    "report_generated_at": current_time,
    "system_metrics": {
        "cpu_percentage": cpu_usage,
        "ram_percentage": ram_metrics.percent,
        "disk_percentage": disk_metrics.percent
    },
    "network_telemetry": {
        "gateway_status": network_status
    }
}

# 5. Create the Logs Directory Structure and Save the JSON Report
output_dir = Path("./logs")
output_dir.mkdir(exist_ok=True)
report_file_path = output_dir / "health_report.json"

with open(report_file_path, "w", encoding="utf-8") as file:
    json.dump(health_report, file, indent=4)

print(f"\n✅ Health check complete! Consolidated metrics saved to: {report_file_path.resolve()}")