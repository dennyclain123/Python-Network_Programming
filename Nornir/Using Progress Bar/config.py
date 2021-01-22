from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config
from nornir_netmiko import netmiko_send_command
from tqdm import tqdm

nr = InitNornir(config_file="config.yaml")
def config_demo(task,progress_bar):
    task.run(netmiko_send_config, config_file="config_file.txt")
    progress_bar.update()
    task.run(netmiko_send_command, command_string="sh version | sec Cisco IOS")
    progress_bar.update()

with tqdm(total=len(nr.inventory.hosts)) as progress_bar:
    result = nr.run(task=config_demo, progress_bar=progress_bar)

print_result(result)