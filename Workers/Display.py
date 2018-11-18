
import sys
import os

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def pil_display(title):
    myfont = ImageFont.truetype("verdanab.ttf", 8)
    size = myfont.getsize(title)
    img = Image.new('1', size, "black")
    draw = ImageDraw.Draw(img)
    draw.text((0,0), title, "green", font=myfont)
    pixels = np.array(img, dtype=np.uint8)
    chars = np.array([' ', '#'], dtype="U1")[pixels]
    strings = chars.view('U' + str(chars.shape[1])).flatten()
    print('\n'.join(strings))


def display_title(title):
    cprint(figlet_format(
        title,
        font='starwars'),
        'green',
        attrs=['bold', 'blink'])


def cls():
    # clears the console when called from shell/console
    os.system('cls' if os.name == 'nt' else 'clear')



pil_display('TESTING 1, 2, 3')

display_title('TESTING 1, 2, 3')