import requests
import json
from pathlib import Path

print("--- Running Cloud API and Website Health Audit ---")
api_url = "https://typicode.com"
print(f"Querying cloud configuration metadata endpoint: {api_url}")

response = requests.get(api_url)
print(f"✅ Connection Status: {response.status_code}")
print(response.json())