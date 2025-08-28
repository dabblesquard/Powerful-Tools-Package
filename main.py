import os
import sys
import time
import random

# === Colors (Matrix Green Theme + Mix) ===
GREEN = "\033[92m"
RESET = "\033[0m"
BOLD = "\033[1m"
YELLOW = "\033[1;33m"
CYAN = "\033[0;36m"
RED = "\033[0;31m"
PURPLE = "\033[0;35m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Typing Animation
def hacker_text(text, delay=0.02):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Loading Bar
def loading(msg="Loading"):
    for i in range(3):
        sys.stdout.write(f"\r{CYAN}{msg}{'.' * (i+1)}{RESET}")
        sys.stdout.flush()
        time.sleep(0.5)
    print()

# Banner
def banner():
    hacker_text(f"""{GREEN}{BOLD}
░██████╗████████╗██╗░░░██╗██████╗░██╗██████╗░░██████╗████████╗
██╔════╝╚══██╔══╝██║░░░██║██╔══██╗██║██╔══██╗██╔════╝╚══██╔══╝
╚█████╗░░░░██║░░░██║░░░██║██████╔╝██║██║░░██║╚█████╗░░░░██║░░░
░╚═══██╗░░░██║░░░██║░░░██║██╔═══╝░██║██║░░██║░╚═══██╗░░░██║░░░
██████╔╝░░░██║░░░╚██████╔╝██║░░░░░██║██████╔╝██████╔╝░░░██║░░░
╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░
        {RESET}{BOLD}\t ⚡ Stupid Script Tools Zone ⚡{RESET}
""", 0.002)

# Matrix Effect
def matrix_effect(duration=3):
    chars = "01#$%&@*"
    end_time = time.time() + duration
    while time.time() < end_time:
        line = "".join(random.choice(chars) for _ in range(60))
        print(GREEN + line + RESET)
        time.sleep(0.05)
    time.sleep(1)

# Hacker Quotes
quotes = [
    "“Hackers are the immune system of the internet.”",
    "“The quieter you become, the more you are able to hear.”",
    "“In a world of locked doors, the one with the key is king.”",
    "“Code is like humor. When you have to explain it, it’s bad.”",
]

# Login option
while True:
    clear()
    banner()
    hacker_text("\t ===== LOGIN PANEL =====\n", 0.01)
    user = input(f"{YELLOW}👤{BOLD} Username :{BOLD} {CYAN}")
    pas = input(f"{YELLOW}🔑{BOLD} Password : {BOLD}{CYAN}")

    if user == "ALAX" and pas == "1100":
        hacker_text(f"{GREEN}☑{BOLD} ACCESS GRANTED... WELCOME AGENT {user}{CYAN}", 0.03)
        time.sleep(1)
        clear()
        matrix_effect(4)
        hacker_text(f"{PURPLE}{random.choice(quotes)}{RESET}", 0.04)
        time.sleep(2)
        break
    else:
        hacker_text(f"{RED}❌{BOLD} ACCESS DENIED! Try Again...{RESET}", 0.03)
        time.sleep(1.5)

def tool(name):
    loading(f"▶ Starting {name}")
    hacker_text(f"{GREEN}✔ {name} Module Loaded Successfully!{RESET}", 0.03)

# === Menu Section ===
while True:
    clear()
    banner()
    hacker_text(f"""{GREEN}{BOLD}
[1] 📱 SMS Bombing
[2] 📧 MAIL Bombing
[3] 🌐 DDOS Attack
[4] 📍 IP Tracking
[5] 🗃️ Zip File Password Cracking
[6] 🔐 Encryption/Decryption Tools
[7] ⚙️ Basic Essential Package Installation
[0] ❌ Exit
{RESET}""", 0.01)

    choice = input(f"{YELLOW}{BOLD} Your Choice: {RESET}")

    if choice == "1":
        tool("SMS Bombing")
        os.system("python e-sms-bomb.py")  
        input(f"{CYAN}🔙 Press Enter to return to menu...{RESET}")

    elif choice == "2":
        tool("MAIL Bombing")
        os.system("python e-mail.py")
        input(f"{CYAN}🔙 Press Enter to return to menu...{RESET}")
    elif choice == "3":
        tool("DDOS Attack")
        os.system(" python enc_ddos.py")
        input(f"{CYAN}🔙 Press Enter to return to menu...{RESET}")
    elif choice == "4":
        tool("IP Tracking")
        os.system("python e-location.py")
        input(f"{CYAN}🔙 Press Enter to return to menu...{RESET}")
    elif choice == "5":
        tool("Zip File Cracking")
        os.system("python e-zip.py")
        input(f"{CYAN}🔙 Press Enter to return to menu...{RESET}")
    elif choice == "6":
        tool("Encryption/Decryption")
        os.system("python c-encryption.py")
        input(f"{CYAN}🔙 Press Enter to return to menu...{RESET}")
    elif choice == "7":
        tool("Essential Package Installation")
        os.system("python e-package.py")
        input(f"{CYAN}🔙 Press Enter to return to menu...{RESET}")
    elif choice == "0":
        # ASCII Banner for Exit
        banner_lines = [
            " ██████╗  ██████╗",
            "██╔════╝ ██╔═══██╗",
            "██║  ███╗██║   ██║",
            "██║   ██║██║   ██║",
            "╚██████╔╝╚██████╔╝",
            " ╚═════╝  ╚═════╝"
        ]
        for line in banner_lines:
            print(RED + BOLD + "─────────────── " + line + RESET)
            time.sleep(0.25)

        hacker_text(f"{RED}{BOLD}👋 Goodbye Agent {user}! Session Terminated...{RESET}", 0.03)
        time.sleep(2)
        break
    else:
        hacker_text(f"{RED}{BOLD}⚠ Invalid Choice! Try Again.{RESET}", 0.03)
        time.sleep(1.5)