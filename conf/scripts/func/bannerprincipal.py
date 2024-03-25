import time
from pystyle import Write, System, Colors
from colorama import Fore

def display_banner():
    Write.Print(f"""                  
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
\t\t         
\t\t                                                                                                                              
""", Colors.red_to_blue, interval=0.000)
    time.sleep(1)