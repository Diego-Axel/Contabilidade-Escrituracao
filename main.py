############################################################
######          ESCRITURAÇÃO CONTÁBIL BÁSICA          ######
######               OBJETIVO: TREINAR                ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RM                    ######
############################################################

# OBS: Estou refazendo... Motivos? -> Posso melhorar

# imports
import clientes # fazendo importação do arquivo onde ficará as funções do CLIENTE (modularizando)
import funcoes # fazendoimportação do arquivo onde ficará as funções (modularizando)
import datetime # biblioteca para puxar a data do computador

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
while True < 3:
    # solicitar ao usuário que escolha um dos dois môdulos:
    print("|--------------------|")
    print("| Escolha um môdulo: |")
    print("|--------------------|")
    print("") 
    print("1. Usuário Existente")
    print("2. Usuário Novo")
    print("3. Sair")
    print("") 
    
    escolha = int(input("Digite o môdulo desejado (ou 3 para sair): "))
    print("") 

    if escolha == 1:
        clientes.usuario_existente_1()
        break 
    
    elif escolha == 2:
        clientes.novo_usuario_2()
        break

    else:
        print("Encerrando o programa, até breve!")
        break 

# PÓS ESSA PRIMEIRA PARTE
    
print("")

# começo do while 2 
while True < 5:
    # solicitar ao usuário que escolha um dos dois môdulos:
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
        funcoes.livro_diario_1()
    
    elif escolha_2 == 2:
        funcoes.livro_razao_2()
    
    elif escolha_2 == 3:
        funcoes.balancete_3()
    
    elif escolha_2 == 4:
        funcoes.balanco_patrimonial_4()
        
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