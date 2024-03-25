import json
from colorama import Fore

HISTORICO_PATH = "./conf/json/history/history.json"

def show_history():
    try:
        with open(HISTORICO_PATH, "r") as file:
            history = json.load(file)

        if not history:
            print(f"{Fore.RED}[!] Histórico vazio.{Fore.RESET}")
        else:
            print(f"{Fore.BLACK}\n[+] Histórico de Comandos:{Fore.RESET}")
            for index, command in enumerate(history, start=1):
                print(f"{index}. {Fore.GREEN}{command}{Fore.RESET}")

    except (json.JSONDecodeError, FileNotFoundError):
        print(f"{Fore.RED}[!] Erro ao ler o arquivo de histórico.{Fore.RESET}")

if __name__ == "__main__":
    show_history()
