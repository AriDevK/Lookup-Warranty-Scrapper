import os
import sys

def clear():
    if sys.platform.startswith('win32'):
        os.system('cls')
    else:
        os.system('clear')
