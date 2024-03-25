import json
from colorama import Fore
import os
from func.commands import execute_command
from func.bannerprincipal import display_banner
from func.clearscreen import clear_screen

clear_screen()

HISTORICO_PATH = "./conf/json/history/history.json"

def load_history():
    try:
        with open(HISTORICO_PATH, "r") as file:
            history = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        history = []
    return history

def save_history(history):
    with open(HISTORICO_PATH, "w") as file:
        json.dump(history, file, indent=2)

if __name__ == "__main__":
    display_banner()
    
    while True:
        user_input = input(Fore.LIGHTBLACK_EX + "-> ")
        
        history = load_history()
        
        history.append(user_input)
        
        try:
            execute_command(user_input)
        except ValueError:
            os.system("python ./conf/scripts/invalidcommand.py")
        
        save_history(history)