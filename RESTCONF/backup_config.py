import requests

requests.packages.urllib3.disable_warnings()

HOST = "ios-xe-mgmt.cisco.com:9443"
USER = "developer"
PW = "C1sco12345"


url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native/"

headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json'
}

get_response = requests.get(url, headers=headers, auth=(USER, PW), verify=False)

with open("/home/mr_linux/Desktop/Py_Net scripts/RESTCONF/Outputs/" + HOST + "_running_config.txt", 'w') as file:
  file.write(get_response.text)
