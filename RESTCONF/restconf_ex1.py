# This is an example of restconf script hitting cisco devnet lab device (CSR1000V)

import requests

# disable warnings from SSL/TLS certificates
r = requests.packages.urllib3.disable_warnings()

# login creds
HOST  = "ios-xe-mgmt.cisco.com:9443"
USER = 'developer'
PASS = 'C1sco12345'

# create a main() method
def main():
    """Main method that retrieves info from the device using RESTCONF."""
    url = "https://{h}/restconf/data?fields=ietf-yang-library:modules-state/module".format(h=HOST)


    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    # this statement performs a GET on the specified url
    response = requests.get(url, auth=(USER, PASS),
                            headers=headers, verify=False)

    # print the json that is returned
    print(response.text)

if __name__ == '__main__':
    main()
