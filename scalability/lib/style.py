from colorama import Fore, Style
import sys

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