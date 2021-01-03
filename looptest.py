import pyfiglet 
import getpass
import telnetlib
from itertools import count
import os
from termcolor import colored
from pyfiglet import figlet_format
print((colored(figlet_format("Code By NIT :D"), color="green")))

for i in count(0):
    try:
        print("####################################################")
        print("     1) Routing and assign interfaces (OSPF)       ")
        print("     2) Assign a single vlan to a switch        ")
        print("     3) Assign multiple vlan to a switch     ")
        print("     4) Assign a vlan interface for SVI      ")
        print("     5) Show the information of a router      ")
        print("     6) Show the information of a switch      ")
        print("     7) EXIT      ")
        print("###################################################")
        choice = int(input("Enter your choice: "))
        if(choice<=7):
            if(choice==1):
                os.system('python Routing.py')
            elif(choice==2):
                os.system('python single_vlan.py')
            elif(choice==3):
                os.system('python multi_ports.py')
            elif(choice==4):
                os.system('python SVI.py')
            elif(choice==5):
                os.system('python show_router.py')
            elif(choice==6):
                os.system('python show_switch.py')
            elif(choice==7):
                print((colored(figlet_format("BYE, HAVE FUN!!!"), color="green")))
                break
        else:
            print("Invaild")
    except ValueError:
        print("Input must be integar")  