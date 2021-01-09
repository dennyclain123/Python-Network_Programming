import json
from pyntc import ntc_device as NTC

R1 = {
    'host': 'R1',
    'device_type':'cisco_ios_ssh',
    'username': 'nituser',
    'password': 'nit',
}

switch1 = {
    'host': 'Switch1',
    'device_type': 'cisco_ios_ssh',
    'username': 'nituser',
    'password': 'nit',
}

all_devices = [R1,switch1]
for devices in all_devices:
    connect = NTC(**devices)
    connect.open()
    output = connect.running_config
    print (json.dumps(output, indent=4))
