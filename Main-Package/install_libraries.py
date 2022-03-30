from os import system as command
from sys import platform

if platform == "linux" or platform == "linux2" or platform == "darwin":
    clear = "clear"
elif platform == "win32":
    clear = "cls"


command("pip install --upgrade pip")
command("pip install simple_chalk")

command(clear)