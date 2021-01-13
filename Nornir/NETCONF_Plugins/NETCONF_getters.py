from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from nornir_scrapli.tasks import (
    netconf_get_config,
)
from xml.dom import minidom

nr = InitNornir(config_file="/home/mr_linux/Desktop/Py_Net scripts/Nornir/NETCONF_Plugins/config.yaml")
def getters(task):
    result = task.run(task=netconf_get_config,source="running").result
    formal = minidom.parseString(result).toprettyxml()
    print(formal)

output = nr.run(task=getters)
print_result(output)