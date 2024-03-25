from colorama import Fore, Style, init
import re
import instaloader
import json
import os

common_passwords = [
    "12345678", "123456789", "qwerty", "22222222", "11111111", "abc123", "123123123", "senha", "password"
]

def is_password_secure(password):
    if len(password) < 8:
        return False
    for common_pw in common_passwords:
        if password == common_pw:
            return False
    return True

def read_accounts_from_file(file_path):
    if file_path.endswith(".txt"):
        with open(file_path, "r") as file:
            accounts = []
            for line in file:
                line = line.strip()
                if "@" in line:
                    username = line
                    password = next(file).strip() if next(file) != "" else ""
                else:
                    match = re.search(r"(\w+):(\w+)", line)
                    if match:
                        username = match.group(1)
                        password = match.group(2)
                    else:
                        username = line
                        password = next(file).strip() if next(file) != "" else ""
                accounts.append({"username": username, "password": password})
        return accounts
    elif file_path.endswith(".json"):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        raise ValueError("Invalid file format. Please provide a .txt or .json file.")

def save_accounts_to_json(accounts, file_path):
    with open(file_path, "w") as file:
        json.dump(accounts, file, indent=4)

def add_account_from_file(file_path, username, password):
    accounts = read_accounts_from_file(file_path)
    accounts.append({"username": username, "password": password})
    save_accounts_to_json(accounts, file_path)

if __name__ == "__main__":
    init(autoreset=True)

    username = input("[*] Digite o nome de usuário da conta do Instagram: ")
    password = input("[*] Digite a senha da conta do Instagram: ")

    if not is_password_secure(password):
        print(Fore.RED + "[!] A senha deve ter pelo menos 8 caracteres e não deve ser uma senha comum.")
        exit()

    accounts_file_path = "./conf/json/accounts/accounts.json"
    os.makedirs(os.path.dirname(accounts_file_path), exist_ok=True)

    try:
        print(Fore.CYAN + '[+] Testando conta...')
        L = instaloader.Instaloader()
        L.login(username, password)
        print(Fore.GREEN + '[!] Conta bem-sucedida!')

        if os.path.exists(accounts_file_path):
            accounts = read_accounts_from_file(accounts_file_path)
        else:
            accounts = []

        if any(account["username"] == username for account in accounts):
            print(Fore.YELLOW + '[!] A conta já está registrada no arquivo.')
            response = input(Fore.YELLOW + '[?] Deseja continuar e adicionar a conta novamente? (S/N): ').strip().upper()
            if response == 'S':
                print(Fore.BLUE + '[!] Adicionando conta novamente...')
                add_account_from_file(accounts_file_path, username, password)
            else:
                print(Fore.RED + '[!] Operação cancelada.')
                exit()
        else:
            print(Fore.BLUE + '[+] Registrando nova conta...')
            accounts.append({'username': username, 'password': password})
            save_accounts_to_json(accounts, accounts_file_path)
            print(Fore.BLUE + '[i] Conta registrada com sucesso!')
    except instaloader.exceptions.BadCredentialsException:
        print(Fore.RED + '[!] Erro no login: Credenciais inválidas.')
