#Ip to location 

import requests 
import time

# Logo 

import os 
import sys 


os.system("clear")

print("\n\n\n\n")

ab="           \033[1;33mSystem loding...."

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)

print("\n\n\n\n")


os.system("clear")

time.sleep(1)
print("\n\n")

ab="         \033[1;32mSuccessfully Loaded.!\n"

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)
name=input("         \033[1;34mName:")

ab="         \033[1;31mHey "+name+", Be Ethical.."

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)

print("\n\n")


time.sleep(2)

os.system("clear")

print(""" \033[1;31m


   _____  .__                 
  /  _  \\ |  | _____  ___  ___
 /  /_\\  \\|  | \\__  \\ \\  \\/  /
/    |    \\  |__/ __ \\_>    < 
\\____|__  /____(____  /__/\\_ \\
        \\/          \\/      \\/
        

\033[1;33m==============================================
\033[1;32mTools Name: IP Locaton Tracker
Owner: Alax Mahmud
Github: dabblesquard
Use this tools only for educational purposes
\033[1;33m==============================================\033[0m
""")

print("""\033[1;36m
----------------------------------------------
""")
print("\t     IP To Location Tools")
print("""
----------------------------------------------\033[0m
""")

YELLO="\033[1;33m"
GREEN="\033[1;32m"
CYAN= "\033[1;36m"
RED="\033[1;31m"

ip=input(f"{YELLO}Enter Your Terget IP: {RED}")
print("""
**********************************************
""")


ab=("\t\033[1;32m    Information Gathering..\n\033[0m")

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)

time.sleep(0.2)
print("""\033[1;31m
**********************************************\033[0m
""")
response=requests.get("http://ip-api.com/json/"+ip)


txt=response.json()

#Use deictionary
print(f"{CYAN}Country			:{GREEN} {txt['country']}")
print(f"{CYAN}Country Code		:{GREEN} {txt['countryCode']}")
print(f"{CYAN}Region Name		:{GREEN} {txt['regionName']}")
print(f"{CYAN}City			:{GREEN} {txt['city']}")
print(f"{CYAN}Zip Code		:{GREEN} {txt['zip']}")
print(f"{CYAN}ISP Provider		:{GREEN} {txt['isp']}")
print(f"{CYAN}Organization		:{GREEN} {txt['org']}")
print(f"{CYAN}Query		 	:{GREEN} {txt['query']}")


print(f"{CYAN}Real Time Location	:{GREEN} https://www.google.com/maps/search/?api=1&query={txt['lat']},{txt['lon']}")

