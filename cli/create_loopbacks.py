from netmiko import ConnectHandler
import sys

sys.path.append("..")
from device_info import ios_xe1 as device

config = []
for n in range(201, 221):
    config += [
        f"interface Loopback{n}",
        f"description Demo loopback {n}",
        f"ip address 10.{n}.{n}.1 255.255.255.255",
        "no shutdown",
    ]

with ConnectHandler(device_type="cisco_ios", ip=device["address"], port=device["ssh_port"],
                    username=device["username"], password=device["password"]) as ch:
    print(ch.send_config_set(config))