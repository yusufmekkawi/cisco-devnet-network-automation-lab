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
payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback100",
        "description": "Created via RESTCONF (Python)",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [{"ip": "10.100.100.1", "netmask": "255.255.255.255"}]
        },
    }
}

response = requests.post(url, auth=(user, password), headers=headers, json=payload, verify=False)
print(response.status_code)
if response.status_code not in (201, 409):
    print(response.text)