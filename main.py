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
import cliente # fazendo a importação do arquivo onde ficará as funções do cliente (modularizando)
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
 
print("Antes de prosseguir, por favor realize o login ou entre com um usuário existente.")
print()
print("CARREGANDO...")
print()
time.sleep(4) # espera (n) segundos até a mensagem de cima ser apagada para vir a posterior


# solicitar ao usuário que escolha um dos dois môdulos:
os.system('clear || cls')
print("|-----------------------------|")
print("| Escolha uma forma de Login: |")
print("|-----------------------------|")
print() 
print("1. Usuário Existente")
print("2. Usuário Novo")
print() 
    
modulo_escolha = int(input("Digite a forma de login desejada: "))
print() 
time.sleep(.3) 

if modulo_escolha == 1:
    cliente.usuario_existente_1()
    
else:
    cliente.novo_usuario_2()
        
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
    time.sleep(4)
    print()

    print(exemplos_modulos.exemplo_livro_diario())
    print("CARREGANDO EXEMPLO LIVRO RAZÃO...")
    time.sleep(4)
    print()

    print(exemplos_modulos.exemplo_livro_razao())
    print("CARREGANDO EXEMPLO BALANCETE...")
    time.sleep(4)
    print()

    print(exemplos_modulos.exemplo_balancete())
    print("CARREGANDO EXEMPLO BALANÇO PATRIMÔNIAL...")
    time.sleep(4)
    print()

    print(exemplos_modulos.exemplo_balanco_patrimonial())
    time.sleep(4)
    print()

    enter = input("APERTE ENTER PARA PROSSEGUIR")

else:
    print("CERTO, ENTÃO IRA SE INICIAR OS MÔDULOS PROPOSTOS LOGO EM CIMA")

print()
print("CARREGANDO 1º MÔDULO (LIVRO DIÁRIO)...")
time.sleep(5)

# execução dos môdulos referentes a escrituração:
time.sleep(.3)
funcoes_diario.livro_diario()
funcoes_razao.livro_razao() 



# em desenvolvimento...
ascii.em_dev()

# feito por Diêgo Axel
ascii.feito_por_diego_axel()

# FIM DO PRGRAMA
