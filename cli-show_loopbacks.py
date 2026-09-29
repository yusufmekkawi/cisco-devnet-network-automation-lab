from netmiko import ConnectHandler
import sys

sys.path.append("..")
from device_info import ios_xe1 as device

with ConnectHandler(device_type="cisco_ios", ip=device["address"], port=device["ssh_port"],
                    username=device["username"], password=device["password"]) as ch:
    print(ch.send_command("show ip interface brief | include Loopback"))