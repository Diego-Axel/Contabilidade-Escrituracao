############################################################
######          ESCRITURAÇÃO CONTÁBIL BÁSICA          ######
######               OBJETIVO: TREINAR                ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RM                    ######
############################################################

# OBS: Estou refazendo... Motivos? -> Posso melhorar

# imports:
import cliente # fazendo a importação do arquivo onde ficará as funções do cliente (modularizando)
import funcoes_diario # fazendo a importação do arquivo onde ficará as funções do diário (modularizando)
import funcoes_razao # fazendo a importação do arquivo onde ficará as funções do razão (modularizando)
import datetime # biblioteca para puxar a data do computador
import os # biblioteca para interagir com o sistema operacional, estou usando para que tudo que esteja acima dela, seja limpo(console ou terminal). fica mais "limpo" de se vizualizar
import time # da um tempo para as informações sumirem -> time.sleep(o segundo que você quiser aqui quendo dos parenteses)

data = datetime.date.today()

dia = data.day
mes = data.month
ano = data.year

# INICIO
os.system('clear || cls') # limpar a tela do console ou terminal, tanto em sistema operacional Windows quanto em Linux

print("""
    ________________________________________________________________________________________________________________
    |  .______    _______ .___  ___.    ____    ____  __  .__   __.  _______    ______     ___     ___      ___    | 
    |  |   _  \  |   ____||   \/   |    \   \  /   / |  | |  \ |  | |       \  /  __  \   /  /    /   \     \  \   | 
    |  |  |_)  | |  |__   |  \  /  |     \   \/   /  |  | |   \|  | |  .--.  ||  |  |  | |  |    /  ^  \     |  |  | 
    |  |   _  <  |   __|  |  |\/|  |      \      /   |  | |  . `  | |  |  |  ||  |  |  | |  |   /  /_\  \    |  |  | 
    |  |  |_)  | |  |____ |  |  |  |       \    /    |  | |  |\   | |  '--'  ||  `--'  | |  |  /  _____  \   |  |  | 
    |  |______/  |_______||__|  |__|        \__/     |__| |__| \__| |_______/  \______/  |  | /__/     \__\  |  |  | 
    |                                                                                     \__\              /__/   | 
    |______________________________________________________________________________________________________________|
      
""")
 
print("") # espaços para evitar ficar colado
print("Antes de prosseguir, por favor insira qual môdulo você quer escolher: ")
print("")
print("CARREGANDO...")
print("")
time.sleep(4) # espera (n) segundos até a mensagem de cima ser apagada para vir a posterior

# começo do While 1:
client_modulo = True
while True < 3:
    # solicitar ao usuário que escolha um dos dois môdulos:
    os.system('clear || cls')
    print("|--------------------|")
    print("| Escolha um môdulo: |")
    print("|--------------------|")
    print("") 
    print("1. Usuário Existente")
    print("2. Usuário Novo")
    print("") 
    
    escolha = int(input("Digite o môdulo desejado: "))
    print("") 
    time.sleep(.3) 

    if escolha == 1:
        cliente.usuario_existente_1()
        break 
    
    elif escolha == 2:
        cliente.novo_usuario_2()
        break

    else:
        print("Não foi colocado o que se pede.") 

print("")


os.system('clear || cls')
print("|------------------------------------------------|")
print("| Môdulos que iram ser executados (em sequência) |")
print("|------------------------------------------------|")
print("") 
print("1. Livro Diário")
print("2. Livrro Razão")
print("3. Balancete (Opcional)")
print("4. Balanço Patrimônial")
print("")
print("")
print("CARREGANDO...")
print("")
time.sleep(8)

print("Eis o modelo de cada um dos passos apresentados:")
print("""











    """)

os.system('clear || cls')

# execução dos môdulos referentes a escrituração:
print(funcoes_diario.livro_diario()) 
print(funcoes_razao.livro_razao()) 



# em desenvolvimento...
print("""

     _______ .___  ___.     _______   _______ ____    ____             
    |   ____||   \/   |    |       \ |   ____|\   \  /   /             
    |  |__   |  \  /  |    |  .--.  ||  |__    \   \/   /              
    |   __|  |  |\/|  |    |  |  |  ||   __|    \      /               
    |  |____ |  |  |  |    |  '--'  ||  |____    \    /     __  __  __ 
    |_______||__|  |__|    |_______/ |_______|    \__/     (__)(__)(__)


""")



print("""

     _______  _______  __  .___________.  ______      .______     ______   .______         
    |   ____||   ____||  | |           | /  __  \     |   _  \   /  __  \  |   _  \      _ 
    |  |__   |  |__   |  | `---|  |----`|  |  |  |    |  |_)  | |  |  |  | |  |_)  |    (_)
    |   __|  |   __|  |  |     |  |     |  |  |  |    |   ___/  |  |  |  | |      /        
    |  |     |  |____ |  |     |  |     |  `--'  |    |  |      |  `--'  | |  |\  \----. _ 
    |__|     |_______||__|     |__|      \______/     | _|       \______/  | _| `._____|(_)
      
     _______   __   _______   _______   ______           ___      ___   ___  _______  __      
    |       \ |  | |   ____| /  _____| /  __  \         /   \     \  \ /  / |   ____||  |     
    |  .--.  ||  | |  |__   |  |  __  |  |  |  |       /  ^  \     \  V  /  |  |__   |  |     
    |  |  |  ||  | |   __|  |  | |_ | |  |  |  |      /  /_\  \     >   <   |   __|  |  |     
    |  '--'  ||  | |  |____ |  |__| | |  `--'  |     /  _____  \   /  .  \  |  |____ |  `----.
    |_______/ |__| |_______| \______|  \______/     /__/     \__\ /__/ \__\ |_______||_______|

      
""")


# FIM DO PRGRAMA