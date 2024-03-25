import json
from collections import Counter
from rich.console import Console
from rich.table import Table
from user_agents import parse

def obter_sistemas_operacionais_e_navegadores(agents_data):
    sistemas_operacionais_navegadores = {}
    total = 0
    for agent in agents_data:
        user_agent = parse(agent)
        navegador = user_agent.browser.family
        versao = user_agent.browser.version_string
        sistema_operacional = user_agent.os.family
        dispositivo = user_agent.device.family

        if sistema_operacional not in sistemas_operacionais_navegadores:
            sistemas_operacionais_navegadores[sistema_operacional] = []
        sistemas_operacionais_navegadores[sistema_operacional].append((navegador, versao, dispositivo))
        total += 1

    return sistemas_operacionais_navegadores, total

def exibir_tabela_sistemas_operacionais_e_navegadores(sistemas_operacionais_navegadores, total):
    console = Console()
    table = Table(title="[i] Sistemas Operacionais e Navegadores dos User Agents", show_lines=True, header_style="bold blue")
    table.add_column("Sistema Operacional", style="cyan", justify="left")
    table.add_column("Navegador", style="cyan", justify="left")
    table.add_column("Versão", style="cyan", justify="left")
    table.add_column("Dispositivo", style="cyan", justify="left")

    contagem_sistemas_operacionais = Counter()
    contagem_navegadores = Counter()
    contagem_versoes = Counter()

    for sistema_operacional, navegadores in sistemas_operacionais_navegadores.items():
        contagem_sistemas_operacionais[sistema_operacional] += len(navegadores)
        for navegador, versao, dispositivo in navegadores:
            table.add_row(sistema_operacional, navegador, versao, dispositivo)
            contagem_navegadores[navegador] += 1
            contagem_versoes[versao] += 1

    console.print(table)
    console.print(f"[i] Total de User Agents: {total}")

    # Exibindo as informações em tabelas separadas
    table_os = Table(title="[i] Contagem de Sistemas Operacionais", show_lines=True, header_style="bold green")
    table_os.add_column("Sistema Operacional", style="magenta", justify="left")
    table_os.add_column("Contagem", style="magenta", justify="right")
    for os, count in contagem_sistemas_operacionais.most_common():
        table_os.add_row(os, str(count))
    console.print(table_os)

    table_browser = Table(title="[i] Contagem de Navegadores", show_lines=True, header_style="bold green")
    table_browser.add_column("Navegador", style="magenta", justify="left")
    table_browser.add_column("Contagem", style="magenta", justify="right")
    for browser, count in contagem_navegadores.most_common():
        table_browser.add_row(browser, str(count))
    console.print(table_browser)

    table_version = Table(title="Contagem de Versões", show_lines=True, header_style="bold green")
    table_version.add_column("Versão", style="magenta", justify="left")
    table_version.add_column("Contagem", style="magenta", justify="right")
    for version, count in contagem_versoes.most_common():
        table_version.add_row(version, str(count))
    console.print(table_version)

def contar_navegadores(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            agents_data = json.load(arquivo)
            sistemas_operacionais_navegadores, total = obter_sistemas_operacionais_e_navegadores(agents_data)
            
            # Se a lista de sistemas operacionais estiver vazia, adiciona 'Desconhecido' para evitar erros
            if not sistemas_operacionais_navegadores:
                sistemas_operacionais_navegadores = {'Desconhecido': []}

            exibir_tabela_sistemas_operacionais_e_navegadores(sistemas_operacionais_navegadores, total)

    except FileNotFoundError:
        print(f"[!] Arquivo {caminho_arquivo} não encontrado.")
    except json.JSONDecodeError as e:
        print(f"[!] Erro ao decodificar o JSON no arquivo {caminho_arquivo}. Detalhes: {e}")

# Substitua o caminho abaixo pelo seu caminho real
caminho_arquivo_agents = './conf/json/agent/agents.json'
contar_navegadores(caminho_arquivo_agents)
