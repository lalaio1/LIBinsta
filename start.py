import subprocess
import sys
import os
import platform

cor_vermelha = "\033[1;31m"
cor_verde = "\033[1;32m"
cor_amarela = "\033[1;33m"
cor_azul = "\033[1;34m"
cor_roxa = "\033[1;35m"
cor_ciano = "\033[1;36m"
cor_branca = "\033[1;37m"
cor_reset = "\033[0m"

def instalar_bibliotecas_necessarias():
    bibliotecas = [
        "selenium ",
        "colorama",
        "platform",
        "psutil",
        "pystyle",
        "terminaltables",
        "pandas",
        "nltk",
        "stem",
        "tabulate",
        "inquirer",
        "typer[all]"
    ]

    print(f"\n{cor_amarela}[!] Verificando bibliotecas...{cor_reset}")

    for biblioteca in bibliotecas:
        print(f"{cor_reset}[{cor_amarela}*{cor_reset}]{cor_amarela} Verificando {biblioteca}{cor_reset}")
        try:
            __import__(biblioteca)
            print(f"{cor_reset}[{cor_azul}+{cor_reset}]{cor_verde} {biblioteca} Verificada {cor_reset}")
        except ImportError:
            print(f"{cor_reset}[{cor_vermelha}-{cor_reset}]{cor_vermelha} Instalando biblioteca {biblioteca}{cor_reset}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", biblioteca])

def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")

def verificar_versao_python():
    versao_minima = (3, 11, 7)  
    versao_atual = sys.version_info

    if versao_atual < versao_minima:
        print(f"{cor_reset}[{cor_vermelha}-{cor_reset}]{cor_vermelha} Versão do Python inadequada. Atualize para pelo menos {versao_minima[0]}.{versao_minima[1]}{cor_reset}")
        sys.exit(1)
    else:
        print(f"{cor_reset}[{cor_azul}+{cor_reset}]{cor_verde} Versão do Python verificada.{cor_reset}")

def verificar_versao_pip():
    try:
        from pip._internal import main as pipmain
    except ImportError:
        from pip import main as pipmain

    versao_minima_pip = "24.0" 

    try:
        pipmain(['install', '--upgrade', 'pip'])
        import pip
        if pip.__version__ < versao_minima_pip:
            print(f"{cor_reset}[{cor_vermelha}-{cor_reset}]{cor_vermelha} Versão do pip inadequada. Atualize para pelo menos {versao_minima_pip}{cor_reset}")
            sys.exit(1)
        else:
            print(f"{cor_reset}[{cor_azul}+{cor_reset}]{cor_verde} Versão do pip verificada.{cor_reset}")
    except Exception as e:
        print(f"{cor_reset}[{cor_vermelha}-{cor_reset}]{cor_vermelha} Erro ao verificar a versão do pip: {str(e)}{cor_reset}")

def tutorial_admin_windows():
    print(f"{cor_reset}[{cor_azul}i{cor_reset}]{cor_ciano} Passo a Passo para Executar como Administrador no Windows:{cor_reset}")
    print(f"{cor_reset}   1. Clique com o botão direito no script 'start.py'.")
    print(f"{cor_reset}   2. Selecione 'Executar como administrador'.")
    print(f"{cor_reset}   3. Confirme qualquer prompt de UAC (Controle de Conta de Usuário).")
    sys.exit(1)

def tutorial_admin_linux():
    print(f"{cor_reset}[{cor_azul}i{cor_reset}]{cor_ciano} Passo a Passo para Executar como Administrador no Linux:{cor_reset}")
    print(f"{cor_reset}   1. Abra um terminal.")
    print(f"{cor_reset}   2. Navegue até o diretório do script usando o comando 'cd'.")
    print(f"{cor_reset}   3. Execute 'chmod +x start.py' para dar permissões de execução.")
    print(f"{cor_reset}   4. Execute 'sudo python3 start.py' para iniciar o script.")
    sys.exit(1)

def verificar_administrador():
    if platform.system() == "Windows":
        try:
            print(f"{cor_reset}[{cor_azul}+{cor_reset}]{cor_verde} Verificando permções de adiministrador.{cor_reset}")
            is_admin = os.getuid() == 0
        except AttributeError:
            
            is_admin = os.name == 'nt'

        if not is_admin:
            print(f"[{cor_vermelha}-{cor_reset}]{cor_vermelha} Permissões administrativas necessárias no Windows.{cor_reset}")
            tutorial_admin_windows()
    elif platform.system() == "Linux":
        if os.geteuid() != 0:
            print(f"[{cor_vermelha}-{cor_reset}]{cor_vermelha} Permissões administrativas necessárias no Linux.{cor_reset}")
            tutorial_admin_linux()
    else:
        print(f"[{cor_vermelha}-{cor_reset}]{cor_vermelha} Sistema operacional não suportado.{cor_reset}")
        sys.exit(1)

import subprocess
import urllib.request
import os

def check_for_updates():
    try:
        with urllib.request.urlopen("https://raw.githubusercontent.com/lalaio1/LIBinsta/main/version.txt") as response:
            latest_version = response.read().decode().strip()
            current_version = get_current_version()
            if latest_version != current_version:
                print("[!] Uma nova versão está disponível. Atualizando...")
                update_repository()
                update_version_file(latest_version)
                print("[/] Atualização concluída com sucesso.")
            else:
                print("[i] Você já tem a versão mais recente.")
    except Exception as e:
        print(f"[e] Erro ao verificar atualizações: {e}")

def get_current_version():
    try:
        with open("version.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""

def update_repository():
    try:
        subprocess.run(["git", "pull"])
    except Exception as e:
        print(f"[e] Erro ao atualizar o repositório: {e}")

def update_version_file(version):
    try:
        with open("version.txt", "w") as file:
            file.write(version)
    except Exception as e:
        print(f"[e] Erro ao atualizar o arquivo de versão: {e}")



def verificar_arquitetura_sistema():
    arquitetura_desejada = '64bit'
    arquitetura_atual = platform.architecture()[0]

    if arquitetura_atual != arquitetura_desejada:
        print(f"{cor_reset}[{cor_vermelha}-{cor_reset}]{cor_vermelha} Arquitetura do sistema incompatível. Utilize uma arquitetura de {arquitetura_desejada}.{cor_reset}")
        sys.exit(1)
    else:
        print(f"{cor_reset}[{cor_azul}+{cor_reset}]{cor_verde} Arquitetura do sistema verificada.{cor_reset}")

def verificar_sistema_operacional():
    sistema_operacional_atual = platform.system()

    if sistema_operacional_atual == "Windows":
        print(f"{cor_reset}[{cor_azul}+{cor_reset}]{cor_verde} Sistema operacional: Windows.{cor_reset}")
    elif sistema_operacional_atual == "Linux":
        print(f"{cor_reset}[{cor_azul}+{cor_reset}]{cor_verde} Sistema operacional: Linux.{cor_reset}")
    else:
        print(f"{cor_reset}[{cor_vermelha}-{cor_reset}]{cor_vermelha} Sistema operacional não suportado.{cor_reset}")
        sys.exit(1)

def verificar_e_definir_flag():
    flag_path = "conf/flag.txt"

    if os.path.exists(flag_path):
        with open(flag_path, "r") as file:
            flag_status = file.read().strip()
    else:
        flag_status = "False"

    return flag_status

def setar_flag_true():
    flag_path = "conf/flag.txt"

    with open(flag_path, "w") as file:
        file.write("True")

def iniciar_LIBconsole_logs():
    os.system(f"python3 ./conf/logs/logs.py") if os.name != 'nt' else os.system(f"python ./conf/logs/logs.py")
    os.system(f"python3 ./conf/scripts/LIBconsole.py") if os.name != 'nt' else os.system(f"python ./conf/scripts/LIBconsole.py")


def imprimir_banner():
    banner = f"""
      .---.        .-----------      
     /     \\  __  /   ------      
    / /     \\(  )/   -----        
   //////   ' \\/ `   ---
  //// / // :    : ---
 // /   /  /`    '--
//          //..\\

       ====UU====UU====
           '||\\`
             ''``        {cor_reset}[{cor_verde}!{cor_reset}] {cor_amarela}Verificação iniciada... {cor_reset}                                         
"""
    print(f"{cor_azul} {cor_roxa} {banner}{cor_reset}")


if __name__ == "__main__":
    os.system("clear" if os.name != "nt" else "cls")

    flag_status = verificar_e_definir_flag()

    if flag_status == "True":
        print(f"{cor_azul}[{cor_verde}+{cor_azul}] Verificação já foi executada anteriormente. Saindo...{cor_reset}")
        os.system("clear" if os.name != "nt" else "cls")

        if os.name != "posix":
            check_for_updates()
            iniciar_LIBconsole_logs()
          

    else:
        imprimir_banner()
        verificar_administrador()
        verificar_sistema_operacional()
        verificar_arquitetura_sistema()
        verificar_versao_python() 
        verificar_versao_pip() 
        check_for_updates()
        instalar_bibliotecas_necessarias()
        setar_flag_true()

        print(f"{cor_azul}[{cor_verde}!{cor_azul}] Bibliotecas instaladas. Verificação concluída.{cor_reset}")
        if os.name != "posix":
            iniciar_LIBconsole_logs()
            
     