import http.server
import socketserver
import webbrowser
from colorama import Fore, Style
import os
import platform
import subprocess

python_command = "python"
if platform.system() == "Linux":
    python_command = "python3"

port = 8000
directory = "./conf/site/index.html"

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"{Fore.GREEN}[{Fore.YELLOW}+{Fore.GREEN}]Servidor iniciado em {Fore.CYAN}: http://localhost:{port}{Style.RESET_ALL}")
    webbrowser.open(f"http://localhost:{port}/conf/site")
    try:
        print(f"{Fore.YELLOW}[{Fore.BLUE}i{Fore.YELLOW}] Pressione Ctrl+C para encerrar o servidor.{Style.RESET_ALL}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()  # Certificar-se de fechar o servidor
        print(f"\n{Fore.RED}[!] Servidor encerrado.{Style.RESET_ALL}")
        console_script_path = os.path.abspath("./conf/script/LIBconsole.py")
        subprocess.run([python_command, console_script_path], shell=True)