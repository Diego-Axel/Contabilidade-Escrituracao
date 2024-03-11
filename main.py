############################################################
######          ESCRITURAÇÃO CONTÁBIL BÁSICA          ######
######               OBJETIVO: TREINAR                ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RM                    ######
############################################################

# OBS: Estou refazendo... Motivos? -> Posso melhorar

# imports
import funcoes # fazenzo importação do arquivo onde ficará as funções (modularizando)
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
        funcoes.usuario_existente_1()
        break 
    
    elif escolha == 2:
        funcoes.novo_usuario_2()
        break

    else:
        print("Encerrando o programa, até breve!")
        break 

# PÓS ESSA PRIMEIRA PARTE
    
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

    # INICIO -> CONDICIONAIS DOS NÚMEROS DE OPERAÇÕES:
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
            print("Você escolheu adicionar nehuma conta ")
            print("")
            conta_D_main = input("Digite o nome da sua PRIMEIRA CONTA de Débito: ")
            valor_D_main = float(input("Digite o valor (R$) dessa respectiva conta: "))
            print("__________________________________________________________________")

            conta_C_main = input("Digite o nome da sua PRIMEIRA CONTA de Crédito: ")
            valor_C_main = float(input("Digite o valor (R$) dessa respectiva conta: "))
            print("__________________________________________________________________")

            historico1 = input("Digite o histórico referente a está operação: ")
            print("__________________________________________________________________")
            print("")
            print("|____________________________LIVRO_DIÁRIO____________________________|")
            print("| Data da operação: %02d/%02d/%d"%(dia,mes,ano))
            print("| D -\t%s\tR$ %.2f"%(conta_D_main,valor_D_main))
            print("| C -\t%s\tR$ %.2f"%(conta_C_main,valor_C_main))
            print("| Histórico: %s"%historico1)
            print("|____________________________________________________________________|")
            print("") # espaços
            
        elif numero_contas == 1:
            print("Você escolheu adiconar 1 conta.")
            print("")
            print("Como havia falado anteriormeente, você você JA POSSUI duas contas 1 DE DÉBITO E 1 DE CRÉDITO.")
            print("") # ESPAÇOS

            tipo_conta0 = input("Qual o tipo da conta você deseja adicionar(D ou C):? ")
            if tipo_conta0 == "Débito" or "Debtio" or "débito" or "debito" or "D" or "d": # CONDICIONAL REFERENTE AO TIPO DA CONTA (D OU C)
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

                historico1 = input("Digite o histórico referente a está operação: ")
                print("___________________________________________________________________")
                print("")
                print("|____________________________LIVRO_DIÁRIO____________________________|")
                print("| Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                print("| D -\t%s\tR$ %.2f"%(conta_D_main,valor_D_main))
                print("| D -\t%s\tR$ %.2f"%(conta_D1,valor_D1))
                print("| C -\t%s\tR$ %.2f"%(conta_C_main,valor_C_main))
                print("| Histórico: %s"%historico1)
                print("|____________________________________________________________________|")
                print("") # espaços
            
            elif tipo_conta0 == "Crédito" or "Credito" or "crédito" or "credito" or "C" or "c":
                print("Você escolheu adicionar uma conta aoo tipo CRÉDITO:")
                print("")

                conta_D_main = input("Digite o nome da sua PRIMERIA CONTA de Débito: ")
                valor_D_main = float(input("Digite o valor(R$) dessa respectiva conta: "))
                print("__________________________________________________________________")

                conta_C_main = input("Digite o nome da sua PRIMEIRA CONTA de Crédito: ")
                valor_C_main = float(input("Digite o valor(R$) dessa respectiva conta: "))
                print("___________________________________________________________________")

                conta_C1 = input("Digite o valor da sua SEGUNDA CONTA DE CRÉDITO: ")
                valor_C1 = float(input("Digite o valor(R$) dessa respectiva conta: "))
                print("__________________________________________________________________")

                historico1 = input("Digite o histórico referente a está operação: ")
                print("__________________________________________________________________")
                print("")
                print("|____________________________LIVRO_DIÁRIO____________________________|")
                print("| Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                print("| D -\t%s\tR$ %.3f"%(conta_D_main,valor_D_main))
                print("| C -\t%s\tR$ %.3f"%(conta_C_main,valor_C_main))
                print("| C -\t%s\tR$ %.3f"%(conta_C1,valor_C1))
                print("| Histórico: %s"%historico1)
                print("|____________________________________________________________________|")
                print("") # espaços
            
            else:
                print("Não foi colocado o que se pede.")

        elif numero_contas == 2:
            print("Você escolheu adicionar 2 contas.")
            print("")
            print("Como havia falado anteriormeente, você você JA POSSUI duas contas 1 DE DÉBITO E 1 DE CRÉDITO.")
            print("") # ESPAÇOS

            tipo_conta0 = input("Qual o tipo da 1 CONTA que você deseja adicionar(D ou C):? ")
            tipo_conta1 = input("Qual o tipo da 2 CONTA que você deseja adicionar(D ou C):? ")

            if tipo_conta0 == ("Débito","débtio","Debito","debito","D","d") and tipo_conta1 == ("Débito","débtio","Debito","debito","D","d"):
                print("Você escolheu adiconar 2 CONTAS ao Débito.")
                print("")

                conta_D_main = input("Digite o nome da sua PRIMERIA CONTA de Débito: ")
                valor_D_main = float(input("Digite o valor(R$) dessa respectiva conta: "))
                print("__________________________________________________________________")

                conta_D1 = input("Digite o valor da sua SEGUNDA CONTA DE DÉBITO: ")
                valor_D1 = float(input("Digite o valor(R$) dessa respectiva conta: "))
                print("__________________________________________________________________")

                conta_D2 = input("Digite o valor da sua TERCEIRA CONTA DE DÉBITO: ")
                valor_D2 = float(input("Digite o valor(R$) dessa respectiva conta: "))
                print("__________________________________________________________________")

                conta_C_main = input("Digite o nome da sua PRIMEIRA CONTA de Crédito: ")
                valor_C_main = float(input("Digite o valor(R$) dessa respectiva conta: "))
                print("___________________________________________________________________")

                historico1 = input("Digite o histórico referente a está operação: ")
                print("___________________________________________________________________")
                print("")
                print("|____________________________LIVRO_DIÁRIO____________________________|")
                print("| Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                print("| D -\t%s\tR$ %.3f"%(conta_D_main,valor_D_main))
                print("| D -\t%s\tR$ %.3f"%(conta_D1,valor_D1))
                print("| D -\t%s\tR$ %.3f"%(conta_D2,valor_D2))
                print("| C -\t%s\tR$ %.3f"%(conta_C_main,valor_C_main))
                print("| Histórico: %s"%historico1)
                print("|____________________________________________________________________|")
                print("") # espaços

            elif tipo_conta0 == ("Débito","débtio","Debito","debito","D","d") and tipo_conta1 == ("Crédito","crédito","Crédito","credito","C","c"):
                print("Você escolheu adicionar 1 conta ao Débtio e 1 conta ao Crédito: ")
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

                conta_C1 = input("Digite o valor da sua SEGUNDA CONTA DE CRÉDITO: ")
                valor_C1 = float(input("Digite o valor(R$) dessa respectiva conta: "))

                historico1 = input("Digite o histórico referente a está operação: ")
                print("___________________________________________________________________")
                print("")
                print("|____________________________LIVRO_DIÁRIO____________________________|")
                print("| Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                print("| D -\t%s\tR$ %.3f"%(conta_D_main,valor_D_main))
                print("| D -\t%s\tR$ %.3f"%(conta_D1,valor_D1))
                print("| C -\t%s\tR$ %.3f"%(conta_C_main,valor_C_main))
                print("| C -\t%s\tR$ %.3f"%(conta_C1,valor_C1))
                print("| Histórico: %s"%historico1)
                print("|____________________________________________________________________|")
                print("") # espaços

            elif tipo_conta0 == ("Crédito","crédito","Crédito","credito","C","c") and tipo_conta1 == ("Débito","débtio","Debito","debito","D","d"):
                print("Você escolheu adicionar 1 conta ao Débtio e 1 conta ao Crédito: ")
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

                conta_C1 = input("Digite o valor da sua SEGUNDA CONTA DE CRÉDITO: ")
                valor_C1 = float(input("Digite o valor(R$) dessa respectiva conta: "))

                historico1 = input("Digite o histórico referente a está operação: ")
                print("___________________________________________________________________")
                print("")
                print("|____________________________LIVRO_DIÁRIO____________________________|")
                print("| Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                print("| D -\t%s\tR$ %.3f"%(conta_D_main,valor_D_main))
                print("| D -\t%s\tR$ %.3f"%(conta_D1,valor_D1))
                print("| C -\t%s\tR$ %.3f"%(conta_C_main,valor_C_main))
                print("| C -\t%s\tR$ %.3f"%(conta_C1,valor_C1))
                print("| Histórico: %s"%historico1)
                print("|____________________________________________________________________|")
                print("") # espaços
            
            elif tipo_conta0 == ("Crédito","crédito","Crédito","credito","C","c") and tipo_conta1 == ("Crédito","crédito","Crédito","credito","C","c"):
                print("Você escolheu adicionar 2 contas ao CRÉDITO.")
                print("")

                conta_D_main = input("Digite o nome da sua PRIMERIA CONTA de Débito: ")
                valor_D_main = float(input("Digite o valor(R$) dessa respectiva conta: "))
                print("__________________________________________________________________")

                conta_C_main = input("Digite o nome da sua PRIMEIRA CONTA de Crédito: ")
                valor_C_main = float(input("Digite o valor(R$) dessa respectiva conta: "))
                print("___________________________________________________________________")

                conta_C1 = input("Digite o valor da sua SEGUNDA CONTA DE CRÉDITO: ")
                valor_C1 = float(input("Digite o valor(R$) dessa respectiva conta: "))

                conta_C2 = input("Digite o valor da sua TERCEIRA CONTA DE CRÉDITO: ")
                valor_C2 = float(input("Digite o valor(R$) dessa respectiva conta: "))
                print("__________________________________________________________________")

                historico1 = input("Digite o histórico referente a está operação: ")
                print("___________________________________________________________________")
                print("")
                print("|____________________________LIVRO_DIÁRIO____________________________|")
                print("| Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                print("| D -\t%s\tR$ %.3f"%(conta_D_main,valor_D_main))
                print("| C -\t%s\tR$ %.3f"%(conta_C_main,valor_C_main))
                print("| C -\t%s\tR$ %.3f"%(conta_C1,valor_C1))
                print("| C -\t%s\tR$ %.3f"%(conta_C2,valor_C2))
                print("| Histórico: %s"%historico1)
                print("|____________________________________________________________________|")
                print("") # espaços
            
            else:
                print("Não foi colocado o que se pede.")

        else:
            print("Não foi colocado o que se pede.") # FIM -> REFERENTE AO NÚMERO DE CONTAS QUANDO A OPERAÇÃO FOR APENAS 1

    else:
        print("Não foi colocado o que se pede.") # FIM -> REFERENTE AO NÚMERO DE OPERAÇÕES
        

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

    escolha_2 = int(input("Digite o môdulo desejado (ou 5 para sair): "))
    print("")

    if escolha_2 == 1:
        livro_diario_1()
    
    elif escolha_2 == 2:
        livro_razao_2()
    
    elif escolha_2 == 3:
        balancete_3()
    
    elif escolha_2 == 4:
        balanco_patrimonial_4()
        
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