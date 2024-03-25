from rich.console import Console
from rich.table import Table
from rich import box
import os

def listar_arquivos():
    pasta = "./conf/wordlists/"
    arquivos = os.listdir(pasta)
    return arquivos

def calcular_peso_total():
    pasta_wordlists = "./conf/wordlists/"
    arquivos = listar_arquivos()

    peso_total = 0

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta_wordlists, arquivo)
        peso_arquivo = os.path.getsize(caminho_arquivo)
        peso_total += peso_arquivo

    return peso_total

def criar_painel():
    console = Console()

    # Cria a tabela
    table = Table(show_header=True, header_style="bold cyan", box=box.SIMPLE)
    table.add_column("ID", style="magenta", justify="center")
    table.add_column("Wordlists", style="green")
    table.add_column("Peso (bytes)", style="blue", justify="right")

    # Adiciona os arquivos à tabela
    arquivos = listar_arquivos()
    for i, arquivo in enumerate(arquivos, start=1):
        caminho_arquivo = os.path.join("./conf/wordlists/", arquivo)
        peso_arquivo = os.path.getsize(caminho_arquivo)

        table.add_row(str(i), arquivo, f"{peso_arquivo:,}")

    # Adiciona uma linha separadora
    table.add_row("", "", "")

    # Adiciona a linha com o peso total
    table.add_row("", "Peso Total", f"{calcular_peso_total():,}", style="bold")

    # Imprime a tabela
    console.print(table)

def clear_wordlists():
    console = Console()

    pasta_wordlists = "./conf/wordlists/"

    try:
        # Lista os arquivos na pasta de wordlists
        arquivos = os.listdir(pasta_wordlists)

        if not arquivos:
            console.print("[bold yellow]A pasta de wordlists está vazia. Nada a limpar.[/bold yellow]")
            return

        # Confirmação do usuário
        confirmacao = input("Tem certeza de que deseja apagar todos os arquivos de wordlists? (s/n): ").lower()

        if confirmacao == 's':
            # Apaga os arquivos
            for arquivo in arquivos:
                caminho_arquivo = os.path.join(pasta_wordlists, arquivo)
                os.remove(caminho_arquivo)

            console.print("[bold green]Todos os arquivos de wordlists foram apagados com sucesso.[/bold green]")
        else:
            console.print("[bold cyan]Operação cancelada.[/bold cyan]")
    except Exception as e:
        console.print(f"[bold red]Ocorreu um erro ao apagar os arquivos: {e}[/bold red]")

def main():
    criar_painel()
    clear_wordlists()

if __name__ == "__main__":
    main()
