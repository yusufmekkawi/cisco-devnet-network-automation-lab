import os
import requests

host = os.environ["DEVNET_HOST"]
user = os.environ["DEVNET_USER"]
password = os.environ["DEVNET_PASS"]

url = f"https://{host}/restconf/data/ietf-interfaces:interfaces"
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

response = requests.get(url, auth=(user, password), headers=headers, verify=False)
response.raise_for_status()

data = response.json()
for iface in data["ietf-interfaces:interfaces"]["interface"]:
    print(iface["name"], "-", "enabled" if iface["enabled"] else "disabled")