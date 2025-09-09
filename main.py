from colorama import Fore, Back, Style, init
import sqlite3 as sq
import os
import platform
import time
from funcs import clear, registrar_prod, remover_prod, adicionar_prod, view_prods

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

cursor.execute("CREATE TABLE IF NOT EXISTS produtos (nome TEXT, valor REAL, quantidade INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS vendas (nome TEXT, valor REAL, quantidade INTEGER, data TEXT, hora TEXT)")


while True:
    os.system(clear)
    titulo()
    print(Fore.BLUE + """Selecione uma opção:
          (1) Registrar uma Venda
          (2) Registrar Produto
          (3) Remover Estoque de um produto
          (4) Adicionar Estoque de um produto
          (5) Visualizar produtos""")
    prompt = input(">>> ")
    if prompt == "1":
        print(Fore.YELLOW + "Sem sucesso...")
        time.sleep(1)
    elif prompt == "2":
        registrar_prod()
    elif prompt == "3":
        remover_prod()
    elif prompt == "4":
        adicionar_prod()
    elif prompt == "5":
        view_prods()
    else:
        print(Fore.YELLOW + "Escreva uma opção correta...")
        time.sleep(1)