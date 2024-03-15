import datetime # biblioteca para puxar a data do computador

data = datetime.date.today()

dia = data.day
mes = data.month
ano = data.year

def livro_diario_1():
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
        
        # fim -> condiconais 2
        else:
            print("")
    # fim -> condiconais 1
    else:
        print("Não foi colocado o que se pede.")

        