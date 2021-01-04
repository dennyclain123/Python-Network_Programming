import json
from napalm import get_network_driver
driver = get_network_driver('ios')
R2 = driver('192.168.1.2', 'nituser', 'nit')
R2.open()

ios_output = R2.get_interfaces_ip()
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = R2.get_arp_table()
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = R2.get_route_to()
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = R2.ping('192.168.1.1')
print (json.dumps(ios_output, sort_keys=True, indent=4))

R2.close()