import json
from ttp import ttp
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command

nr = InitNornir(config_file="config.yaml")
ttp_template = """
interface {{ inf }}
 ip address {{ ip }} {{ mask }}
 ip router {{ protocol }} 
 duplex {{ duplex_type }}
 speed {{ speed }}
 media-type {{ media_type }}
 negotiation {{ negotiation_type}}
"""

def text(task):
    r = task.run(netmiko_send_command, command_string="show run int g0/0") 
    datatoparse = r.result
    parser = ttp(data=datatoparse, template=ttp_template)
    parser.parse()
    json_result = json.loads(parser.result(format='json')[0])
    task.host["facts"] = json_result

result = nr.run(task=text)
import ipdb
ipdb.set_trace()
