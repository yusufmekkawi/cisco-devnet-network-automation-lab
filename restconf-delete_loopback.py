import os
import requests

host = os.environ["DEVNET_HOST"]
user = os.environ["DEVNET_USER"]
password = os.environ["DEVNET_PASS"]

url = f"https://{host}/restconf/data/ietf-interfaces:interfaces/interface=Loopback100"
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

response = requests.delete(url, auth=(user, password), headers=headers, verify=False)
print(response.status_code)