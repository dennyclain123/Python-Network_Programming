import json
from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'nituser',
    'password': 'nit',
}

R2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.2',
    'username': 'nituser',
    'password': 'nit',
}

switch1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.3',
    'username': 'nituser',
    'password': 'nit',
}


with open('R1') as f:
    lines = f.read().splitlines()
print (json.dumps(lines, indent=4))


all_devices = [R1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)


with open('R2') as f:
    lines = f.read().splitlines()
print (json.dumps(lines, indent=4))


all_devices = [R2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

with open('switch1') as f:
    lines = f.read().splitlines()
print (json.dumps(lines, indent=4))


all_devices = [switch1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)