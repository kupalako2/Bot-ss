
import os
print("Setup Bot Telegram By @tretraunetwork")
while True:
    choice = input("1. npm setup | 2. pip setup : ")
    if choice == "1":
       os.system(f"npm install fake-useragent")
       os.system(f'npm install socks')
       os.system(f"npm install hpack")
       os.system(f"npm install colors")
       break
    elif choice == "2":
       os.system(f"pip install telebot")
       os.system(f"pip install requests")
       break