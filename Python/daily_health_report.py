import os
import time
import json
from pathlib import Path
from datetime import datetime
import psutil
import schedule

print("=== ⏰ Daily Cloud Server Health Report Service Started ===")

def run_health_check():
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print(f"\n[🔄 Executing Scheduled Health Check at {current_time}]")
    
    # Gather hardware telemetry
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    # Structure payload
    report_data = {
        "timestamp": current_time,
        "cpu_usage_percent": cpu,
        "ram_usage_percent": ram,
        "disk_usage_percent": disk,
        "status": "HEALTHY" if cpu < 85 and ram < 90 else "WARNING"
    }
    
    # Save a separate report file for each daily run
    output_dir = Path("./logs/daily_reports")
    output_dir.mkdir(exist_ok=True, parents=True)
    report_file = output_dir / f"health_report_{current_time}.json"
    
    with open(report_file, "w", encoding="utf-8") as file:
        json.dump(report_data, file, indent=4)
        
    print(f"✅ Daily snapshot generated successfully: {report_file.name}")

# --- AUTOMATION SCHEDULE ENGINE ---
# For quick testing, we will configure it to run every 10 seconds.
# (To make it daily in production, you switch it to: schedule.every().day.at("08:00").do(run_health_check))
schedule.every(10).seconds.do(run_health_check)

print("Service is running in the background. Press Ctrl + C to stop.")

# Keep the background script engine alive to monitor intervals
while True:
    schedule.run_pending()
    time.sleep(1)
