import datetime

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

    if numero_operacoes == 1:
        numero_contas = int(input("Quantas contas você deseja adiconar em %d operação: "%numero_operacoes))
        if numero_contas == 0:
            print("")
            contaD_main = input("Digite o nome da sua conta D: ")
            valorD_main = float(input("Digite o valor dessa conta: "))
            print("")
            contaC_main = input("Digite o nome da sua conta C: ")
            valorC_main = float(input("Digite o valor dessa conta: "))
            print("")
            historico1 = input("Digite o histórico desta operação: ")
            print("")
            print("Data da operação: %02d/%02d/%d"%(dia,mes,ano))
            print("D\t-\t%s\tR$%0.3f"%(contaD_main,valorD_main))
            print("C\t-\t%s\tR$%0.3f"%(contaC_main,valorC_main))
            print("Histórico:\t%s"%historico1)
            print("")

        elif numero_contas == 1:
            print("")
        

        else:
            print("")

    else:
        print("")

        