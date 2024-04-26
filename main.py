############################################################
######          ESCRITURAÇÃO CONTÁBIL BÁSICA          ######
######               OBJETIVO: TREINAR                ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RM                    ######
############################################################

# imports:
import ascii 
import exemplos_modulos 
import livro_diario 
import datetime 
import os 
import time 

data = datetime.date.today() 

dia = data.day
mes = data.month
ano = data.year

# INICIO
os.system('clear || cls') # Se for Linux use "clear" e se for Windowns use "cls"
print(ascii.bem_vindo())
print()
print("CARREGANDO...")
time.sleep(2)
print()

os.system('clear || cls')
print("|------------------------------------------------|")
print("| Môdulos que iram ser executados (em sequência) |")
print("|------------------------------------------------|")
print() 
print("1. Livro Diário")
print("2. Livrro Razão")
print("3. Balancete (Opcional)")
print("4. Balanço Patrimônial")
print()

resp = input("VOCÊ DESEJA VER OS EXEMPLOS DE CADA UM DOS MÔDULOS? ")

resp = resp.upper()
dic = ["SIM", "S", "COM CERTEZA", "EU QUERO", "PODE SER", "CLARO", "CLARO QUE SIM", "OK", "TA", "TÁ"] 
if resp in dic:
    print()
    time.sleep(3)
    print()
    print(exemplos_modulos.exemplo_livro_diario())
    print("CARREGANDO EXEMPLO LIVRO RAZÃO...")
    time.sleep(3)
    print()
    print(exemplos_modulos.exemplo_livro_razao())
    print("CARREGANDO EXEMPLO BALANCETE...")
    time.sleep(3)
    print()
    print(exemplos_modulos.exemplo_balancete())
    print("CARREGANDO EXEMPLO BALANÇO PATRIMÔNIAL...")
    time.sleep(3)
    print()
    print(exemplos_modulos.exemplo_balanco_patrimonial())
    time.sleep(3)
    print()
    input("tecle <ENTER> para prosseguir...")
    print()    
else:
    print("INICIALIZANDO MÔDULOS.")
    print()

print("CARREGANDO 1º MÔDULO (LIVRO DIÁRIO)...")
time.sleep(3)

# execução dos môdulos referentes a escrituração:
time.sleep(.3)
print(livro_diario)
print()

# ASCII de desenvolvimento:
print(ascii.em_dev())

print("Programa encerrado, até breve.")