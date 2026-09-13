import json
from pathlib import Path
import requests

print("--- Running Cloud API and Website Health Audit ---")

# 1. Querying a valid testing sandbox endpoint
api_url = "https://typicode.com"
print(f"Querying cloud configuration metadata endpoint: {api_url}")

try:
    api_response = requests.get(api_url, timeout=10)
    if api_response.status_code == 200:
        print("✅ API Endpoint Connection: Successful (Status 200)")
        cloud_data = api_response.json()
        
        # Cleaned: Standard Python string tracking with no escape characters
        engineer_name = cloud_data.get('name')
        print(f"Retrieved Cloud Engineer Name: {engineer_name}")
    else:
        print(f"❌ API Failed. Status Code: {api_response.status_code}")
        cloud_data = {"error": f"Status code {api_response.status_code}"}
except Exception as e:
    print(f"❌ Connection failed: {e}")
    cloud_data = {"error": str(e)}

# 2. Auditing Website Health
github_url = "https://github.com"
print(f"\nAuditing Live Website Health: {github_url}")

try:
    web_response = requests.get(github_url, timeout=10)
    print(f"✅ Website Status Code: {web_response.status_code}")
except Exception as e:
    print(f"❌ Website check failed: {e}")

# 3. Export findings to logs directory
output_dir = Path("./logs")
output_dir.mkdir(exist_ok=True)
output_file = output_dir / "api_report.json"

with open(output_file, "w") as file:
    json.dump({"api_data": cloud_data}, file, indent=4)

print(f"\n✅ Audit complete! Logs saved to: {output_file.resolve()}")