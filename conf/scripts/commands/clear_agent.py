from rich import print
from rich.panel import Panel
from colorama import init, Fore
import json
from user_agents import parse

init(autoreset=True)

def exibir_banner():
    banner_text = f"""                                    
       1. {Fore.YELLOW}Remover por sistema operacional{Fore.RESET}
       2. {Fore.YELLOW}Remover por versão{Fore.RESET}            
       3. {Fore.YELLOW}Remover por navegador{Fore.RESET}   
       4. {Fore.YELLOW}Remover User-Agent específico{Fore.RESET}   
       5. {Fore.YELLOW}Remover para pesar menos{Fore.RESET}
       6. {Fore.YELLOW}Cancelar{Fore.RESET}
    """

    print(Panel(banner_text, style="cyan"))

def remover_por_sistema_operacional(user_agents):
    sistema_operacional = input(Fore.YELLOW + "-> Insira o sistema operacional que deseja remover: " + Fore.RESET)
    return [ua for ua in user_agents if parse(ua).os.family != sistema_operacional]

def remover_por_versao(user_agents):
    versao = input(Fore.YELLOW + "-> Insira a versão que deseja remover: " + Fore.RESET)
    return [ua for ua in user_agents if parse(ua).browser.version_string != versao]

def remover_por_navegador(user_agents):
    navegador = input(Fore.YELLOW + "-> Insira o navegador que deseja remover: " + Fore.RESET)
    return [ua for ua in user_agents if parse(ua).browser.family != navegador]

def remover_user_agent_especifico(user_agents):
    user_agent_especifico = input(Fore.YELLOW + "-> Insira o User-Agent específico que deseja remover: " + Fore.RESET)
    return [ua for ua in user_agents if ua != user_agent_especifico]

def remover_para_pesar_menos(user_agents):
    percentual = float(input(Fore.YELLOW + "-> Insira o percentual (0-100) de User-Agents que deseja remover: " + Fore.RESET))
    num_remover = int((percentual / 100) * len(user_agents))
    return user_agents[num_remover:]

def limpar_user_agents():
    caminho_arquivo = "./conf/json/agent/agents.json"

    try:
        with open(caminho_arquivo, "r") as arquivo:
            user_agents = json.load(arquivo)

        if not user_agents:
            print(Fore.YELLOW + "[*] O arquivo já está vazio. Nada a fazer." + Fore.RESET)
            return

        exibir_banner()
        opcao = input(Fore.CYAN + "[$] Escolha uma opção: " + Fore.RESET)

        if opcao == "1":
            user_agents = remover_por_sistema_operacional(user_agents)
        elif opcao == "2":
            user_agents = remover_por_versao(user_agents)
        elif opcao == "3":
            user_agents = remover_por_navegador(user_agents)
        elif opcao == "4":
            user_agents = remover_user_agent_especifico(user_agents)
        elif opcao == "5":
            user_agents = remover_para_pesar_menos(user_agents)
        elif opcao == "6":
            print("[*] Operação cancelada. Nenhum User-Agent removido.")
            return
        else:
            print("[!] Opção inválida. Nenhum User-Agent removido.")
            return

        with open(caminho_arquivo, "w") as arquivo:
            json.dump(user_agents, arquivo, indent=4)
            print(f"[*] Conteúdo do arquivo atualizado. [i]: {len(user_agents)} User-Agents restantes.")

    except Exception as e:
        print(f"[!] Erro ao limpar o arquivo: {e}")

limpar_user_agents()
