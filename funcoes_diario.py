import datetime # biblioteca para puxar a data do computador
import os 

data = datetime.date.today()

dia = data.day
mes = data.month
ano = data.year

def livro_diario_1():
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
    if numero_operacoes == 1:
        numero_contas = int(input("Quantas contas você deseja adiconar em %d operação: "%numero_operacoes))
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
            print("D\t-\t%s\tR$%0.3f"%(conta_d_main,valor_d_main))
            print("C\t-\t%s\tR$%0.3f"%(conta_c_main,valor_c_main))
            print("Histórico:\t%s"%historico1)
            print("")

        elif numero_contas == 1:
            print("")
            conta_d_main = input("Digite o nome da sua conta D: ")
            valor_d_main = float(input("Digite o valor dessa conta: "))
            print("")
            conta_c_main = input("Digite o nome da sua conta C: ")
            valor_c_main = float(input("Digite o valor dessa conta: "))
            print("")
            tipo_conta = input("Escolha qual o tipo da próxima conta que deseja adicionar a operção(D/C): ")

            d1 = ["Débito","débito","Debito","debito","D","d"] # Bom, criei uma variável e na mesma adicionei as possiveis strings que o usuário poderá digitar para que de continuidade ao programa. Pate dos D

            c1 = ["Crédito","crédito","Credito","credito","C","c"] # Parte dos C

            if tipo_conta in d1:
                print("Escolha = %s"%tipo_conta)
                conta_d1 = input("Digite o nome da sua conta D: ")
                valor_d1 = float(input("Digite o valor dessa conta: "))
                print("")
                historico1 = input("Digite o histórico desta operação: ")
                print("")
                print("Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                print("D\t-\t\t%s\tR$%0.3f"%(conta_d_main,valor_d_main))
                print("D\t-\t\t%s\tR$%0.3f"%(conta_d1,valor_d1))
                print("C\t-\t\t%s\tR$%0.3f"%(conta_c_main,valor_c_main))
                print("Histórico:\t%s"%historico1)
                print("")

            elif tipo_conta in c1:
                print("Escolha = %s"%tipo_conta)
                conta_c1 = input("Digite o nome da sua conta C: ")
                valor_c1 = float(input("Digite o valor dessa conta: "))
                print("")
                historico1 = input("Digite o histórico desta operação: ")
                print("")
                print("Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                print("D\t-\t\t%s\tR$%0.3f"%(conta_d_main,valor_d_main))
                print("C\t-\t\t%s\tR$%0.3f"%(conta_c_main,valor_c_main))
                print("C\t-\t\t%s\tR$%0.3f"%(conta_c1,valor_c1))
                print("Histórico:\t%s"%historico1)
                print("")

            # fim -> condiconais 2
            else:
                print("Não foi colocado o que se pede.")    
                
        # fim -> condiconais 2
        else:
            print("Não foi colocado o que se pede.")
    # fim -> condiconais 1
    else:
        print("Não foi colocado o que se pede.")

        