from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
import getpass

nr = InitNornir(config_file="config.yaml")
password = getpass.getpass()
nr.inventory.defaults.password = password
def show_command(task):
    task.run(netmiko_send_command, command_string="show ip int br")

result = nr.run(task=show_command)

print("Deploying Configurations...")
print_result(result)
