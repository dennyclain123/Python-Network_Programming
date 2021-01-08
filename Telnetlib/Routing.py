import getpass
import telnetlib

HOST = input("Enter your target IP Address: ")
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b"int g1/0\n")
tn.write(b"ip address 10.0.0.1 255.255.255.0\n")
tn.write(b"int loop 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 192.168.1.0 0.0.0.255 area 0\n")
tn.write(b"network 10.0.0.0 0.0.0.255 area 0\n")
tn.write(b"network 1.1.1.1 255.255.255.255 area 0\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
