from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_configure

nr = InitNornir(config_file="config.yaml", dry_run=True)
def config_demo(task):
    task.run(napalm_configure, filename="config_file.txt")

result = nr.run(task=config_demo)
print_result(result)