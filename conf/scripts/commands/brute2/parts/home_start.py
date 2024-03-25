from sys import stdout
from colorama import Fore, init
import os

# Banner padrão
default_banner = """""" + Fore.GREEN + """
\t\t       .---.        .-----------
\t\t      /     \  __  /    ------
\t\t     / /     \(  )/    -----
\t\t    //////   ' \/ `   ---
\t\t   //// / // :    : ---
\t\t  // /   /  /`    '--
\t\t //          //..\\\\
\t\t 
\t\t        ====UU====UU====
\t\t            '//||\\\`
\t\t              ''``
                                                          
"""

def home_page():
    os.system("cls")
    stdout.write("\n")
    stdout.write(default_banner)