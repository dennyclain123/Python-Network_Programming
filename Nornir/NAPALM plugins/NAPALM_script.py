from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

nr = InitNornir(config_file="config.yaml")
def get_info(task):
    task.run(task=napalm_get,getters=["get_interfaces_ip"])
    task.run(task=napalm_get,getters=["get_facts"])

result = nr.run(task=get_info)
print_result(result)