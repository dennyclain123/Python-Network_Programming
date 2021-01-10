from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")
cmd = input("Enter command: ")
filtered = nr.filter(F(routing__contains="isis"))
result = filtered.run(task=send_command,command=cmd)
print_result(result)