import json
from rich.console import Console
from rich.panel import Panel

COR_VERDE = "[green]"
COR_VERMELHO = "[red]"
COR_RESET = "[reset]"
COR_AMARELO = "[yellow]"

def carregar_user_agents(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r") as arquivo:
            conteudo_arquivo = arquivo.read()
            return json.loads(conteudo_arquivo) if conteudo_arquivo else []
    except json.JSONDecodeError as e:
        raise ValueError(f"{COR_VERMELHO}[{COR_AMARELO}!{COR_VERMELHO}] Erro ao decodificar JSON: {e}{COR_RESET}")
    except FileNotFoundError:
        raise FileNotFoundError(f"{COR_VERMELHO}[{COR_AMARELO}!{COR_VERMELHO}] Arquivo de User-Agents não encontrado.{COR_RESET}")

def listar_user_agents():
    caminho_arquivo = "./conf/json/agent/agents.json"
    console = Console()

    try:
        user_agents = carregar_user_agents(caminho_arquivo)

        if not user_agents:
            console.print(f"{COR_VERMELHO}[{COR_AMARELO}!{COR_VERMELHO}] A lista de User-Agents está vazia.{COR_RESET}")
        else:
            console.print(f"{COR_AMARELO}[{COR_VERDE}+{COR_AMARELO}] Lista de User-Agents:{COR_RESET}")
            for index, agent in enumerate(user_agents, start=1):
                console.print(f"   {index}. {COR_VERDE}{agent}{COR_RESET}")

            console.print(f"\n{COR_AMARELO}[{COR_VERDE}+{COR_AMARELO}] Total de User-Agents: {len(user_agents)}{COR_RESET}")

    except (ValueError, FileNotFoundError) as e:
        console.print(str(e))

if __name__ == "__main__":
    listar_user_agents()
