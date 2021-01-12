from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command

nr = InitNornir(config_file="config.yaml")
def show_command(task):
    task.run(netmiko_send_command, command_string="show int description", use_genie = True) 
#You need to download ntc_templates from git hub, link is in the txt file

result = nr.run(task=show_command)
print_result(result)