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

# PEDIR O NÚMERO DE OPERAÇÕES
num_op = input("Digite quantas operações você deseja realizar (1,2,3,4...): ")
print()

if num_op == "1":
    os.system('clear || cls') # Se for Linux use "clear" e se for Windowns use "cls"
    print("1 OPERAÇÃO:")
    num_contas = input("Quantas contas terá nesta operção (POR PADRÃO JA TEM 1 DE DÉBITO E 1 DE CRÉDITO, ESCOLHA 0 PARA NÃO ADICIONAR)? ")
    print()
    if num_contas == "0":
        valor_d0 = 0
        valor_c0 = 0
        while valor_d0 == valor_c0:
            os.system('clear || cls')
            print("NENHUMA CONTA ADICIONADA 1 - DÉBITO e 1 - CRÉDTIO (PADRÃO).")
            print()
            conta_d0 = input("Digite o nome da sua 1ª conta de DÉBITO: ")
            valor_d0 = float(input("Digite o valor R$ da conta %s: "%conta_d0))
            print()
            conta_c0 = input("Digite o nome da sua 1ª conta de CRÉDITO: ")
            valor_c0 = float(input("Digite o valor R$ da conta %s: "%conta_c0))  
            if valor_d0 != valor_c0:
                print("OPS! Os valores das contas não estão batendo com igualdade, por favor insira-os novamente.")
                print()
                input("tecle <ENTER> para retornar a inserir os dados...")
                valor_d0 = 0
                valor_c0 = 0
            else:
                historico0 = input("Digite o histórico referente a está operação: ")
                print()
                print(ascii.livro_diario_ascii())
                print("Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                print("D\t\t-\t\t%s\t\tR$ %.2f"%(conta_d0,valor_d0))
                print("C\t\t-\t\t%s\t\tR$ %.2f"%(conta_c0,valor_c0))
                print("Histórico: %s"%historico0)
                print()
                input("tecle <ENTER> para continuar...")
                
                def prmeira_operacao():
                    print(ascii.livro_diario_ascii())
                    print("Data da operação: %02d/%02d/%d"%(dia,mes,ano))
                    print("D\t\t-\t\t%s\t\tR$ %.2f"%(conta_d0,valor_d0))
                    print("C\t\t-\t\t%s\t\tR$ %.2f"%(conta_c0,valor_c0))
                    print("Histórico: %s"%historico0)
                    print()
                
            


    
    










# FIM DE FUNÇÕES DIÁRIO        

# OBS: Eu ainda vou fazer muito mais por aqui, mas, como ainda estou na fase de testes, estou fazendo com um tamanho reduzido.