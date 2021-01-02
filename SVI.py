import getpass
import telnetlib

HOST = input("Enter your target device IP Address: ")
user = input("Enter your telnet username: ")
password = getpass.getpass()
print ("Note: Vlans are start with 2")
start = int(input("Enter your VLAN start number: "))
end = int(input("Enter your vlan end number: "))
tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")

for n in range (start,end):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name NIT_VLAN_" + str(n).encode('ascii') + b"\n")

tn.write(b"int vlan 2\n")
tn.write(b"no shut\n")
tn.write(b"ip add 10.0.0.1 255.255.255.0\n")
tn.write(b"int vlan 3\n")
tn.write(b"no shut\n")
tn.write(b"ip add 20.0.0.1 255.255.255.0\n")
tn.write(b"int vlan 4\n")
tn.write(b"no shut\n")
tn.write(b"ip add 30.0.0.1 255.255.255.0\n")
tn.write(b"int e0/0\n")
tn.write(b"switchport trunk encapsulation dot1q\n")
tn.write(b"switchport mode trunk\n")
tn.write(b"end\n")
tn.write(b"wr mem\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
