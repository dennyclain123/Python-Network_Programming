import json
from napalm import get_network_driver

devicelist = ['192.168.1.1','192.168.1.2',
           '192.168.1.3'
           ]

for ip_address in devicelist:
    print ("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    ios = driver(ip_address, 'nituser', 'nit')
    ios.open()
    ios.load_merge_candidate(filename='OSPF_R1.cfg')
    diffs = ios.compare_config()
    if len(diffs) > 0:
        print(diffs)
        ios.commit_config()
    else:
        print('No OSPF changes required for R1.')
        ios.discard_config()

    ios.load_merge_candidate(filename='OSPF_R2.cfg')
    diffs = ios.compare_config()
    if len(diffs) > 0:
        print(diffs)
        ios.commit_config()
    else:
        print('No OSPF changes required for R2.')
        ios.discard_config()

    ios.load_merge_candidate(filename='SVI_SW1.cfg')

    diffs = ios.compare_config()
    if len(diffs) > 0:
        print(diffs)
        ios.commit_config()
    else:
    	print('No SVI changes required for SW1.')
    	ios.discard_config()

    ios.close()
