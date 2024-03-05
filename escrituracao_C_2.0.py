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
    print("") 

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
    
    escolha = input("Digite o môdulo desejado (ou 3 para sair): ")
    print("") 

    if escolha == "1":
        usuario_existente_1()
        print("Bem vindo(a) de volta!") # quando tiver com os dados e nome da empresa ou do mei fazer com a frase apareça "Bem vindop(a) NOME"
        print("") 
    
    elif escolha == "2":
        novo_usuario_2()
        # LOCAL DE CASDATRO
        print("________________________________________________________________________")
        print("|                                                                      |")
        print("|         Vamos seguir para o processo de cadastrar novo usuáriio.     |")
        print("|                                                                      |")
        print("|         Por favor, preeencha esses dados para dar continuidade.      |")
        print("|______________________________________________________________________|")
        print("")
        
        # NOME DA EMPRESA/MEI/USUARIO
        nome = input("Digite o nome da sua empresa/ou MEI: ")
        print("") 
        # CPF
        cpf = int(input("Digite o seu CPF: "))
        print("")  
        # CNPJ
        cnpj = int(input("Digite o seu cnpj: "))
        print("")
        # ENDEREÇO DE E-MAIL
        email = input("Digite o seu endereço de e-mail: ")
        print("")
        # TEL. PARA CONTATO(DA EMPRESA PREFERENCIALEMNTE) COM DDD
        telefone_empresa = int(input("Digite o número de telefone(da empresa preferencialmente) com DDD: "))
        print("")
        # ENDEREÇO DA EMPRESA
        endereco_empresa = input("Digite o endereço da empresa: ")
        print("")
        print("")
        print("Seus dados foram cadastrados com sucesso!")
        print("Dê uma conferida:")
        print("____________________________________________________________________________")
        print("| Nome da empresa")


    else:
        print("Encerrando o programa, até breve!")
        break #fim do While 1



# -------------------------------------------------------      
# PÓS ESSA PRIMEIRA PARTE  
# MODULOS
#   LIVRO DÍARIO
#   LIVRO RAZÃO
#   BALANCETE(OPCIONAL)
#   BALANÇO PATRIMÔNIAL
# FIM DO PRGRAMA