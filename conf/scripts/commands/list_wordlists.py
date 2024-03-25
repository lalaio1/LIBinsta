import os
from rich.console import Console
from rich.table import Table
from rich import pretty
import re

pretty.install()

def convert_bytes(bytes_size):
    suffixes = {
        1024: "KB",
        1048576: "MB",
        1073741824: "GB",
    }

    for divisor, suffix in suffixes.items():
        if bytes_size >= divisor:
            return f"{bytes_size / divisor:.2f} {suffix}"

    return f"{bytes_size} Bytes"


def analisar_senhas(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        content = file.read()

        num_linhas = content.count('\n') + 1

        palavras = re.findall(r'\b\w+\b', content)

        contagem_palavras = {}
        for palavra in palavras:
            contagem_palavras[palavra.lower()] = contagem_palavras.get(palavra.lower(), 0) 

        media_caracteres = sum(len(word) for word in palavras) / len(palavras) if palavras else 0

        return num_linhas, contagem_palavras, media_caracteres

def listar_arquivos_info(diretorio):
    console = Console()

    lista_arquivos = os.listdir(diretorio)
    lista_arquivos.sort()

    for arquivo in lista_arquivos:
        caminho_completo = os.path.join(diretorio, arquivo)

        if os.path.isfile(caminho_completo):
            num_linhas, contagem_palavras, media_caracteres = analisar_senhas(caminho_completo)

            table = Table(show_lines=True)
            table.add_column("Propriedade", style="cyan", justify="right")
            table.add_column("Valor", justify="left")

            table.add_row("Nome:", arquivo)
            table.add_row("Caminho:", caminho_completo)
            table.add_row("Tamanho:", convert_bytes(os.path.getsize(caminho_completo)))
            table.add_row("Número de Linhas:", str(num_linhas))
            table.add_row("Média de Caracteres por Senha:", f"{media_caracteres:.2f}")

            console.print(table)

if __name__ == "__main__":
    diretorio_wordlists = "./conf/wordlists"
    listar_arquivos_info(diretorio_wordlists)
