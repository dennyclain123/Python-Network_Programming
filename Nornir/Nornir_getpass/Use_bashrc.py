from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
import getpass
import sys
import os

nr = InitNornir(config_file="config.yaml")

nr.inventory.defaults.username = os.environ["NIT_USER"]
nr.inventory.defaults.password = os.environ["NIT_PASS"]

def show_command(task):
    task.run(netmiko_send_command, command_string="show ip int br")

result = nr.run(task=show_command)

print("Deploying Configurations...")
print_result(result)
