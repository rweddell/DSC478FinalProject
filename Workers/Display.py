
import sys
import os

from colorama import init

# strip colors if stdout is redirected
init(strip=not sys.stdout.isatty())

from termcolor import cprint
from pyfiglet import figlet_format


def display_title(title):
    """
    Displays title in 'starwars' font
    :param title: string: title of program
    :return: None
    """
    cprint(figlet_format(
        title,
        font='starwars'),
        attrs=['blink'])


def cls():
    """
    Clears the console when called from shell/console
    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')
