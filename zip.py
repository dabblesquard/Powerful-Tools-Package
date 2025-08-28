

import zipfile

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
        

\033[1;33m=============================================
\033[1;32m Tools Name:Zip File Password Cracking Tools
Owner: Alax Mahmud
 Github: dabblesquard
 Facebook: Alax Hridoy
Use this tools only for educational purposes
\033[1;33m=============================================\033[0m
""")
print("""\033[1;36m
-------------------------------------------------
""")
print("\tZip File Password Cracking Tools")
print("""
-------------------------------------------------\033[0m
""")


RED="033[1;31m"
YELLO="\033[1;33m"
GREEN="\033[1;32m"

z=input(f"{YELLO}Your Zip File Path:{GREEN}")
print("\n")
try:
	zip=zipfile.ZipFile(z)
except FileNotFoundError:
	print(f"{RED}File Not Found,Try Again.")
	exit()
except zipfile.BadZipFile:
	print(f"{RED}Wrong File,Enter Valid Zipfile Path ")	
	exit()

#password input
pw=input(f"{YELLO}Enter Your Password List Path: {GREEN}")

print("""\033[0;36m
*************************************************
""")


ab=("\t\033[1;32m       Password Checking...\n\033[0m")

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)

print("""\033[0;36m
*************************************************\033[0m
""")
time.sleep(2)

try:
	file=open(pw,"r")
except FileNotFoundError:
	print(f"{RED}Wrong,Enter Right Password File Path.")
	exit()

found= False

for password in file:
	password=password.strip()
	try:
		zip.extractall(pwd=bytes(password,"utf-8"))
		print(f"{GREEN}Match Found,Password is: "+password)
		found= True
		break
	except:
		print("\033[1;31mWrong Password "+password)
		
if not found:
	print("\033[1;31mNo Password Match")