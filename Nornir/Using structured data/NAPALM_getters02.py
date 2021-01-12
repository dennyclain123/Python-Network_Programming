from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from rich import print

nr = InitNornir(config_file="config.yaml")
def get_info(task):
    r = task.run(task=napalm_get,getters=["get_facts"])
    task.host["facts"] = r.result
    facts_data = task.host["facts"]
    uptime = facts_data["get_facts"]["uptime"]
    model = facts_data["get_facts"]["vendor"]
    int_list = facts_data["get_facts"]["interface_list"]
    num_int = len(int_list)
    if(model == "Cisco"):
        print(f"Device {task.host} is running [green] {model}[/green],"
        f"has {num_int} interfaces, and has been up for {uptime} seconds")
    if(model == "Juniper"):
        print(f"Device {task.host} is running [blue] {model}[/blue],"
        f"has {num_int} interfaces, and has been up for {uptime} seconds") 
    if(model == "Arista"):
        print(f"Device {task.host} is running [yellow] {model}[/yellow],"
        f"has {num_int} interfaces, and has been up for {uptime} seconds")  

result = nr.run(task=get_info)