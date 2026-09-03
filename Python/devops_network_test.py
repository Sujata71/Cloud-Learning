import requests

print("--- Running Fresh Network Module Check ---")

# Targeting an un-cached public API domain name
api_url = "https://reqres.in"
print(f"Connecting to: {api_url}")

response = requests.get(api_url)
print(f"✅ Success! Connection Status: {response.status_code}")
print(response.json())