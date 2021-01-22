from jinja2 import Environment, FileSystemLoader
import yaml
from pprint import pprint as pp
from netmiko import Netmiko

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("ebgp_neighbor_template.j2")


with open("ospf_template_r1.yaml") as r4:
    r1_ospf = yaml.load(r1)
    print(r1_ospf)

with open("ospf_template_r1.yaml") as r5:
    r2_ospf = yaml.load(r2)
    print(r2_ospf)



output_r1 = template.render(ospf=r1_ospf)
output_r2 = template.render(ospf=r2_ospf)


my_device_r1 = {
    "host": "192.168.122.100",
    "username": "nituser",
    "password": "nit",
    "device_type": "cisco_ios"
}

my_device_r2 = {
    "host": "192.168.122.200",
    "username": "nituser",
    "password": "nit",
    "device_type": "cisco_ios"
}

net_conn_r1 = Netmiko(**my_device_r1)

print(net_conn_r1.find_prompt())

net_conn_r2 = Netmiko(**my_device_r2)

pp(net_conn_r2.send_config_set(output_r2))

