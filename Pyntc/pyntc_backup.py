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
    run = connect.backup_running_config('running.cfg')
