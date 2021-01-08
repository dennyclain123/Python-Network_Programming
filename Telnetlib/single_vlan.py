import getpass
import telnetlib

HOST = input("Enter your target device IP Address: ")
user = input("Enter your telnet username: ")
password = getpass.getpass()
print ("Note: This script only work for single vlans")
vlan = int(input("which number of vlan you want to add: "))
tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")


tn.write(b"conf t\n")
tn.write(b"vlan " + str(vlan).encode('ascii') + b"\n")
tn.write(b"name NIT_VLAN_" + str(vlan).encode('ascii') + b"\n")
tn.write(b"int e0/0\n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan " + str(vlan).encode('ascii') + b"\n")
tn.write(b"int e0/1\n")
tn.write(b"switchport trunk encapsulation dot1q\n")
tn.write(b"switchport mode trunk\n")
tn.write(b"end\n")
tn.write(b"show vlan br\n")
tn.write(b"show int status\n")
tn.write(b"wr mem\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))