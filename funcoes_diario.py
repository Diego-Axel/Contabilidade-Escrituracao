import datetime # biblioteca para puxar a data do computador
import os # biblioteca para interagir com o sistema operacional, estou usando para que tudo que esteja acima dela, seja removido. fica mais "limpo" de se vizualizar
import time # da um tempo para as informações sumirem -> time.sleep(o segundo que você quiser aqui quendo dos parenteses)


data = datetime.date.today()

dia = data.day
mes = data.month
ano = data.year

def livro_diario():
    os.system('clear || cls')

    print("""
     __       __  ____    ____ .______        ______       _______   __       ___      .______       __    ______   
    |  |     |  | \   \  /   / |   _  \      /  __  \     |       \ |  |     /   \     |   _  \     |  |  /  __  \  
    |  |     |  |  \   \/   /  |  |_)  |    |  |  |  |    |  .--.  ||  |    /  ^  \    |  |_)  |    |  | |  |  |  | 
    |  |     |  |   \      /   |      /     |  |  |  |    |  |  |  ||  |   /  /_\  \   |      /     |  | |  |  |  | 
    |  `----.|  |    \    /    |  |\  \----.|  `--'  |    |  '--'  ||  |  /  _____  \  |  |\  \----.|  | |  `--'  | 
    |_______||__|     \__/     | _| `._____| \______/     |_______/ |__| /__/     \__\ | _| `._____||__|  \______/ 
 
    """)

    print("CARREGANDO...")
    print("")
    time.sleep(4)
    os.system('clear || cls')


    print("_______________________")
    print("|                     |")
    print("|    LIVRO DIÁRIO     |")
    print("|_____________________|")
    print("")
    # PEDIR O NÚMERO DE OPERAÇÕES
    numero_operacoes = int(input("Digite quantas operações você deseja realizar(1,2,3...): "))
    print("")

    # condicionais 1
    if (numero_operacoes == 1):
        numero_contas = int(input("Quantas contas você deseja adiconar em %d operação(ões): "%numero_operacoes))
        # condicionais 2
        if numero_contas == 0:
            print("")
            conta_d_main = input("Digite o nome da sua conta D: ")
            valor_d_main = float(input("Digite o valor dessa conta: "))
            print("")
            conta_c_main = input("Digite o nome da sua conta C: ")
            valor_c_main = float(input("Digite o valor dessa conta: "))
            print("")
            historico1 = input("Digite o histórico desta operação: ")
            print("")
            print("Data da operação: %02d/%02d/%d"%(dia,mes,ano))
            print("D\t-\t%s\t\tR$%0.3f"%(conta_d_main,valor_d_main))
            print("C\t-\t%s\t\tR$%0.3f"%(conta_c_main,valor_c_main))
            print("Histórico: %s"%historico1)
            print("")
            print("CARREGANDO...")
            time.sleep(4)
            enter1 = input("APERTE ENTER PARA PROSSEGUIR ")
            print("")

        elif (numero_contas == 1):
            print("")
            conta_d_main = input("Digite o nome da sua conta D: ")
            valor_d_main = float(input("Digite o valor dessa conta: "))
            print("")
            conta_c_main = input("Digite o nome da sua conta C: ")
            valor_c_main = float(input("Digite o valor dessa conta: "))
            print("")
            tipo_conta = input("Escolha qual o tipo da próxima conta que deseja adicionar a operção(D/C): ")

            d1 = ["Débito","débito","Debito","debito","D","d"] # Bom, criei uma variável e na mesma adicionei as possiveis strings em uma lista que o usuário poderá digitar para que de continuidade ao programa. Pate dos Débitos

            c1 = ["Crédito","crédito","Credito","credito","C","c"] # Parte dos Créditos

            if (tipo_conta in d1):
                tipo_conta = tipo_conta.upper()
                print("Escolha = %s"%tipo_conta)
                conta_d1 = input("Digite o nome da sua conta D: ")
                valor_d1 = float(input("Digite o valor dessa conta: "))
                print("")
                historico1 = input("Digite o histórico desta operação: ")
                print("")
                print("Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                print("D\t-\t%s\t\tR$%0.3f"%(conta_d_main,valor_d_main))
                print("D\t-\t%s\t\tR$%0.3f"%(conta_d1,valor_d1))
                print("C\t-\t%s\t\tR$%0.3f"%(conta_c_main,valor_c_main))
                print("Histórico: %s"%historico1)
                print("")
                print("CARREGANDO...")
                time.sleep(4)
                enter1 = input("APERTE ENTER PARA PROSSEGUIR ")
                print("")

            elif (tipo_conta in c1):
                tipo_conta = tipo_conta.upper()
                print("Escolha = %s"%tipo_conta)
                conta_c1 = input("Digite o nome da sua conta C: ")
                valor_c1 = float(input("Digite o valor dessa conta: "))
                print("")
                historico1 = input("Digite o histórico desta operação: ")
                print("")
                print("Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                print("D\t-\t%s\t\tR$%0.3f"%(conta_d_main,valor_d_main))
                print("C\t-\t%s\t\tR$%0.3f"%(conta_c_main,valor_c_main))
                print("C\t-\t%s\t\tR$%0.3f"%(conta_c1,valor_c1))
                print("Histórico: %s"%historico1)
                print("")
                print("CARREGANDO...")
                time.sleep(4)
                enter1 = input("APERTE ENTER PARA PROSSEGUIR ")
                print("")

            # fim -> condiconais 2
            else:
                print("Não foi colocado o que se pede.")    
        
        elif numero_contas == 2:
            print("")
            conta_d_main = input("Digite o nome da sua conta D: ")
            valor_d_main = float(input("Digite o valor dessa conta: "))
            print("")
            conta_c_main = input("Digite o nome da sua conta C: ")
            valor_c_main = float(input("Digite o valor dessa conta: "))
            print("")
            tipo_conta = input("Escolha qual o tipo da próxima conta que deseja adicionar a operção(D/C): ")

            d1 = ["Débito","débito","Debito","debito","D","d"]

            c1 = ["Crédito","crédito","Credito","credito","C","c"]

            if tipo_conta in d1:
                tipo_conta = tipo_conta.upper()
                print("Escolha = %s"%tipo_conta)
                conta_d1 = input("Digite o nome da sua conta D: ")
                valor_d1 = float(input("Digite o valor dessa conta: "))
                print("")
                tipo_conta2 = input("Escolha qual o tipo da próxima conta que deseja adicionar a operação(D/C): ")

                d2 = ["Débito","débito","Debito","debito","D","d"]

                c2 = ["Crédito","crédito","Credito","credito","C","c"]

                if tipo_conta2 in d2:
                    tipo_conta2 = tipo_conta2.upper()
                    print("Escolha = %s"%tipo_conta2)
                    conta_d2 = input("Digite o nome da sua conta: ")
                    valor_d2 = float(input("Digite o valor dessa conta: "))
                    print("")
                    historico1 = input("Digite o histórico desta operação: ")
                    print("")
                    print("Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                    print("D\t-\t%s\t\tR$%0.3f"%(conta_d_main,valor_d_main))
                    print("D\t-\t%s\t\tR$%0.3f"%(conta_d1,valor_d1))
                    print("D\t-\t%s\t\tR$%0.3f"%(conta_d2,valor_d2))
                    print("C\t-\t%s\t\tR$%0.3f"%(conta_c_main,valor_c_main))
                    print("Histórico: %s"%historico1)
                    print("")
                    print("CARREGANDO...")
                    time.sleep(4)
                    enter1 = input("APERTE ENTER PARA PROSSEGUIR ")
                    print("")
                
                elif tipo_conta2 in c2:
                    tipo_conta2 = tipo_conta2.upper()
                    print("Escolha = %s"%tipo_conta2)
                    conta_c2 = input("Digite o nome da sua conta: ")
                    valor_c2 = float(input("Digite o valor dessa conta: "))
                    print("")
                    historico1 = input("Digite o histórico desta operação: ")
                    print("")
                    print("Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                    print("D\t-\t%s\t\tR$%0.3f"%(conta_d_main,valor_d_main))
                    print("D\t-\t%s\t\tR$%0.3f"%(conta_d1,valor_d1))
                    print("C\t-\t%s\t\tR$%0.3f"%(conta_c_main,valor_c_main))
                    print("C\t-\t%s\t\tR$%0.3f"%(conta_c2,valor_c2))
                    print("Histórico: %s"%historico1)
                    print("")
                    print("CARREGANDO...")
                    time.sleep(4)
                    enter1 = input("APERTE ENTER PARA PROSSEGUIR ")
                    print("")

            elif tipo_conta in c1:
                tipo_conta = tipo_conta.upper()
                print("Escolha = %s"%tipo_conta)
                conta_c1 = input("Digite o nome da sua conta: ")
                valor_c1 = float(input("Digite o valor dessa conta: "))
                print("")
                tipo_conta2 = input("Escolha qual o tipo da próxima conta que deseja adicionar a operação(D/C): ")

                d2 = ["Débito","débito","Debito","debito","D","d"]

                c2 = ["Crédito","crédito","Credito","credito","C","c"]

                if tipo_conta2 in c2:
                    tipo_conta2 = tipo_conta2.upper()
                    print("Escolha = %s"%tipo_conta2)
                    conta_c2 = input("Digite o nome da sua conta: ")
                    valor_c2 = float(input("Digite o valor dessa conta: "))
                    print("")
                    historico1 = input("Digite o histórico desta operação: ")
                    print("")
                    print("Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                    print("D\t-\t%s\t\tR$%0.3f"%(conta_d_main,valor_d_main))
                    print("C\t-\t%s\t\tR$%0.3f"%(conta_c_main,valor_c_main))
                    print("C\t-\t%s\t\tR$%0.3f"%(conta_c1,valor_c1))
                    print("C\t-\t%s\t\tR$%0.3f"%(conta_c2,valor_c2))
                    print("Histórico: %s"%historico1)
                    print("")
                    print("CARREGANDO...")
                    time.sleep(4)
                    enter1 = input("APERTE ENTER PARA PROSSEGUIR ")
                    print("")

                elif tipo_conta2 in d2:
                    tipo_conta2 = tipo_conta2.upper()
                    print("Escolha = %s"%tipo_conta2)
                    conta_d2 = input("Digite o nome da sua conta: ")
                    valor_d2 = float(input("Digite o valor dessa conta: "))
                    print("")
                    historico1 = input("Digite o histórico desta operação: ")
                    print("")
                    print("D\t-\t%s\t\tR$%0.3f"%(conta_d_main,valor_d_main))
                    print("D\t-\t%s\t\tR$%0.3f"%(conta_d2,valor_d2))
                    print("C\t-\t%s\t\tR$%0.3f"%(conta_c_main,valor_c_main))
                    print("C\t-\t%s\t\tR$%0.3f"%(conta_c1,valor_c1))
                    print("Histórico: %s"%historico1)
                    print("")
                    print("CARREGANDO...")
                    time.sleep(4)
                    enter1 = input("APERTE ENTER PARA PROSSEGUIR ")
                    print("")
                    
        # fim -> condiconais 2
        else:
            print("Não foi colocado o que se pede.")

    # fim -> condiconais 1
    else:
        print("Não foi colocado o que se pede.")

print("")
print("CARREGANDO...")
print("")
time.sleep(.4)

# FIM DE FUNÇÕES DIÁRIO        

# OBS: Eu ainda vou fazer muito mais por aqui, mas, como ainda estou na fase de testes, estou fazendo com um tamanho reduzido.