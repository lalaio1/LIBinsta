import os
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress

console = Console()

def baixar_wordlist(url, destino):
    response = requests.get(url, stream=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))

    with open(destino, 'wb') as file, Progress() as progress:
        task = progress.add_task("[cyan]Baixando:[/cyan]", total=total_size_in_bytes)

        downloaded_bytes = 0

        for data in response.iter_content(chunk_size=1024):
            file.write(data)
            downloaded_bytes += len(data)
            progress.update(task, completed=downloaded_bytes)

        progress.stop()

    console.print("\n[bold][green][!] Download concluído![/green][/bold] ", style="green")

    if total_size_in_bytes != 0 and downloaded_bytes != total_size_in_bytes:
        return False
    return True

def carregar_tabela(wordlists):
    table = Table(title=f"[i] Informações das Wordlists", show_lines=True)
    table.add_column("ID", justify="right", style="cyan")
    table.add_column("Nome do Arquivo", justify="left", style="magenta")
    table.add_column("Tamanho (MB)", justify="right", style="green")

    for i, wordlist in enumerate(wordlists):
        wordlist_size_mb = round(int(requests.head(wordlist["url"]).headers.get('content-length', 0)) / (1024 * 1024), 2)
        table.add_row(str(i+1), wordlist['nome'], str(wordlist_size_mb))

    wordlist_panel = Panel(table, title="", border_style="blue")
    console.print(wordlist_panel)

def main():
    console.print("[bold blue] [[/bold blue][bold yellow]+[/bold yellow][bold blue]] Isso pode demorar um pouco ...[/bold blue]")

    wordlists = [
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/burnett.txt", "nome": "burnett.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/common_passwords_win.txt", "nome": "common_passwords_win.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/common_roots.txt", "nome": "common_roots.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/darkweb_2017.txt", "nome": "darkweb_2017.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/default_passwords_for_services.txt", "nome": "default_passwords_for_services.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/dutch_passwords.txt", "nome": "dutch_passwords.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/hak5.txt", "nome": "hak5.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/honeynet.txt", "nome": "honeynet.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/ipmi_passwords.txt", "nome": "ipmi_passwords.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/keyboard_patterns.txt", "nome": "keyboard_patterns.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/medical_devices_passwords.txt", "nome": "medical_devices_passwords.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/most_used_passwords.txt", "nome": "most_used_passwords.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/most_used_passwords_ncsc.txt", "nome": "most_used_passwords_ncsc.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/nord_vpn.txt", "nome": "nord_vpn.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/openwall.txt", "nome": "openwall.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/password.txt", "nome": "password.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/probable_wpa.txt", "nome": "probable_wpa.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/top_adobe_passwords.txt", "nome": "top_adobe_passwords.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/unix_passwords.txt", "nome": "unix_passwords.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/xato_net_passwords.txt", "nome": "xato_net_passwords.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/000webhost.txt", "nome": "000webhost.txt"},
        {"url": "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/passwords/bt4_passwords.txt", "nome": "bt4_passwords.txt"}
    ]


    carregar_tabela(wordlists)

    escolha_id = int(input("\033[1;30m-> Digite o ID da wordlist que deseja baixar: \033[0m")) - 1

    if 0 <= escolha_id < len(wordlists):
        wordlist = wordlists[escolha_id]
        url = wordlist["url"]
        destino = os.path.join("./conf/wordlists", wordlist["nome"])
        
        try:
            sucesso = baixar_wordlist(url, destino)

            if sucesso:
                wordlist_size_mb = round(int(requests.head(url).headers.get('content-length', 0)) / (1024 * 1024), 2)
                wordlist_info = f"[bold green]ID: {escolha_id + 1}, Nome: {wordlist['nome']}, Tamanho: {wordlist_size_mb} MB[/bold green]"
                wordlist_panel = Panel(wordlist_info, title="Wordlist Baixada com Sucesso", border_style="green")
                console.print(wordlist_panel)
                console.print(f"[bold green]Caminho: {destino}[/bold green]")
            else:
                pass  # Não exibe mensagem de erro
        except Exception as e:
            pass  # Não exibe mensagem de erro


if __name__ == "__main__":
    main()
