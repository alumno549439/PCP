import random, emoji
from colorama import Fore, Style

colores = {
    "R": (emoji.emojize(":red_circle:"), Fore.RED),
    "V": (emoji.emojize(":green_circle:"), Fore.GREEN),
    "A": (emoji.emojize(":yellow_circle:"), Fore.YELLOW),
    "Z": (emoji.emojize(":blue_circle:"), Fore.BLUE),
    "M": (emoji.emojize(":purple_circle:"), Fore.MAGENTA),
    "B": (emoji.emojize(":white_circle:"), Fore.WHITE),
    "N": (emoji.emojize(":black_circle:"), Fore.BLACK)
}

def codigoSecreto():
    coloressecretos = random.choices(list(colores.values()), k=4)

    print(
        coloressecretos[0][1] + coloressecretos[0][0] + " " +
        coloressecretos[1][1] + coloressecretos[1][0] + " " +
        coloressecretos[2][1] + coloressecretos[2][0] + " " +
        coloressecretos[3][1] + coloressecretos[3][0] +
        Style.RESET_ALL
    )

def inicio():
    print("Bienvenido a Mastermind")