import paramiko
import time
import getpass

HOST = input("Enter target IP Address: ")
username = input('Enter username: ')
password = getpass.getpass()
start = int(input("Enter a start number of VLAN: "))
end = int(input("Enter a end number of VLAN: "))

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=HOST, username=username, password=password)

print('Successful SSH Connection ',HOST)

remote_connection = ssh_client.invoke_shell()

remote_connection.send('conf t\n')

for n in range (start,end):
    print("Creating Vlan" + str(n))
    remote_connection.send('vlan ' + str (n) + '\n')
    remote_connection.send('name NIT_VLAN_' + str (n) + '\n')
    time.sleep(0.5)

remote_connection.send("int g0/1 \n")
remote_connection.send("switchport mode access\n")
remote_connection.send("switchport access vlan 2\n")
remote_connection.send("int g0/2 \n")
remote_connection.send("switchport mode access\n")
remote_connection.send("switchport access vlan 3\n")
remote_connection.send("int vlan 2 \n")
remote_connection.send("no shut \n")
remote_connection.send("ip address 10.0.0.1 255.255.255.0\n")
remote_connection.send("int vlan 3 \n")
remote_connection.send("no shut \n")
remote_connection.send("ip address 20.0.0.1 255.255.255.0\n")
remote_connection.send("router ospf 1\n")
remote_connection.send("network 0.0.0.0 255.255.255.255 area 0\n")
remote_connection.send('end\n')
remote_connection.send('wr mem\n')
time.sleep(1)
print(remote_connection.recv(65535))

ssh_client.close