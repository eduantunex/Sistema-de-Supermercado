from colorama import Fore, Back, Style, init
import sqlite3 as sq
import os
import platform

clear = ""
sistema = platform.system()
if sistema == "Windows":
    clear = "cls"
elif sistema == "Darwin":  # macOS
    clear = "clear"
else:  # Linux ou outros
    clear = "clear"
    
init(autoreset=True)

def titulo():
    print(Fore.BLUE + """
          ____ _  _ ___ _  _ _  _ ____ ____    _  _ ____ ____ _  _ ____ ___
          |__| |\ |  |  |  | |\ | |___ [__     |\/| |__| |__/ |_/  |___  |
          |  | | \|  |  |__| | \| |___ ___]    |  | |  | |  \ | \_ |___  |
          
          """)

conn = sq.connect("database.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS produtos (valor REAL, nome TEXT, quantidade INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS vendas (valor REAL, nome TEXT, quantidade INTEGER, data TEXT, hora TEXT)")

def registrar_prod():
    os.system(clear)
    titulo()
    print(Fore.BLUE)