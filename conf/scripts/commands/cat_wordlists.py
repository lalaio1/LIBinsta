from rich.console import Console
from rich.table import Table
from rich import box
import os

cores = {
    "reset": "\033[0m",
    "preto": "\033[0;30m",
    "vermelho": "\033[0;31m",
    "verde": "\033[0;32m",
    "amarelo": "\033[0;33m",
    "azul": "\033[0;34m",
    "roxo": "\033[0;35m",
    "ciano": "\033[0;36m",
    "branco": "\033[0;37m",
    "negrito": "\033[1m",
    "sublinhado": "\033[4m",
    "inverter": "\033[7m",
    "brilho": "\033[1;37;40m"
}


# Defina sua variável de estilo
estilo_destaque = "bold blue"

def listar_arquivos():
    pasta = "./conf/wordlists/"
    arquivos = os.listdir(pasta)
    return arquivos

def exibir_conteudo_arquivo(nome_arquivo):
    try:
        caminho_arquivo = f"./conf/wordlists/{nome_arquivo}"
        with open(caminho_arquivo, 'r') as arquivo:
            return arquivo.readlines()
    except FileNotFoundError:
        return [f"[bold red][!] Erro:[/bold red] O arquivo '{nome_arquivo}' não foi encontrado."]

def criar_painel():
    console = Console()

    # Cria a tabela
    table = Table(show_header=True, header_style="bold cyan", box=box.SIMPLE)
    table.add_column("ID", style="magenta", justify="center")
    table.add_column("Wordlists", style="green")

    # Adiciona os arquivos à tabela
    arquivos = listar_arquivos()
    for i, arquivo in enumerate(arquivos, start=1):
        table.add_row(str(i), arquivo)

    # Adiciona uma linha separadora
    table.add_row("", "")

    # Imprime a tabela
    console.print(table)

def main():
    criar_painel()

    # Solicita ao usuário o ID do arquivo desejado
    id_arquivo = int(input(f"\n{cores['preto']}[$] Digite o ID do arquivo que deseja visualizar:{cores['branco']} "))
    if 1 <= id_arquivo <= len(listar_arquivos()):
        nome_arquivo = listar_arquivos()[id_arquivo - 1]
        linhas = exibir_conteudo_arquivo(nome_arquivo)

        # Exibe o conteúdo do arquivo com destaque para o nome do arquivo
        console = Console()
        console.print(f"\n[bold yellow][+][/bold yellow] [bold black]Conteúdo do arquivo [/bold black]'[{estilo_destaque}]{nome_arquivo}[/{estilo_destaque}]:\n")
        for linha in linhas:
            console.print(linha, style="white", end="")
    else:
        console = Console()
        console.print("[bold red][!] ID inválido. Por favor, insira um ID válido.")

if __name__ == "__main__":
    main()
