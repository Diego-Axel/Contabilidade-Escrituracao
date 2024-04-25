############################################################
######          ESCRITURAÇÃO CONTÁBIL BÁSICA          ######
######               OBJETIVO: TREINAR                ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RM                    ######
############################################################

# OBS: Estou refazendo... Motivos? -> Posso melhorar
# Em desenvolvimento :)

# imports:
import ascii # importação do meu arquivo com so ASCII
import exemplos_modulos # importação do arquivo que contém os exemplos de cada môdulo
import funcoes_diario # fazendo a importação do arquivo onde ficará as funções do diário (modularizando)
import funcoes_razao # fazendo a importação do arquivo onde ficará as funções do razão (modularizando)
import datetime # biblioteca para puxar a data do computador
import os # biblioteca para interagir com o sistema operacional, estou usando para que tudo que esteja acima dela, seja limpo(console ou terminal). fica mais "limpo" de se vizualizar
import time # da um tempo para as informações sumirem -> time.sleep(o segundo que você quiser aqui quendo dos parenteses)

data = datetime.date.today() # data do dispositivo

dia = data.day
mes = data.month
ano = data.year

# INICIO
os.system('clear || cls') # limpar a tela do console ou terminal, tanto em sistema operacional Windows quanto em Linux

ascii.bem_vindo()
print()
print("CARREGANDO...")
print()
time.sleep(2) # espera (n) segundos até a mensagem de cima ser apagada para vir a posterior
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
print()
resp = resp.upper()
dic = ["SIM", "S", "COM CERTEZA", "EU QUERO", "PODE SER", "CLARO", "CLARO QUE SIM", "OK", "TA", "TÁ"] 

if resp in dic:

    print("OBS: OS NOMES E VALORES SÃO APENAS PARA FINS DE EXEMPLO.")
    time.sleep(3)
    print()

    exemplos_modulos.exemplo_livro_diario()
    print("CARREGANDO EXEMPLO LIVRO RAZÃO...")
    time.sleep(3)
    print()

    exemplos_modulos.exemplo_livro_razao()
    print("CARREGANDO EXEMPLO BALANCETE...")
    time.sleep(3)
    print()

    exemplos_modulos.exemplo_balancete()
    print("CARREGANDO EXEMPLO BALANÇO PATRIMÔNIAL...")
    time.sleep(3)
    print()

    exemplos_modulos.exemplo_balanco_patrimonial()
    time.sleep(3)
    print()

    input("tecle <ENTER> para prosseguir...")

else:
    print("INICIALIZANDO MÔDULOS.")

print()
print("CARREGANDO 1º MÔDULO (LIVRO DIÁRIO)...")
time.sleep(3)

# execução dos môdulos referentes a escrituração:
time.sleep(.3)
funcoes_diario.livro_diario()
funcoes_razao.livro_razao() 

# em desenvolvimento...
ascii.em_dev()

# FIM DO PRGRAMA
print("Programa encerrado, até breve.")