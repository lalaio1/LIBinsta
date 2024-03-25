import time
from rich import print
from rich.console import Console
from rich.panel import Panel
from pystyle import Write, System, Colors
from colorama import Fore

def display_panel(title, content):
    console = Console()
    console.print(Panel(content, title=title, style="black"))

title = ""
content = '''
[bold red]●[bold yellow] ●[bold green] ● 
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
'''
display_panel(title, content)