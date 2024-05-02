############################################################
######          ESCRITURAÇÃO CONTÁBIL BÁSICA          ######
######               OBJETIVO: TREINAR                ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RM                    ######
############################################################

# imports

import main
import ascii
import datetime 
import os 

data = datetime.date.today()

dia = data.day
mes = data.month
ano = data.year

os.system('clear || cls') # Se for Linux use "clear" e se for Windowns use "cls"
ascii.livro_diario_ascii()
print()

num_op = input("Digite quantas operações você deseja realizar (1,2,3,4...): ") # PEDIR O NÚMERO DE OPERAÇÕES
print()

if num_op == "1":
    os.system('clear || cls') # Se for Linux use "clear" e se for Windowns use "cls"
    print("1 OPERAÇÃO:")
    num_contas = input("Quantas contas terá nesta operção (POR PADRÃO JA TEM 1 DE DÉBITO E 1 DE CRÉDITO, ESCOLHA 0 PARA NÃO ADICIONAR)? ")
    print()
    if num_contas == "0":
        valor_d0 = 0
        valor_c0 = 0
        valor_nulo = 0
        while (valor_d0 == valor_c0) and (valor_nulo == 0):
            os.system('clear || cls')
            print("NENHUMA CONTA ADICIONADA 1 - DÉBITO e 1 - CRÉDTIO (PADRÃO).")
            print()
            conta_d0 = input("Digite o nome da sua 1ª conta de DÉBITO: ")
            valor_d0 = float(input("Digite o valor R$ da conta %s: "%conta_d0))
            print()
            conta_c0 = input("Digite o nome da sua 1ª conta de CRÉDITO: ")
            valor_c0 = float(input("Digite o valor R$ da conta %s: "%conta_c0))  
            print()
            if valor_d0 != valor_c0:
                print("OPS! Os valores das suas contas de DÉBITO(R$ %.2f,00) e CRÉDITO(R$ %.2f,00) não estão batendo com igualdade, por favor insira-os novamente."%(valor_d0,valor_c0))
                print()
                input("tecle <ENTER> para retornar a inserir os dados...")
                valor_d0 = 0
                valor_c0 = 0
                valor_nulo = 0
            else:
                historico_0 = input("Digite o histórico referente a está operação: ")
                print()
                ascii.livro_diario_ascii()
                print("Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                print("D\t\t-\t\t%s\t\tR$ %.2f,00"%(conta_d0,valor_d0))
                print("C\t\t-\t\t%s\t\tR$ %.2f,00"%(conta_c0,valor_c0))
                print("Histórico: %s"%historico_0)
                print()
                input("tecle <ENTER> para continuar...")
                valor_nulo = 1
                def prmeira_operacao_0(): # Função que nela vai estar contida a primeira operação caso precise chamar novamente mais para frente
                    print()
                    ascii.livro_diario_ascii()
                    print("Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                    print("D\t\t-\t\t%s\t\tR$ %.2f,00"%(conta_d0,valor_d0))
                    print("C\t\t-\t\t%s\t\tR$ %.2f,00"%(conta_c0,valor_c0))
                    print("Histórico: %s"%historico_0)
                    print()                 
    elif num_contas == "1":
        valor_d0 = 0
        valor_d1 = 0
        valor_c0 = 0
        valor_c1 = 0
        valor_nulo = 0
        tipo_conta = input("Qual tipo da conta você quer adicionar(D/C)? ")
        tipo_conta = tipo_conta.upper()
        dic_D = ["D", "DÉBITO", "DEBITO"] 
        dic_C = ["C", "CRÉDITO", "CREDITO"]
        if tipo_conta in dic_D: 
            while ((valor_d0 + valor_d1) == valor_c0) and (valor_nulo == 0):
                os.system('clear || cls') # Se for Linux use "clear" e se for Windowns use "cls"
                print("UM CONTA ADICIONADA: DÉBITO")
                print()
                conta_d0 = input("Digite o nome da sua 1ª conta de DÉBITO: ")
                valor_d0 = float(input("Digite o valor R$ da conta %s: "%conta_d0))
                print()
                conta_d1 = input("Digite o nome da sua 2ª conta de DÉBITO: ")
                valor_d1 = float(input("Digite o valor R$ da conta %s: "%conta_d1))
                print()
                conta_c0 = input("Digite o nome da sua 1ª conta de CRÉDITO: ")
                valor_c0 = float(input("Digite o valor R$ da conta %s: "%conta_c0))
                print()
                if ((valor_d0 + valor_d1) != valor_c0):
                    soma_d = valor_d0 + valor_d1
                    print("OPS! Os valores da suas contas de DÉBITO(R$ %.2f,00) e CRÉDTIO(R$ %.2f,00) não estão batendo com igualdade, por favor insira-os novamente."%(soma_d,valor_c0))
                    print()
                    input("tecle <ENTER> para retornar a inserir os dados...")
                    valor_d0 = 0
                    valor_d1 = 0
                    valor_c0 = 0
                    valor_nulo = 0
                else:
                    historico_0 = input("Digite o histórico referente a está operação: ")
                    print()
                    ascii.livro_diario_ascii()
                    print("Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                    print("D\t\t-\t\t%s\t\tR$ %.2f,00"%(conta_d0,valor_d0))
                    print("D\t\t-\t\t%s\t\tR$ %.2f,00"%(conta_d1,valor_d1))
                    print("C\t\t-\t\t%s\t\tR$ %.2f,00"%(conta_c0,valor_c0))
                    print("Histórico: %s"%historico_0)
                    print()
                    input("tecle <ENTER> para continuar...")
                    valor_nulo = 1
                    def primeira_operacao_1D():
                        ascii.livro_diario_ascii()
                        print("Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                        print("D\t\t-\t\t%s\t\tR$ %.2f,00"%(conta_d0,valor_d0))
                        print("D\t\t-\t\t%s\t\tR$ %.2f,00"%(conta_d1,valor_d1))
                        print("C\t\t-\t\t%s\t\tR$ %.2f,00"%(conta_c0,valor_c0))
                        print("Histórico: %s"%historico_0)
                        print()
        elif tipo_conta in dic_C:
            print()
            


    
    










# FIM DE FUNÇÕES DIÁRIO        

# OBS: Eu ainda vou fazer muito mais por aqui, mas, como ainda estou na fase de testes, estou fazendo com um tamanho reduzido.