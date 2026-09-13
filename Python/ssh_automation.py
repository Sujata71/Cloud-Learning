import csv
import json
from pathlib import Path
import paramiko

print("=== 🚀 Automated Multi-Server SSH Command Runner ===")

csv_file_path = "servers.csv"
command_to_run = "uname -a"  # Default Linux command to check system kernel status

# 1. Read Server Details using Python's built-in CSV module
servers = []
try:
    with open(csv_file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            servers.append(row)
    print(f"📦 Inventory Loaded: Detected {len(servers)} servers from CSV record.")
except FileNotFoundError:
    print(f"❌ Error: Could not locate inventory tracking file at {csv_file_path}")
    exit(1)

# Ensure our clean output logs directory folder structure exists
output_dir = Path("./logs")
output_dir.mkdir(exist_ok=True)
output_log_file = output_dir / "ssh_output.txt"

# Clear out any stale history logs from previous scripting sessions
with open(output_log_file, "w", encoding="utf-8") as clear_log:
    clear_log.write(f"Multi-Server SSH Orchestration Log — Target Command: '{command_to_run}'\n")
    clear_log.write("="*60 + "\n\n")

# 2. Iterate Through All 20 Loaded Servers and Execute via Paramiko SSH
for index, server in enumerate(servers, start=1):
    ip = server["ip"]
    username = server["username"]
    password = server["password"]

    print(f"[{index}/20] Connecting to node {ip} as user '{username}'...")

    # Initialize the Paramiko secure shell network client connection engine
    ssh = paramiko.SSHClient()
    
    # Automatically accept unknown remote host keys (Crucial step for hands-off automation)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Establish connection (Using a 3-second timeout so it won't hang your machine)
        ssh.connect(hostname=ip, username=username, password=password, timeout=3)
        
        # 3. Run Command on the Remote Operating System
        stdin, stdout, stderr = ssh.exec_command(command_to_run)
        
        # Capture raw return telemetry streams
        output = stdout.read().decode("utf-8").strip()
        error = stderr.read().decode("utf-8").strip()

        # 4. Format the Data Log
        log_entry = f"🌐 NODAL IP: {ip}\n🟢 STDOUT OUTPUT:\n{output if output else 'Command executed with blank return data.'}\n"
        if error:
            log_entry += f"🔴 STDERR ERROR:\n{error}\n"

    except Exception as e:
        # Because these are private placeholder IPs, they will log network connection timeouts.
        # This clean exception block is exactly how real engineers catch dead cloud infrastructure nodes!
        log_entry = f"🌐 NODAL IP: {ip}\n❌ SSH NETWORK CONNECTION FAILURE: {e}\n"
        print(f"   ⚠️ Warning: Server target {ip} is currently unreachable.")
    
    finally:
        ssh.close()

    # 5. Append and Save the Session Data to our consolidated report
    with open(output_log_file, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry + "\n" + "-"*50 + "\n\n")

print(f"\n✅ Orchestration completed! Consolidated server reports saved to: {output_log_file.resolve()}")