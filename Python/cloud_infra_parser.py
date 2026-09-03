import json

print("=== Enterprise Cloud Infrastructure API Processor ===")

# --- 1. SIMULATING AN AZURE REST API RESPONSE STREAM ---
# This raw JSON block matches the exact data format returned by the Azure ARM API
azure_raw_response = """
{
    "id": "/subscriptions/sub-1234/resourceGroups/Prod-RG/providers/Microsoft.Compute/virtualMachines/Web-Server-01",
    "name": "Web-Server-01",
    "type": "Microsoft.Compute/virtualMachines",
    "location": "eastus",
    "properties": {
        "vmId": "a8b9c1d2-3456",
        "hardwareProfile": {
            "vmSize": "Standard_D2s_v3"
        },
        "provisioningState": "Succeeded"
    }
}
"""

# Read Data & Parse JSON for Azure
azure_data = json.loads(azure_raw_response)

print("\n[Parsing Azure REST API Payload...]")
print(f"🔹 Target VM Name: {azure_data.get('name')}")
print(f"🔹 Deployment Data Center Region: {azure_data.get('location')}")
print(f"🔹 Hardware Scale Size: {azure_data['properties']['hardwareProfile']['vmSize']}")
print(f"🔹 Cloud Status: {azure_data['properties']['provisioningState']}")


# --- 2. SIMULATING AN OPENSTACK NOVA API RESPONSE STREAM ---
# Fixed: Closed the triple quotes at the bottom cleanly
openstack_raw_response = """
{
    "server": {
        "id": "9ef3-402a-92bc",
        "name": "Private-Database-Node",
        "status": "ACTIVE",
        "flavor": {
            "id": "m1.medium",
            "ram": 4096
        }
    }
}
"""

# Read Data & Parse JSON for OpenStack
openstack_data = json.loads(openstack_raw_response)

print("\n[Parsing OpenStack Nova API Payload...]")
print(f"🔸 Server Name: {openstack_data['server']['name']}")
print(f"🔸 Instance Status: {openstack_data['server']['status']}")
print(f"🔸 Flavor Size ID: {openstack_data['server']['flavor']['id']}")
print(f"🔸 Allocated RAM: {openstack_data['server']['flavor']['ram']} MB")