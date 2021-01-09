import paramiko
import time

ip_address = "192.168.1.2"
username = "nituser"
password = "nit"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print("Successful connection to", ip_address)

remote_connection = ssh_client.invoke_shell()

remote_connection.send("conf t\n")
remote_connection.send("int loop 0\n")
remote_connection.send("ip address 1.1.1.1 255.255.255.255\n")
remote_connection.send("router ospf 1\n")
remote_connection.send("network 0.0.0.0 255.255.255.255 area 0\n")

# creating vlans 2-20
for n in range(2,20):
    print("Creating Vlan" + str(n))
    remote_connection.send("vlan " + str(n) + "\n")
    remote_connection.send("name Python_VLAN_" + str(n) + "\n")
    # delay to create vlan successfully
    time.sleep(2) 

remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print(output)

ssh_client.close()