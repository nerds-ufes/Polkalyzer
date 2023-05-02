from colorama import Fore, Style
from alive_progress import alive_bar
import sys
import time

def compute():
    for i in range(1000):
        yield

def checkpoint(string):
    print(Fore.YELLOW + string + " . . ." +Style.RESET_ALL)
    sys.stdout.flush()

def checkpointDone(string):
    print(Fore.YELLOW + string + Fore.GREEN + " \u2713" + Style.RESET_ALL + '\n')
    sys.stdout.flush()

def success():
    print(Fore.YELLOW + "Success" + Fore.GREEN + " \u2713" + Style.RESET_ALL + '\n')
    sys.stdout.flush()

def done():
    print(Fore.YELLOW + "Done" + Fore.GREEN + " \u2713" + Style.RESET_ALL + '\n')
    sys.stdout.flush()

def colorful_print(string, color):
    print(Fore.YELLOW + "Done" + Fore.GREEN + " \u2713" + Style.RESET_ALL + '\n')
    sys.stdout.flush()

def colorful_print(string, color):
    print(getattr(Fore, color.upper()) + string + Style.RESET_ALL)
    sys.stdout.flush()

def print_colorfulDict(dictName,d, color):
    colorfulString = getattr(Fore, color.upper()) + f"{dictName}: " + Style.RESET_ALL + "| "
    for k in d.keys():
        colorfulString += getattr(Fore, color.upper()) + str(k) + Style.RESET_ALL + " = " + str(d[k]) + " | "
    sys.stdout.flush()
    print(colorfulString)

def greetings():
    print("==> Polkalyzer finished with SUCCESS !!!\n")
    colorful_print("==> Contribute with us giving this repo a Star ⭐", color="yellow")
    colorful_print("Owner:",color="yellow")
    print("\t - NERDS (Núcleo de Estudos em Redes Definidas por Software)     | @nerds-ufes")
    colorful_print("Maintainers:",color="yellow")
    print("\t - Lucas R. de Almeida      |    Email: contato@propi.dev        | @propilideno")
    print("\t - Rodolfo S. Villaca       |    Email: rodolfo.villaca@ufes.br  | @rodolfovillaca")
