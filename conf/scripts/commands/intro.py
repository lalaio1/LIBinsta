import os
import json
from getpass import getpass
import time
import subprocess as sub
import random
import requests
import getpass
import re
from rich import print
from rich.console import Console
from rich.panel import Panel

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_word_in_file(url, word):
    response = requests.get(url)
    if response.status_code == 200:
        file_content = response.text
        if word in file_content:
            os.system("clear")
            print(Panel('''
[bold white][[bold red]^[bold white]] [bold green] By: lalaio1
[bold white][[bold red]^[bold white]] [bold green] Github: lalaio1
[bold white][[bold red]^[bold white]] [bold green] Discord: lalaio1
 '''))
            print(f'[bold green]Your id[italic blue] {word} [italic green] Has SucessFully Accepted')
            print(f"[bold white][[bold blue]✓[bold white]] [bold green]Login Sucess Full Your User Id : [italic green]{word}")
            time.sleep(5)
            pass
            
           
        else:
            print(Panel('''
[bold white][[bold red]^[bold white]] [bold green] By: lalaio1
[bold white][[bold red]^[bold white]] [bold green] Github: lalaio1
[bold white][[bold red]^[bold white]] [bold green] Discord: lalaio1
 '''))
            print(f"[bold green]You haven't Allowed/n[italic yellow] Your Id is [italic red] {word}[bold green] Contact Admin For Activation")
            print(f"[bold blue]Send Him The Id [bold yellow] {word} [bold blue] For Activation")
    else:
        print(f"Failed to retrieve the file. Status code: {response.status_code}")
url = "https://raw.githubusercontent.com/MR-S74RK/INSTA/main/.img/users.txt"  
word_to_find = getpass.getuser() 

find_word_in_file(url,word_to_find)


# password+ banner
os.system("clear")


# BANNER educational purposes
print(Panel( '''

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

[bold red] LIBinsta By // lalaio1                           
'''))
print(Panel('''
[bold white][[bold red]^[bold white]] [bold green] By: lalaio1
[bold white][[bold red]^[bold white]] [bold green] Github: lalaio1
[bold white][[bold red]^[bold white]] [bold green] Discord: lalaio1
 '''))



class bcolors:
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'


def start():
    clear_screen()
    print(Panel('''
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

[bold red] LIBinsta By // lalaio1
                      
'''))

def acquisizione():
    while True:
        if veri_break == "si":
            break
        USER = input('\033[1m\033[92m [?]ENTER INSTAGRAM USERNAME: ')
        wl = input("\033[1m\033[92m [?]Enter the PassList along The Path: ")
        
        clear_screen()
        veri_break = "si"
        break


