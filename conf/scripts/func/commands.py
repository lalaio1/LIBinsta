from func.bannerprincipal import display_banner
from func.clearscreen import clear_screen
import os
import platform

def execute_command(command):
    python_command = "python"
    if platform.system() == "Linux":
        python_command = "python3"

    elif command.lower() in ["bruteforce1", "brute1", "instabrute", "instabrute1", "bruter1", "brutear1"]: 
        os.system(f"{python_command} ./conf/scripts/commands/bruteforce1.py")

    elif command.lower() in ["clear", "cls", "limpar"]:
        clear_screen()

    elif command.lower() in ["help", "h", "?", "??", "-?", "/?", "--?", "hep", "helpe", "helps", "ajuda", "ayuda"]:
        os.system(f"{python_command} ./conf/scripts/commands/help.py")

    elif command.lower() in ["banner", "banner1"]:
        clear_screen()
        display_banner()

    elif command.lower() in ["banner2", "banner green"]:
        clear_screen()
        os.system(f"{python_command} ./conf/scripts/commands/banner2.py")

    elif command.lower() in ["la",  "listar", "ls"]:
        os.system(f"{python_command} ./conf/scripts/commands/la.py")

    elif command.lower() in ["add agent", "add agents"]:
        os.system(f'{python_command} ./conf/scripts/commands/add_agent.py')

    elif command.lower() == "clear all agent":
        os.system(f'{python_command} ./conf/scripts/commands/clear_agent_all.py')

    elif command.lower() == "list agent":
        os.system(f'{python_command} ./conf/scripts/commands/list_agent.py')

    elif command.lower() == "history":
        os.system(f'{python_command} ./conf/scripts/commands/history.py')

    elif command.lower() == "collect agent":
        os.system(f'{python_command} ./conf/scripts/commands/collect_agent.py')

    elif command.lower() == "list wordlists":
        os.system(f'{python_command} ./conf/scripts/commands/list_wordlists.py')

    elif command.lower() == "download wordlists":
        os.system(f'{python_command} ./conf/scripts/commands/download_wordlists.py')

    elif command.lower() == "cat wordlists":
        os.system(f'{python_command} ./conf/scripts/commands/cat_wordlists.py')

    elif command.lower() == "secret spamer -menu":
        os.system(f"{python_command} ./conf/scripts/commands/SecretSpam.py")

    elif command.lower() == "scret.me spamer":
        os.system(f"{python_command} ./conf/scripts/commands/scret.me.py")
     
    elif command.lower() == "ng.link spammer":
        os.system(f"{python_command} ./conf/scripts/commands/ng.link.py")
        
    elif command.lower() == "support":
        os.system(f'{python_command} ./conf/site/python/site.py')

    elif command.lower() == "clear all wordlists":
        os.system(f'{python_command} ./conf/scripts/commands/clear_all_wordlists.py')

    elif command.lower() == "info agents":
        os.system(f'{python_command} ./conf/scripts/commands/info_agents.py')
    
    elif command.lower() == "clear agent":
        os.system(f'{python_command} ./conf/scripts/commands/clear_agent.py')

    elif command.lower() == "bruteforce2":
        os.system(f'{python_command} ./conf/scripts/commands/brute2/app.py')

    elif command.lower() == "add acont":
        os.system(f'{python_command} ./conf/scripts/commands/add_acont.py')
    
    elif command.lower() == "clear acont":
        os.system(f'{python_command} ./conf/scripts/commands/clear_accont.py')

    elif command.lower() == "derrubar":
        os.system(f'{python_command} ./conf/scripts/commands/derrubar.py')
        
    else:
        os.system(f"{python_command} ./conf/scripts/commands/invalidcommand.py")
