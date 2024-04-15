############################################################
######          ESCRITURAÇÃO CONTÁBIL BÁSICA          ######
######               OBJETIVO: TREINAR                ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RM                    ######
############################################################

# OBS: Estou refazendo... Motivos? -> Posso melhorar
# Em desenvolvimento :)

# imports:
import ascii
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

print(ascii.bem_vindo())
 
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
print()
print("CARREGANDO...")
print()
time.sleep(7)
os.system('clear || cls')

print("Embaixo está os modelos de cada um dos passos apresentados:\nOBS: OS NOMES E QUANTIDADES SÃO APENAS EXEMPLOS!")
time.sleep(5)
os.system('clear || cls')


print("""
      
            |         LIVRO DIÁRIO          |
      
      data da operação: xx/xx/xxxx
      D - xxxx - R$ xx.xxx,xx
      C - xxxx - R$ xx.xxx,xx
      histórico: xxxxxxxxxxxx
      (Pode ter mais de uma conta de débito e crédito.)

    
    CARREGANDO EXEMPLO LIVRO RAZÃO...
          
    """)
time.sleep(4)
os.system('clear || cls')

print("""

        |         LIVRO RAZÃO           |
    
    _________________CAIXA___________________
      R$ xx.xxx,xx     |     R$ xx.xxx,xx
                       |
                       |
                       |
                       |
    ______TOTAL________|_________TOTAL________
      

    CARREGANDO EXEMPLO BALANCETE...

    """)
time.sleep(4)
os.system('clear || cls')

print("""

             |       BALANCETE(OPCIONAL)       |
    
    ____________________________________________________
    |     CONTAS     |              SALDOS             |
    |________________|_____Débtios____|____Créditos____|
    |     Caixa      | R$ xx.xxxx,xx  |                |
    |     Banco      | R$ xx.xxxx,xx  |                |
    |   Fornecedor   |                | R$ xx.xxxx,xx  |
    |    Estoques    | R$ xx.xxxx,xx  |                | 
    |    Veículos    | R$ xx.xxxx,xx  |                |
    | Contas a pagar |                | R$ xx.xxxx,xx  |
    |________________|________________|________________|
    |______TOTAL_____|________________|_____ TOTAL_____|
    |__R$_xx.xxx,xx__|________=_______|__R$_xx.xxx,xx__|
    |________________|________________|________________|
      
    
    CARREGANDO EXEMPLO BALANÇO PATRIMÔNIAL...

    """)
time.sleep(4)
os.system('clear || cls')

print("""

            |       BALANÇO PATRIMÔNIAL       |
    ____________________________________________________
    |        ATIVOS         |         PASSIVOS         |
    |_______________________|__________________________|
    |  Caixa R$ xx.xxx,xx   |  Fornecedor R$ xx.xxx,xx |
    |  Banco R$ xx.xxx,xx   | Conta/pagar R$ xx.xxx,xx |
    | Estoques R$ xx.xxx,xx |                          |
    | Veículos R$ xx.xxx,xx |                          |
    |_______________________|__________________________|
    |                       |    PATRIMÔNIO LÍQUIDO    |
    |_______________________|__________________________|
    |                       | Cap.Social  R$ xx.xxx,xx |
    |                       |                          |
    |_______________________|__________________________|
    |___TOTAL ATIVOS (R$)___|___TOTAL PASSIVOS + PL____|
    |_______________________|__________________________|
      
    
    CARREGANDO 1º MÔDULO (LIVRO DIÁRIO)...

    """)
time.sleep(4)
os.system('clear || cls')

# execução dos môdulos referentes a escrituração:
time.sleep(.3)
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
