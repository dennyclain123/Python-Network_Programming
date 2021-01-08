import json
import time
import sys
from napalm import get_network_driver

animation = "|/-\\"

for i in range(50):
    time.sleep(0.1)
    sys.stdout.write("\r" + "Connecting to 192.168.1.1...." + animation[i % len(animation)])
    sys.stdout.flush()
print("\nConnection Success!!!")

driver = get_network_driver('ios')
R1 = driver('192.168.1.1', 'nituser', 'nit')
R1.open()

ios_output = R1.get_interfaces_ip()
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = R1.get_users()
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = R1.ping('192.168.1.2')
print (json.dumps(ios_output, sort_keys=True, indent=4))

R1.close()
