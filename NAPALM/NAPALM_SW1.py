import json
import time
import sys
from napalm import get_network_driver

animation = "|/-\\"

for i in range(50):
    time.sleep(0.1)
    sys.stdout.write("\r" + "Connecting to 192.168.1.3...." + animation[i % len(animation)])
    sys.stdout.flush()
print("\nConnection Success!!!")

driver = get_network_driver('ios')
sw1 = driver('192.168.1.3', 'nituser', 'nit')
sw1.open()

ios_output = sw1.get_interfaces_ip()
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = sw1.get_arp_table()
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = sw1.get_mac_address_table()
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = sw1.get_vlans()
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = sw1.traceroute('192.168.1.1')
print (json.dumps(ios_output, sort_keys=True, indent=4))

sw1.close()