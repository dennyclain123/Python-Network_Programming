from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
import getpass

nr = InitNornir(config_file="config.yaml")
routers_password = getpass.getpass(prompt="Routers Password: ")
switches_password = getpass.getpass(prompt="Switches Password: ")

nr.inventory.groups['routers'].password = routers_password
nr.inventory.groups['switches'].password = switches_password

def show_command(task):
    task.run(netmiko_send_command, command_string="show version")

result = nr.run(task=show_command)

print("Deploying Configurations...")
print_result(result)
