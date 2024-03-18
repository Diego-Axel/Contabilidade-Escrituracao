############################################################
######          ESCRITURAÇÃO CONTÁBIL BÁSICA          ######
######               OBJETIVO: TREINAR                ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RM                    ######
############################################################

# OBS: Estou refazendo... Motivos? -> Posso melhorar

# imports
import cliente # fazendo importação do arquivo onde ficará as funções do CLIENTE (modularizando)
import funcoes_diario # fazendoimportação do arquivo onde ficará as funções (modularizando)
import datetime # biblioteca para puxar a data do computador
import os 

data = datetime.date.today()

dia = data.day
mes = data.month
ano = data.year

# o que é importante em uma escrituração contábil? o que deve conter, se tratando da básica... ->
# em ordem seria..
# se tratando de um sistema completo, seria: 

# INICIO

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
print("") # espaços

# começo do While 1:
client = True
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

    if escolha == 1:
        cliente.usuario_existente_1()
        break 
    
    elif escolha == 2:
        cliente.novo_usuario_2()
        break

    else:
        print("") 

print("")

# começo do while 2 
escolh = True
while True < 5:
    # solicitar ao usuário que escolha um dos dois môdulos:
    os.system('clear || cls')
    print("|--------------------|")
    print("| Escolha um môdulo: |")
    print("|--------------------|")
    print("") 
    print("1. Livro Diário")
    print("2. Livrro Razão")
    print("3. Balancete")
    print("4. Balanço Patrimônial")
    print("5. Sair") 
    print("")

    escolha_2 = int(input("Digite o môdulo desejado (ou 5 para sair): "))
    print("")

    if escolha_2 == 1:
        funcoes_diario.livro_diario_1()
    
    elif escolha_2 == 2:
        print("") # usarei depois...
    
    elif escolha_2 == 3:
        print("") # usarei depois...
    
    elif escolha_2 == 4:
        print("") # usarei depois...

    else:
        print("Encerrando o programa, até breve!")
        break 


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