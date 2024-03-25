import time
from pystyle import Write, System, Colors
from colorama import Fore, Style
import os
import platform

python_command = "python"
if platform.system() == "Linux":
    python_command = "python3"

def display_banner():
    System.Clear()
    Write.Print(f"""                                                                                                         
\t\t                                                                                                      
\t\t 
\t\t
\t\t  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
\t\t▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
\t\t░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
\t\t  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
\t\t▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
\t\t▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
\t\t░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
\t\t░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
\t\t      ░                 ░  ░       ░          ░      ░  ░   ░     
\t\t                                                                                     
\t\t [1] Secret.me                                             [2] ngl.link  
\t\t
\t\t                                                                                                                              
""", Colors.red_to_blue, interval=0.000)
    time.sleep(0.40)

def execute_command(option):
    if option == 1:
        System.Clear()
        os.system(f"{python_command} ./conf/scripts/commands/scret.me.py")  # Replace with your actual command for option 1
    elif option == 2:
        System.Clear()
        os.system(f"{python_command} ./conf/scripts/commands/ng.link.py")  
    else:
        print(Fore.RED + "[!] Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    # Display banner
    display_banner()

    user_input = input(Fore.LIGHTBLACK_EX + "-> ")

    try:
        option = int(user_input)
        execute_command(option)
    except ValueError:
        print(Fore.RED + "[!] Invalid input. Please enter a number.")