############################################################
######          ESCRITURAÇÃO CONTÁBIL BÁSICA          ######
######               OBJETIVO: TREINAR                ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RM                    ######
############################################################

# OBS: Estou refazendo... Motivos? -> Posso melhorar

# imports
import datetime

data = datetime.date.today()

dia = data.day
mes = data.month
ano = data.year

# o que é importante em uma escrituração contábil? o que deve conter, se tratando da básica... ->
# em ordem seria..
# se tratando de um sistema completo, seria: 

# INICIO
print("|-------------------|")
print("|---- Bem vindo ----|")
print("|-------------------|")
print("") # espaços para evitar ficar colado
print("Antes de prosseguir, por favor insira qual môdulo você quer escolher: ")
print("") # espaços

# MODOLOS

# USUARIO EXISTENTE
def usuario_existente_1():
    print("|---------------------------------|")
    print("| Você escolheu Usuário Existente |")
    print("|---------------------------------|")
    print("") # espaços
# NOVO USUAIRO
def novo_usuario_2():
    print("|---------------------------------|")
    print("|   Você escolheu Novo Usuário    |")
    print("|---------------------------------|")
    print("") # espaços

# começo do While 1:
while True < 3:
    # solicitar ao usuário que escolha um dos dois môdulos:
    print("|--------------------|")
    print("| Escolha um môdulo: |")
    print("|--------------------|")
    print("") # espaços
    print("1. Usuário Existente")
    print("2. Usuário Novo")
    print("3. Sair")
    print("") # espaços
    
    escolha = input("Digite o môdulo desejado (ou 3 para sair): ")
    print("") #espaços

    if escolha == "1":
        usuario_existente_1()
        print("Bem vindo(a) de volta!")
        print("") #espaços
    
    elif escolha == "2":
        novo_usuario_2()
        # LOCAL DE CASDATRO
        print("________________________________________________________________________")
        print("|                                                                      |")
        print("|         Vamos seguir para o processo de cadastrar novo usuáriio.     |")
        print("|                                                                      |")
        print("|         Por favor, preeencha esses dados para dar continuidade.      |")
        print("|______________________________________________________________________|")
        
        # NOME DA EMPRESA/MEI/USUARIO
        nome = input("Digite o nome da sua empresa/ou MEI: ")
        print("") # espaços
        # CPF
        cpf = input("Digite o seu CPF: ")
        print("") # espaços 
        # CNPJ
        cnpj = input("Digite o seu cnpj: ")
        print("")
        print("seu CPS: %s    |  Seu CNPJ %d   "%(cpf,cnpj))


    else:
        print("Encerrando o programa, até breve!")
        break #fim do While 1







# ENDEREÇO DE E-MAIL
# TEL. PARA CONTATO(DA EMPRESA PREFERENCIALEMNTE) COM DDD
# ENDEREÇO DA EMPRESA
# -------------------------------------------------------      
# PÓS ESSA PRIMEIRA PARTE  
# MODULOS
#   LIVRO DÍARIO
#   LIVRO RAZÃO
#   BALANCETE(OPCIONAL)
#   BALANÇO PATRIMÔNIAL
# FIM DO PRGRAMA