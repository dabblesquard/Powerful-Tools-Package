# ==============================================
# Python Encryption Tool (Marshal Based)
# With Custom Logo (by Alax)
# ==============================================

import marshal
import os
import sys
import time

# === Colors ===
GREEN = "\033[92m"
RESET = "\033[0m"
BOLD = "\033[1m"
YELLOW = "\033[1;33m"
CYAN = "\033[0;36m"
RED = "\033[1;31m"
BLUE = "\033[1;34m"

# === Your Logo Function ===
#def logo():
#    os.system("clear" if os.name == "posix" else "cls")
#    print("\n\n\n\n")

#    ab = "           \033[1;33mSystem loading...."
#    for c in ab:
#        sys.stdout.write(c)
#        sys.stdout.flush()
#        time.sleep(0.05)

#    print("\n\n\n\n")
#    os.system("clear" if os.name == "posix" else "cls")
#    time.sleep(1)

#    print("\n\n")
#    ab = "         \033[1;32mSuccessfully Loaded.!\n"
#    for c in ab:
#        sys.stdout.write(c)
#        sys.stdout.flush()
#        time.sleep(0.05)

#    name = input("         \033[1;34mName: ")
#    ab = "         \033[1;31mHey " + name + ", Be Ethical.."
#    for c in ab:
#        sys.stdout.write(c)
#        sys.stdout.flush()
#        time.sleep(0.05)

#    os.system("clear" if os.name == "posix" else "cls")

#    disclaimer = """
#\033[1;33m
#\t      ⚠️  DISCLAIMER
#\033[1;31m
# This tool is intended for EDUCATIONAL 
# purposes only.

# Unauthorized use of this tool for attacking   
# targets without prior mutual consent is 
# ILLEGAL.

# The creator is NOT responsible for any 
# misuse or damage caused by this tool.
#\033[0m
#"""
#    print(disclaimer)
#    time.sleep(3)
#    os.system("clear" if os.name == "posix" else "cls")

#    print(""" \033[1;31m
#   _____  .__                 
#  /  _  \\ |  | _____  ___  ___
# /  /_\\  \\|  | \\__  \\ \\  \\/  /
#/    |    \\  |__/ __ \\_>    < 
#\\____|__  /____(____  /__/\\_ \\
#        \\/          \\/      \\/

#\033[1;33m========================================
#\033[1;32m Tools Name: Encryption/ Decryption 
#Owner : Alax Mahmud
#Github: dabblesquard
# Use this tool only for educational purposes
#\033[1;33m========================================            
#\033[0m
#""")


# === Encrypt Function ===
def encrypt(inpu, outp):
    try:
        with open(inpu, "r", encoding="utf-8") as f:
            code = f.read()

        comp = compile(code, "Encrypted", "exec")
        com = marshal.dumps(comp)

        with open(outp, "w", encoding="utf-8") as new:
            new.write("import marshal\n")
            new.write(f"exec(marshal.loads({repr(com)}))")

        print(f"\n{GREEN}[✔] Successfully Encrypted!{RESET}")
        print(f"{CYAN}[+] Input File : {inpu}{RESET}")
        print(f"{CYAN}[+] Output File: {outp}{RESET}")

    except FileNotFoundError:
        print(f"{RED}[✘] File not found! Please check path.{RESET}")
    except Exception as e:
        print(f"{RED}[✘] Error: {e}{RESET}")


# === Main Program ===
if __name__ == "__main__":
    #logo()
    try:
        inpu = input(f"{YELLOW}[*] Enter Your File Path : {RESET}")
        outp = input(f"{YELLOW}[*] Enter File Output Name: {RESET}")
        print(f"\n{CYAN}[*] Encrypting... Please wait...{RESET}")
        time.sleep(1.5)
        encrypt(inpu, outp)
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Process Cancelled by User.{RESET}")
        sys.exit()