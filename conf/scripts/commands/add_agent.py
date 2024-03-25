import json
from colorama import init, Fore

# Inicialize o colorama
init(autoreset=True)

def validar_user_agent(user_agent):
    return any(browser in user_agent for browser in ["Mozilla", "Chrome", "Edge"])

def verificar_user_agent_existente(user_agent, lista):
    return user_agent in lista

def adicionar_user_agent():
    caminho_arquivo = "./conf/json/agent/agents.json"

    try:
        with open(caminho_arquivo, "r+") as arquivo:
            try:
                user_agents = json.load(arquivo)
            except json.JSONDecodeError:
                user_agents = []

            arquivo.seek(0)  # Volte ao início do arquivo para escrita

            novo_user_agent = input("[*] Digite o novo User-Agent: ")

            if verificar_user_agent_existente(novo_user_agent, user_agents):
                confirmacao = input(Fore.YELLOW + "[!] Este User-Agent já está na lista. Deseja adicionar mesmo assim? [s/n] " + Fore.RESET)
                if confirmacao.lower() != 's':
                    print(Fore.CYAN + "[*] Adição cancelada." + Fore.RESET)
                    return

            if validar_user_agent(novo_user_agent):
                user_agents.append(novo_user_agent)
                json.dump(user_agents, arquivo, indent=4)
                print(Fore.GREEN + "[*] User-Agent adicionado com sucesso!" + Fore.RESET)
            else:
                print(Fore.RED + "[!] O User-Agent inserido não é válido." + Fore.RESET)

    except Exception as e:
        print(Fore.RED + f"[!] Erro ao abrir o arquivo: {e}" + Fore.RESET)

# Exemplo de uso:
adicionar_user_agent()
