import requests
import json

# Cores no formato ANSI escape codes
class Cores:
    RESET = '\033[0m'
    NEGRITO = '\033[1m'
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'

def obter_user_agents(url):
    print(f"{Cores.AMARELO}[!] Enviando solicitação para obter User Agents...{Cores.RESET}")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para erros HTTP
        user_agents = response.json()
        print(f"{Cores.VERDE}[✓] User Agents obtidos com sucesso.{Cores.RESET}")
        return user_agents
    except requests.exceptions.RequestException as e:
        print(f"{Cores.VERMELHO}[!] Erro ao obter User Agents: {e}{Cores.RESET}")
        return None

def salvar_user_agents_no_arquivo(user_agents, caminho_arquivo):
    print(f"{Cores.AMARELO}[!] Salvando User Agents no arquivo...{Cores.RESET}")
    try:
        with open(caminho_arquivo, "w") as arquivo:
            json.dump(user_agents, arquivo, indent=2)
        print(f"{Cores.VERDE}[✓] User Agents salvos em {caminho_arquivo}{Cores.RESET}")
    except Exception as e:
        print(f"{Cores.VERMELHO}[!] Falha ao salvar User Agents no arquivo: {e}{Cores.RESET}")

if __name__ == "__main__":
    url_user_agents = "https://raw.githubusercontent.com/Said-Ait-Driss/user-agents/main/userAgents.json"
    caminho_arquivo = "./conf/json/agent/agents.json"
    
    user_agents = obter_user_agents(url_user_agents)

    if user_agents:
        for ua in user_agents:
            print(ua)

        salvar_user_agents_no_arquivo(user_agents, caminho_arquivo)
    else:
        print(f"{Cores.VERMELHO}[!] Falha ao obter User Agents.{Cores.RESET}")
