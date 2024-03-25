import typer
from typing import Optional
import inquirer
from parts import *
from helper import *

def main(status: Optional[str] = typer.Argument("home"), target: Optional[str] = typer.Argument("none")):
    if status == "home":
        home_page()

        mode = [
            inquirer.List(
                "mode",
                message="Escolha o comprimento da senha",
                choices=[
                    typer.style("6", fg=typer.colors.GREEN),
                    typer.style("7", fg=typer.colors.GREEN),
                    typer.style("8", fg=typer.colors.GREEN),
                    typer.style("9", fg=typer.colors.GREEN),
                    typer.style("10", fg=typer.colors.GREEN),
                    typer.style("11", fg=typer.colors.GREEN),
                    typer.style("12", fg=typer.colors.GREEN),
                    typer.style("13", fg=typer.colors.GREEN),
                    typer.style("14", fg=typer.colors.GREEN),
                ]
            ),
        ]
        y = inquirer.prompt(mode)

        if "wordlists" in y["mode"]:
            user = typer.prompt(f"{typer.style('Digite seu nome de usuário', fg=typer.colors.GREEN)}")
            default_start(user)
        elif "6" in y["mode"]:
            user = typer.prompt(f"{typer.style('Digite seu nome de usuário', fg=typer.colors.GREEN)}")
            w6_start(user)
        elif "7" in y["mode"]:
            user = typer.prompt(f"{typer.style('Digite seu nome de usuário', fg=typer.colors.GREEN)}")
            w7_start(user)
        elif "8" in y["mode"]:
            user = typer.prompt(f"{typer.style('Digite seu nome de usuário', fg=typer.colors.GREEN)}")
            w8_start(user)
        elif "9" in y["mode"]:
            user = typer.prompt(f"{typer.style('Digite seu nome de usuário', fg=typer.colors.GREEN)}")
            w9_start(user)
        elif "10" in y["mode"]:
            user = typer.prompt(f"{typer.style('Digite seu nome de usuário', fg=typer.colors.GREEN)}")
            w10_start(user)
        elif "11" in y["mode"]:
            user = typer.prompt(f"{typer.style('Digite seu nome de usuário', fg=typer.colors.GREEN)}")
            w11_start(user)
        elif "12" in y["mode"]:
            user = typer.prompt(f"{typer.style('Digite seu nome de usuário', fg=typer.colors.GREEN)}")
            w12_start(user)
        elif "13" in y["mode"]:
            user = typer.prompt(f"{typer.style('Digite seu nome de usuário', fg=typer.colors.GREEN)}")
            w13_start(user)
        elif "14" in y["mode"]:
            user = typer.prompt(f"{typer.style('Digite seu nome de usuário', fg=typer.colors.GREEN)}")
            w14_start(user)

if __name__ == "__main__":
    typer.run(main)
