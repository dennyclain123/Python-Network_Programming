import paramiko
import time
import getpass

HOST = input("Enter target IP Address: ")
username = input('Enter username: ')
password = getpass.getpass()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=HOST, username=username, password=password)

print('Successful SSH Connection ',HOST)

remote_connection = ssh_client.invoke_shell()
remote_connection.send('conf t\n')
remote_connection.send("int g1/0 \n")
remote_connection.send("no shut \n")
remote_connection.send("ip address 30.0.0.1 255.255.255.0\n")
remote_connection.send("router ospf 1\n")
remote_connection.send("network 0.0.0.0 255.255.255.255 area 0\n")
remote_connection.send('end\n')
remote_connection.send('wr mem\n')
time.sleep(1)
print(remote_connection.recv(65535))

ssh_client.close