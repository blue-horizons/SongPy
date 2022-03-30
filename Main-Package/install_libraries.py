import os
from sys import platform

if platform == "linux" or platform == "linux2" or platform == "darwin":
    clear = "clear"
elif platform == "win32":
    clear = "cls"


os.system("pip install --upgrade pip")
os.system("pip install colourpy")

os.system(clear)