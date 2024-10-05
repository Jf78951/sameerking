import requests
import time
import random
import os
from colorama import init, Fore

init(autoreset=True)

def approval():
    os.system('clear')
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)

    try:
        httpCaht = requests.get('https://github.com/Jf78951/sameer-convo/tree/main').text.strip()
        if id in httpCaht:
            print(Fore.GREEN + "Y0UR K3Y IS  SUC3SSFULY APPROV3D")
            msg = str(os.geteuid())
            time.sleep(0.5)
            pass
        else:
            eno = input(Fore.YELLOW + 'ENT3R Y0UR N9M3:S9M33R KH9N ')
            os.system('clear')
            print(Fore.GREEN+ "YOUR T0K3N : " + id)
            print(Fore.WHITE + '◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑')
            print(Fore.YELLOW+ "Important Note")
            print(Fore.WHITE + '◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑')
            print(Fore.GREEN+ "Y0UR TOK3N 1S NOT APPROV3D")
            print(Fore.YELLOW + 'Y0U H9V3 TO T9K3 APPROV3L F1RST')
            print(Fore.GREEN + 'FR33 W9L3 DUR R9H3 :)')
            print(Fore.WHITE + '◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑◑')
            print(Fore.GREEN+ ' 【𝐘𝐎𝐎𝐋 𝐎𝐖𝐍𝐀𝐑: 𝐒𝐀𝐌𝐄𝐄𝐑 𝐏𝐀𝐏𝐀 𝐈𝐍𝐒𝐈𝐃𝐄】')
            print(eno + " " + Fore.YELLOW + "Y0UR TOK3N 1S : " + id)
            input(Fore.GREEN+ 'IF YOU WANT TO BUY THEN PRESS ENTER ')
            tks = ('Hello%20sameer-sir%20!%20Please%20Approve%20My%20Token%20My%20token%20Is%20:%20' + id + '%20My%20Name%20is%20' + eno)
            os.system('am start https://wa.me/+919536764960?text=' + tks)
            time.sleep(1)
            exit()

    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        exit()

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = file.readlines()

    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": ("Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36"),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
        "Referer": "www.google.com",
    }

    logos = [
        '''
   \033[1;32m.  /$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$       
 \033[1;34m. /$$__  $$ /$$__  $$| $$$    /$$$| $$_____/| $$_____/| $$__  $$      
 \033[1;32m.| $$  \__/| $$  \ $$| $$$$  /$$$$| $$      | $$      | $$  \ $$      
 \033[1;34m.|  $$$$$$ | $$$$$$$$| $$ $$/$$ $$| $$$$$   | $$$$$   | $$$$$$$/      
 \033[1;32m. \____  $$| $$__  $$| $$  $$$| $$| $$__/   | $$__/   | $$__  $$      
 \033[1;34m. /$$  \ $$| $$  | $$| $$\  $ | $$| $$      | $$      | $$  \ $$      
 \033[1;32m.|  $$$$$$/| $$  | $$| $$ \/  | $$| $$$$$$$$| $$$$$$$$| $$  | $$      
 \033[1;34m. \______/ |__/  |__/|__/     |__/|________/|________/|__/  |__/      
                                                                   
 \033[1;32m. /$$   /$$  /$$$$$$  /$$$$$$$  /$$$$$$$$                             
 \033[1;36m.| $$$ | $$ /$$__  $$| $$__  $$| $$_____/                             
 \033[1;32m.| $$$$| $$| $$  \__/| $$  \ $$| $$                                   
 \033[1;36m.| $$ $$ $$|  $$$$$$ | $$  | $$| $$$$$                                
 \033[1;32m.| $$  $$$$ \____  $$| $$  | $$| $$__/                                
 \033[1;36m.| $$\  $$$ /$$  \ $$| $$  | $$| $$                                   
 \033[1;32m.| $$ \  $$|  $$$$$$/| $$$$$$$/| $$$$$$$$                             
 \033[1;36m.|__/  \__/ \______/ |_______/ |________/              
                                    
\033[1;36m.╔═══════════════════【𝐂𝐎𝐍𝐕𝐎 𝐌𝐔𝐋𝐓𝐈 𝐓𝐎𝐎𝐊𝐄𝐍 𝐓𝐎𝐎𝐋 】══════════════════╗
 \033[1;32m.           "{ownar sameer inside wp-+91953676****}"
\033[1;36m.╚═══════════════════【𝐒𝐀𝐈𝐌 𝐊 𝐃𝐄𝐃 𝐒𝐀𝐌𝐄𝐄𝐑 𝐈𝐍𝐒𝐈𝐃𝐄】══════════════════╝

 \033[1;34m─────────────────────────────────────────────────────────────────────
 \033[1;36m.      【︻╦デ╤━╼𖣘︎𖣘︎𖣘︎𖣘︎【𝐒𝐀𝐌𝐄𝐄𝐑 𝐓𝐎𝐎𝐋 𝐎𝐖𝐍𝐀𝐑】𖣘︎𖣘︎𖣘︎𖣘︎╾━╤デ╦︻】
 \033[1;34m─────────────────────────────────────────────────────────────────────
 
\033[1;32m.╔═══════════════════【★★★𝐒𝐀𝐌𝐄𝐄𝐑 𝐈𝐍𝐒𝐈𝐃𝐄★★★ 】══════════════════╗
 \033[1;36m.         【𝐌𝐔𝐋𝐓𝐈 𝐈𝐃𝐌𝐔𝐋𝐓𝐈 𝐂𝐎𝐍𝐕𝐎 𝐓𝐎𝐎𝐋𝐌𝐔𝐋𝐓𝐈 𝐅𝐈𝐋𝐄 𝐋𝐎𝐃𝐄𝐑】                                
\033[1;32m.╚═══════════════════【★★★ 𝐒𝐀𝐌𝐄𝐄𝐑 𝐈𝐍𝐒𝐈𝐃𝐄★★★】══════════════════╝
        
 \033[1;35m─────────────────────────────────────────────────────────────────────
 \033[1;36m         【︻╦デ╤━╼𖣘︎𖣘︎𖣘︎𖣘︎【𝐒𝐀𝐌𝐄𝐄𝐑 𝐓𝐎𝐎𝐋 𝐎𝐖𝐍𝐀𝐑】𖣘︎𖣘︎𖣘︎𖣘︎╾━╤デ╦︻】                       
 \033[1;35m─────────────────────────────────────────────────────────────────────
'''
    ]

    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            access_token = tokens[token_index].strip()
            full_message = f"{haters_name} {message.strip()}"

            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}
            try:
                response = requests.post(url, json=parameters, headers=headers)
                response.raise_for_status()
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                current_logo = random.choice(logos)
                print(Fore.GREEN + current_logo)
                print(Fore.YELLOW + f"[+] Message {message_index + 1} sent to Convo {target_id} with Token {token_index + 1}: {full_message} at {current_time}")
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[x] Failed to send Message {message_index + 1} to Convo {target_id} with Token {token_index + 1}: {full_message} - Error: {e}")

            time.sleep(speed)
        print(Fore.CYAN + "\n[+] All messages sent. Restarting the process...\n")

def main():
    approval()
    
    print(Fore.MAGENTA + " 𝐒𝐀𝐈𝐌 𝐊𝐈 𝐁𝐇𝐄𝐍 𝐊𝐈 𝐗𝐇𝐔𝐓 𝐅𝐀𝐃𝐍𝐄 𝐖𝐀𝐋𝐀 𝐌𝐔𝐋𝐓𝐈 𝐂𝐎𝐍𝐕𝐎 𝐓𝐎𝐎𝐋 ")
    print(Fore.CYAN + "❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑")
    # Get file paths and other inputs from the user
    tokens_file = input(Fore.GREEN+ "[✓] 𝐒𝐀𝐈𝐌 𝐊𝐈 𝐃𝐃 𝐊𝐈 𝐗𝐇𝐔𝐓 𝐌𝐄 𝐓𝐎𝐎𝐊𝐄𝐍 𝐅𝐈𝐋𝐄 𝐃𝐀𝐋➼'").strip()
    print(Fore.RED+ '❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑')
    target_id = input(Fore.YELLOW + "[✓] 𝐒𝐀𝐈𝐌 𝐊𝐈 𝐁𝐇𝐄𝐍 𝐊𝐎 𝐊𝐇𝐀 𝐂𝐇𝐎𝐃𝐍𝐀 𝐈𝐃 𝐃𝐀𝐋➼ ").strip()
    print(Fore.RED+ '❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑')
    messages_file = input(Fore.GREEN + "[✓] 𝐒𝐀𝐈𝐌 𝐊𝐈 𝐁𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐊 𝐒3 𝐍𝐈𝐊𝐀𝐋 𝐊𝐀𝐑 𝐅𝐈𝐋𝐄 𝐃𝐀𝐋 ➼").strip()
    print(Fore.RED+ '❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑')
    haters_name = input(Fore.YELLOW+ "[✓] 𝐒𝐀𝐈𝐌 𝐊𝐈 𝐁𝐇𝐄𝐍 𝐊 𝐘𝐀𝐑𝐎 𝐊𝐀 𝐍𝐀𝐌𝐄 𝐃𝐀𝐋➼").strip()
    print(Fore.RED+ '❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑')
    speed = float(input(Fore.GREEN + "[✓] 𝐒𝐀𝐈𝐌 𝐊𝐈 𝐁𝐇𝐄𝐍 𝐊𝐎 𝐊𝐈𝐓𝐍𝐈 𝐒𝐏𝐄𝐄𝐃 𝐒𝐄 𝐂𝐇𝐎𝐃𝐍𝐀 𝐇𝐄➼").strip())

    # Start sending messages
    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()