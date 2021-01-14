import requests
import sys
from pprint import pprint as pp

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()


HOST = 'ios-xe-mgmt.cisco.com:9443'
USER = 'developer'
PASS = 'C1sco12345'



def main():
    """Main method that retrieves the Interface details from Cat9300 via RESTCONF."""
    url = "https://{h}/restconf/data/ietf-interfaces:interfaces".format(h=HOST)
    print(url)
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    response = requests.get(url, auth=(USER, PASS),
                            headers=headers, verify=False).json()
    pp(response)

if __name__ == '__main__':
    sys.exit(main())
