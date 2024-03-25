from colorama import init, Fore
import json

def limpar_user_agents():
    caminho_arquivo = "./conf/json/agent/agents.json"

    try:
        with open(caminho_arquivo, "w") as arquivo:
            json.dump([], arquivo, indent=4)
        print(Fore.YELLOW + "[*] Conteúdo do arquivo limpo. Todos os User-Agents foram removidos." + Fore.RESET)

    except Exception as e:
        print(Fore.RED + f"[!] Erro ao limpar o arquivo: {e}" + Fore.RESET)

# Exemplo de uso:
limpar_user_agents()
