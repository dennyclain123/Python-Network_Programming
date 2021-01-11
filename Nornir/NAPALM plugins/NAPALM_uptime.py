from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

nr = InitNornir(config_file="config.yaml")
def get_info(task):
    r = task.run(task=napalm_get,getters=["get_facts"])
    task.host["facts"] = r.result
    facts_data = task.host["facts"]
    uptime = facts_data["get_facts"]["uptime"]
    if(uptime<=600):
        print(f"FAIL:{task.host}'s backup power did not kick in")

result = nr.run(task=get_info)
print_result(result)