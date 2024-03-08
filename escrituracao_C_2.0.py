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
        break 
    
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
        nome_empresa = input("Digite o nome da sua empresa/ou MEI: ")
        print("") 
        # CPF
        cpf = input("Digite o seu CPF: ")
        print("")  
        # CNPJ
        cnpj = input("Digite o seu cnpj: ")
        print("")
        # ENDEREÇO DE E-MAIL
        email = input("Digite o seu endereço de e-mail: ")
        print("")
        # TEL. PARA CONTATO(DA EMPRESA PREFERENCIALEMNTE) COM DDD
        telefone_empresa = input("Digite o número de telefone(da empresa preferencialmente) com DDD: ")
        print("")
        # ENDEREÇO DA EMPRESA
        endereco_empresa = input("Digite o endereço da empresa: ")
        print("")
        print("")
        print("Seus dados foram cadastrados com sucesso!")
        print("Dê uma conferida:")
        print("")
        # mostrnado os daods que o usuário introduziu no programa:
        print(" _________________________________________________")
        print("                                                  ")
        print("             Nome da empresa/ou MEI: %s           "%nome_empresa)
        print("                     CPF: %s                      "%cpf)
        print("                     CNPJ: %s                     "%cnpj)
        print("                     E-mail: %s                   "%email)
        print("              Telefone da Empresa: %s             "%telefone_empresa)
        print("              Endereço da Empresa: %s             "%endereco_empresa)
        print("__________________________________________________")
        break

    else:
        print("Encerrando o programa, até breve!")
        break 

# PÓS ESSA PRIMEIRA PARTE
    
print("")
print("")

# LIVRO DIÁRIO
def livro_diario_1():
    print("_______________________")
    print("|                     |")
    print("|    LIVRO DIÁRIO     |")
    print("|_____________________|")
    print("")
    # PEDIR O NÚMERO DE OPERAÇÕES
    numero_operacoes = int(input("Digite quantas operações você deseja realizar(1,2,3...): "))
    print("")

    # CONDICIONAIS DOS NÚMEROS DE OPERAÇÕES:
    if numero_operacoes == 1:
        print("""  
        ______________________
        |                    |
        |     1 OPERAÇÃO     |
        |____________________|
              
        """)
        numero_contas = int(input("Digite o número de contas que você deseja ter nesta operação(LEMBRE-SE, INICIALMENTE VOCÊ TEM UMA CONTA DE DÉBITO(D) E UMA DE CRÉDITO(C) POR PADRÃO -> ESCOLHA ADICIONAR 1,2,3 -> VOCÊ JA COMEÇA COM 2(D,C)):"))

        # CONDICIONAIS DOS NÚMEROS DE CONTAS (OPERAÇÃO = 1)
        if numero_contas == 0:
            print("")
            
        elif numero_contas == 1:
            print("Você escolheu adiconar 1 conta.")
            print("")
            print("Como havia falado anteriormeente, você você JA POSSUI duas contas 1 DE DÉBITO E 1 DE CRÉDITO.")
            print("") # ESPAÇOS

            tipo_conta = input("Qual o tipo da conta você deseja adicionar(D ou C):? ")
            if tipo_conta == "Débito" or "Debtio" or "débito" or "debito" or "D" or "d":
                print("Você escolheu adiconar uma conta ao tipo DÉBITO:")
                print("")

                conta_D_main = input("Digite o nome da sua PRIMERIA CONTA de Débito: ")
                valor_D_main = float(input("Digite o valor(R$) dessa respectiva conta: "))
                print("__________________________________________________________________")

                conta_D1 = input("Digite o valor da sua SEGUNDA CONTA DE DÉBITO: ")
                valor_D1 = float(input("Digite o valor(R$) dessa respectiva conta: "))
                print("__________________________________________________________________")

                conta_C_main = input("Digite o nome da sua PRIMEIRA CONTA de Crédito: ")
                valor_C_main = float(input("Digite o valor(R$) dessa respectiva conta: "))
                print("___________________________________________________________________")

                histórico1 = input("Digite o histórico referente a está operação: ")
                print("___________________________________________________________________")
                print("")
                print("|____________________________LIVRO_DIÁRIO____________________________|")
                print("| Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                print("| D -\t%s\tR$ %.2f"%(conta_D_main,valor_D_main))
                print("| D -\t%s\tR$ %.2f"%(conta_D1,valor_D1))
                print("| C -\t%s\tR$ %.2f"%(conta_C_main,valor_C_main))
                print("| Histórico: %s"%histórico1)
                print("|____________________________________________________________________|")
        

    # PEDIR QUANTAS CONTAS DE DÉBITO(D) E CRÉDITO(C) TERAM CADA OPERAÇÃO
    # COLOCAR O VALOR (R$) EM CADA CONTA 
    # PEDIR O HISTORICO REFERENTE A CADA OPERAÇÃO
    # MOSTRAR O FINAL DA OPERÇÃO COM TUDO O QUE O USUÁRIO COLOCOU (AS CONTAS CADA UMA COM O SEU VALOR EM R$ E O HISTÓRICO).
    # FIM DIÁRIO

# LIVRO RAZÃO
def livro_razao_2():
    print("_______________________")
    print("|                     |")
    print("|     LIVRO RAZÃO     |")
    print("|_____________________|")
    print("")

# BALANCETE
def balancete_3():
    print("_______________________")
    print("|                     |")
    print("|      BALANCETE      |")
    print("|_____________________|")
    print("")

# BALANÇO PATRIMÔNIAL
def balanco_patrimonial_4():
    print("____________________________")
    print("|                          |")
    print("|    BALANÇO PATRIMÔNIAL   |")
    print("|__________________________|")
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

    escolha_2 = input("Digite o môdulo desejado (ou 5 para sair): ")
    print("")

    if escolha_2 == "1":
        livro_diario_1()
        print("")
    
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