from rich.console import Console
from rich.table import Table
from rich import box
import json
import os

def clear_username(accounts, username):
    accounts = [account for account in accounts if account['username'] != username]
    return accounts

def clear_password(accounts, password):
    accounts = [account for account in accounts if account['password'] != password]
    return accounts

def clear_email(accounts, email):
    accounts = [account for account in accounts if account.get('email') != email]
    return accounts

def clear_all(accounts):
    return []

def save_accounts_to_json(accounts, file_path):
    with open(file_path, "w") as file:
        json.dump(accounts, file, indent=4)

def clear_menu(accounts, file_path):
    console = Console()

    clear_options = {
        '1': ('Clear Username', lambda: clear_username(accounts, input("Enter username to clear: "))),
        '2': ('Clear Password', lambda: clear_password(accounts, input("Enter password to clear: "))),
        '3': ('Clear Email', lambda: clear_email(accounts, input("Enter email to clear: "))),
        '4': ('Clear All', lambda: clear_all(accounts))
    }

    while True:
        if not accounts:
            console.print("[yellow]No accounts to clear![/yellow]")
            break

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Option", style="dim", width=12)
        table.add_column("Description", justify="center")

        for key, (option, _) in clear_options.items():
            table.add_row(f"[cyan]{key}[/cyan]", option)

        console.print("\n" + "[yellow][*] Clear Menu:[/yellow]", style="bold")
        console.print(table)

        console.print(f"[blue][i] Total accounts:[/blue] {len(accounts)}")
        console.print("[cyan]0[/cyan]. Exit")

        choice = console.input("[yellow][$] Select an option:[/yellow] ").strip()

        if choice == '0':
            break

        if choice in clear_options:
            clear_function = clear_options[choice][1]
            accounts = clear_function()
            save_accounts_to_json(accounts, file_path)
            console.print("[green][!] Accounts cleared successfully![/green]")
        else:
            console.print("[red][!] Invalid choice![/red]")

if __name__ == "__main__":
    file_path = "./conf/json/accounts/accounts.json"

    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
                accounts = json.load(file)
        except json.decoder.JSONDecodeError:
            accounts = []
    else:
        accounts = []

    clear_menu(accounts, file_path)
