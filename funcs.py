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

def registrar_prod():
    os.system(clear)
    titulo()
    
    while True:
        os.system(clear)
        titulo()
        print(Fore.BLUE + "Digite o nome do produto que tenha no max 25 caracteres (digite 0 para sair):")
        nome_produto = input(">>> ")
        db_nome = cursor.execute("SELECT nome FROM produtos WHERE nome = ?", (nome_produto,)).fetchone()
        if db_nome:
            print(Fore.YELLOW + "Este produto ja está registrado!")
            time.sleep(1)
        elif nome_produto == "0":
            return
        elif len(nome_produto) > 25:
            print(Fore.YELLOW + "No máximo 25 caracteres!")
            time.sleep(1)
        else:
            break
    def try_valorproduto():
        os.system(clear)
        titulo()
        print(Fore.BLUE + "Digite o valor do produto (digite 0 para sair):")
        while True:
            try:
                valor_produto = float(input(">>> "))
                if valor_produto == 0:
                    return
                else:
                    return valor_produto
            except:
                print(Fore.YELLOW + "Você deve digitar um NUMERO")
                time.sleep(1)
    def try_estoqueproduto():
        os.system(clear)
        titulo()
        print(Fore.BLUE + "Digite a quantidade em estoque (digite 0 para sair):")
        while True:
            try:
                estoque_produto = int(input(">>>"))
                if estoque_produto == 0:
                    return
                return estoque_produto
            except:
                print(Fore.YELLOW + "Você deve digitar um NUMERO")
                time.sleep(1)
    estoque_produto = try_estoqueproduto()

    cursor.execute("INSERT INTO produtos (valor, nome, quantidade) VALUES (?,?,?)", (try_valorproduto(), nome_produto, estoque_produto,))
    conn.commit()

def remover_prod():
    
    os.system(clear)
    titulo()
    print(Fore.BLUE + "Digite o nome do produto que você deseja remover estoque (digite 0 para sair):")
    in_nome = input(">>> ")
    db_qtd = cursor.execute("SELECT quantidade FROM produtos WHERE nome = ?", (in_nome,)).fetchone()
    db_nome = cursor.execute("SELECT nome FROM produtos WHERE nome = ?", (in_nome,)).fetchone()
    if in_nome == "0":
        return
    if not db_nome:
        os.system(clear)
        titulo()
        print(Fore.YELLOW + "Este produto não está em seu banco de dados (Verifique se ele está registrado).")
        time.sleep(2)
        return
    def try_qtdproduto():
        os.system(clear)
        titulo()
        print(Fore.BLUE + "Digite a quantidade do produto que você deseja remover estoque (digite 0 para sair):")
        try:
            qtd_produto = int(input(">>> "))
            if qtd_produto == 0:
                return
            if qtd_produto > db_qtd[0]:
                print(Fore.YELLOW + "Você deve inserir um numero menor ou igual ao seu estoque para remover!")
                time.sleep(2)
                try_qtdproduto()
            print(Fore.GREEN + ("Estoque modificado com sucesso!"))
            time.sleep(1)
            return qtd_produto
        except:
            os.system(clear)
            titulo()
            print(Fore.YELLOW + "Você deve digitar um NUMERO correto!")
            time.sleep(1)
            try_qtdproduto()
    cursor.execute("UPDATE produtos SET quantidade = ? WHERE nome = ?", (db_qtd[0]-try_qtdproduto(), in_nome,))
    conn.commit()

def adicionar_prod():

    
    os.system(clear)
    titulo()
    print(Fore.BLUE + "Digite o nome do produto que você deseja adicionar estoque (digite 0 para sair):")
    in_nome = input(">>> ")
    db_qtd = cursor.execute("SELECT quantidade FROM produtos WHERE nome = ?", (in_nome,)).fetchone()
    db_nome = cursor.execute("SELECT nome FROM produtos WHERE nome = ?", (in_nome,)).fetchone()
    if in_nome == "0":
        return
    if not db_nome:
        os.system(clear)
        titulo()
        print(Fore.YELLOW + "Este produto não está em seu banco de dados (Verifique se ele está registrado).")
        time.sleep(2)
        return
    def try_qtdproduto():
        os.system(clear)
        titulo()
        print(Fore.BLUE + "Digite a quantidade do produto que você deseja adicionar estoque (digite 0 para sair):")
        try:
            qtd_produto = int(input(">>> "))
            if qtd_produto == 0:
                return
            if qtd_produto < 0:
                print(Fore.YELLOW + "Você deve inserir um numero maior que zero!")
                time.sleep(2)
                try_qtdproduto()
            print(Fore.GREEN + ("Estoque modificado com sucesso!"))
            time.sleep(1)
            return qtd_produto
        except:
            os.system(clear)
            titulo()
            print(Fore.YELLOW + "Você deve digitar um NUMERO correto!")
            time.sleep(1)
            try_qtdproduto()
    cursor.execute("UPDATE produtos SET quantidade = ? WHERE nome = ?", (db_qtd[0]+try_qtdproduto(), in_nome,))
    conn.commit()

def view_prods():
    os.system(clear)
    titulo()
    db = cursor.execute("SELECT nome, quantidade, valor FROM produtos").fetchall()
    if not db:
        print(Fore.YELLOW + "Você não tem produtos registrados no seu banco de dados!")
        time.sleep(1)
        return
    print(Fore.BLUE + "- Seus Produtos (digite 0 para sair):\n")
    print(Fore.GREEN + f'{"NOME":<30} || {"VALOR":<15} || {"QUANTIDADE":<10}')
    print(Fore.GREEN + "-"*65)
    for nome, quantidade, valor in db:
        print(Fore.GREEN + f"{nome:<30} || {valor:<15} || {quantidade:<10}")
    prompt = input(">>> ")
    if prompt == "0":
        return

def reg_venda():
    while True:
        os.system(clear)
        titulo()
        print(Fore.BLUE + "Digite um nome do produto que deseja vender:")
        in_produto = input(">>> ")
        db_produto = cursor.execute("SELECT nome FROM produtos WHERE nome = ?", (in_produto,)).fetchone()
        if not db_produto:
            os.system(clear)
            titulo()
            print(Fore.YELLOW + "Este produto não existe!")
            time.sleep(1)
        else:
            break
    while True:
        print(Fore.BLUE + "Digite a quantidade vendida:")
        in_quantidade = int(input(">>> "))
        db_quantidade = cursor.execute("SELECT quantidade FROM produtos WHERE nome = ?", (in_produto,)).fetchone()
        if db_quantidade[0] < in_quantidade:
            os.system(clear)
            titulo()
            print(Fore.YELLOW + "Você não tem isso de estoque!!")
            time.sleep(1)
        elif in_quantidade < 1:
            os.system(clear)
            titulo()
            print(Fore.YELLOW + "Insira um valor acima de 0!")
            time.sleep(1)
        else:
            break
    while True:
        print(Fore.BLUE + "Digite o valor que você vendeu cada produto:")
        in_valorun = input(">>> ")
        if in_valorun < 0:
            os.system(clear)
            titulo()
            print(Fore.YELLOW + "Digite um valor igual ou acima de 0!")
            time.sleep(1)
        else:
            break
    data = time.strftime("%d/%m/%Y")
    hora = time.strftime("%H:%M:%S")
    valor_total = in_quantidade*in_valorun
    cursor.execute("INSERT INTO vendas (nome, quantidade, valor, data, hora) VALUES (?,?,?,?,?)", (in_produto, in_quantidade, valor_total, data, hora,))
    conn.commit()

def view_vendas():
    os.system(clear)
    titulo()
    db_ = cursor.execute("SELECT nome, quantidade, valor, data, hora FROM vendas").fetchone()
    if not db_:
        os.system(clear)
        titulo()
        print(Fore.YELLOW + "Você não tem vendas registradas!")
        time.sleep(1)
    else:
        os.system(clear)
        titulo()
        print(Fore.BLUE(f"{"NOME":<30}|| {"QTD":<10}|| {"VALOR UNIDADE":<10}|| {"VALOR TOTAL":<10}|| {"DATA":<10}|| {"HORA":<6}"))
        for nome, quantidade, valor, data, hora in db_:
            print(Fore.BLUE + f"{nome:<30}|| {quantidade:<10}|| {"R$"+valor/quantidade:<10}|| {"R$"+valor:<10}|| {data:<10}|| {hora:<6}")
        prompt = input(">>>")