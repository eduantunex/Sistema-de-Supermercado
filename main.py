from colorama import Fore, Back, Style, init
import sqlite3 as sq
import os
import platform
import time

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
    print(Fore.BLUE + "Digite o nome do produto:")
    nome_produto = input(">>> ")
    def try_valorproduto():
        os.system(clear)
        titulo()
        print(Fore.BLUE + "Digite o valor do produto:")
        try:
            valor_produto = float(input(">>> "))
        except:
            print(Fore.YELLOW + "Você deve digitar um NUMERO")
            time.sleep(1)
            try_valorproduto()
        return valor_produto
    valor_produto = try_valorproduto()
    def try_estoqueproduto():
        os.system(clear)
        titulo()
        print(Fore.BLUE + "Digite a quantidade em estoque:")
        try:
            estoque_produto = float(input(">>>"))
            return estoque_produto
        except:
            print(Fore.YELLOW + "Você deve digitar um NUMERO")
            time.sleep(1)
            try_estoqueproduto()
    estoque_produto = try_estoqueproduto()

    cursor.execute("INSERT INTO produtos (valor, nome, quantidade) VALUES (?,?,?)", (valor_produto, nome_produto, estoque_produto))
    conn.commit()


while True:
    os.system(clear)
    titulo()
    print(Fore.BLUE + """Selecione uma opção:
          (1) Registrar uma Venda
          (2) Ver Produtos
          (3) Ver Clientes""")
    prompt = input(">>> ")
    if prompt == "1":
        print(Fore.YELLOW + "Sem sucesso...")
        time.sleep(1)
    elif prompt == "2":
        print(Fore.YELLOW + "Sem sucesso...")
        time.sleep(1)
    elif prompt == "3":
        print(Fore.YELLOW + "Sem sucesso...")
        time.sleep(1)
    else:
        print(Fore.YELLOW + "Escreva uma opção correta...")
        time.sleep(1)