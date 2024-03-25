import json
from terminaltables import SingleTable
from colorama import Fore, init

# Inicialize o colorama para evitar conflitos de cores
init(autoreset=True)

def load_commands():
    with open('./conf/json/commands/commands.json', 'r') as file:
        return json.load(file)

def display_help(commands):
    title = [f"{Fore.CYAN} Comando", "Descrição"]
    rows = [[f"{Fore.LIGHTBLUE_EX} {command}", info['description']] for command, info in commands.items()]

    table_data = [title] + rows
    table = SingleTable(table_data)
    table.inner_heading_row_border = False
    table.outer_border = False

    print(table.table)

if __name__ == "__main__":
    commands = load_commands()
    display_help(commands)
