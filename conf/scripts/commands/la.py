import os
from rich.console import Console

def listar_arvore(caminho, nivel=0, console=Console()):
    if nivel > 0:
        prefixo = "|" + "   " * (nivel - 1) + "|-- "
        console.print(f"{prefixo}[blue]{os.path.basename(caminho)}[/blue]")

    if os.path.isdir(caminho):
        conteudo = os.listdir(caminho)
        conteudo.sort()

        for i, nome_arquivo in enumerate(conteudo):
            caminho_completo = os.path.join(caminho, nome_arquivo)
            é_último_item = i == len(conteudo) - 1
            prefixo = "|" + "   " * nivel + ("`-- " if é_último_item else "|-- ")
            listar_arvore(caminho_completo, nivel + 1, console)

if __name__ == "__main__":
    caminho_raiz = "."  
    console = Console()
    listar_arvore(caminho_raiz, console=console)
