
print("|---------------------------------------------------|")
print("|               ESCRITURAÇÃO CONTABÍL               |")
print("|---------------------------------------------------|")
# Módulos que esse sistemas deve oferecer:
def Livro_Diario_1():
    print("Você escolheu LIVRO DIÁRIO.")

def Livro_Razao_2():
    print("Você escolheu LIVRO RAZÃO")

def Balancete_3():
    print("Você escolheu BALANCETE.")

def Balanco_Patrimonial_4():
    print("Você escolher BALANÇO PATRIMÔNIAL.")

while True:
# Solicitar ao usuário que escolha um módulo
    print("Escolha o módulo:")
    print("1. Livro Diário")
    print("2. Livro Razão")
    print("3. Balancete")
    print("4. Balanço Patrimônial")
    print("0. Sair")

    escolha = input("Digite o número do módulo desejado (ou 0 para sair): ")
# Estruturar o código com base na escolha do usuário
    if escolha == "1":
        Livro_Diario_1()
        print("_________________________________________________________________________________")
        print("                                                                   $$$$$         ")   
        print("                                                                   $:::$         ")    
        print("                                                               $$$$$:::$$$$$$    ") 
        print("                                                             $$::::::::::::::$   ")
        print("                                                             $:::::$$$$$$$::::$  ")
        print("                                                             $::::$       $$$$$  ")
        print(" ########  ####    ###    ########  ####  #######            $::::$              ")            
        print(" ##     ##  ##    ## ##   ##     ##  ##  ##     ##           $::::$              ")            
        print(" ##     ##  ##   ##   ##  ##     ##  ##  ##     ##           $:::::$$$$$$$$$     ")   
        print(" ##     ##  ##  ##     ## ########   ##  ##     ##            $$::::::::::::$$   ")
        print(" ##     ##  ##  ######### ##   ##    ##  ##     ##              $$$$$$$$$:::::$  ")
        print(" ##     ##  ##  ##     ## ##    ##   ##  ##     ##                       $::::$  ")
        print(" ########  #### ##     ## ##     ## ####  #######                        $::::$  ")
        print("                                                             $$$$$       $::::$  ")
        print("                                                             $::::$$$$$$$:::::$  ")
        print("                                                             $::::::::::::::$$   ")
        print("                                                              $$$$$$:::$$$$$     ")
        print("                                                                   $:::$         ")
        print("                                                                   $$$$$         ")
        print("_________________________________________________________________________________")
        print("                                                                                  ")
        print("----------------------------------------------------------------------------------")
    elif escolha == "2":
        Livro_Razao_2()
        print("________________________________________________________________________________")
        print("|  ########     ###    ########  #######  ##    ## ######## ######## ########  |")
        print("|  ##     ##   ## ##        ##  ##     ## ###   ## ##          ##    ##        |")
        print("|  ##     ##  ##   ##      ##   ##     ## ####  ## ##          ##    ##        |")
        print("|  ########  ##     ##    ##    ##     ## ## ## ## ######      ##    ######    |")
        print("|  ##   ##   #########   ##     ##     ## ##  #### ##          ##    ##        |")
        print("|  ##    ##  ##     ##  ##      ##     ## ##   ### ##          ##    ##        |")
        print("|  ##     ## ##     ## ########  #######  ##    ## ########    ##    ########  |")
        print("|______________________________________________________________________________|")

        print("--------------------------------------------------")

        # ASSIM FICARÁ O LIVRO DIÁRIO FINALIZADO
        print("_DÉBITOS__________NOME_DA_CONTA__________CRÉDITOS_")
        print("                        |                         ")
        print("                        |                         ")
        print("                        |                         ")
        print("                        |                         ")
        print("                        |                         ")
        print("__________________________________________________")
        print("                        |                         ") # Nessa parte aqui, após essas linhas, será o total dos D e do outro lado | o total dos C.


        print("--------------------------------------------------")
        nome_conta = input("Digite o NOME DA CONTA: ") # Só para lembrar, essa conta pode ser Caixa, Banco, Cliente, Fornecedor, Despesa, enfim.
        print("--------------------------------------------------")
        valor_conta = float(input(f"Digite o valor do(a, e) {nome_conta} (R$): "))
        print("--------------------------------------------------")

        # Parte das condicionais:
        if nome_conta == "Caixa" or nome_conta == "caixa":
            print(f"Você quer adicionar a conta {nome_conta} no DÉBITO(D) ou no CRÉDITO(C)?")
            tipo_conta = input("")
            if tipo_conta == "D" or tipo_conta == "d":
                print(f"_DÉBITOS__________{nome_conta}__________CRÉDITOS_")
                print(f" R${valor_conta}                                 ")
                print("                                                  ")
                print("__________________________________________________")
            elif tipo_conta == "C" or tipo_conta == "c":
                print(f"_DÉBITOS__________{nome_conta}__________CRÉDITOS_")
                print(f"                                  R${valor_conta}")
                print("                                                  ")
                print("__________________________________________________")
            else:
                print("NÃO FOI DIGITADO O QUE FOI PEDIDO TENTE NOVAMENTE.")
        elif nome_conta == "Banco" or nome_conta == "banco":
            print(f"Você quer adicionar a conta {nome_conta} no DÉBITO(D) ou no CRÉDITO(C)?")
            tipo_conta = input("")
            if tipo_conta == "D" or tipo_conta == "d":
                print(f"_DÉBITOS__________{nome_conta}__________CRÉDITOS_")
                print(f" R${valor_conta}                                 ")
                print("                                                  ")
                print("__________________________________________________")
            elif tipo_conta == "C" or tipo_conta == "c":
                print(f"_DÉBITOS__________{nome_conta}__________CRÉDITOS_")
                print(f"                                  R${valor_conta}")
                print("                                                  ")
                print("__________________________________________________")
            else:
                print("NÃO FOI DIGITADO O QUE FOI PEDIDO TENTE NOVAMENTE.")
        elif nome_conta == "Mercadoria" or "mercadoria":
            print(f"Você quer adicionar a conta {nome_conta} no DÉBITO(D) ou no CRÉDITO(C)?")
            tipo_conta = input("")
            if tipo_conta == "D" or tipo_conta == "d":
                print(f"_DÉBITOS__________{nome_conta}__________CRÉDITOS_")
                print(f" R${valor_conta}                                 ")
                print("                                                  ")
                print("__________________________________________________")
            elif tipo_conta == "C" or tipo_conta == "c":
                print(f"_DÉBITOS__________{nome_conta}__________CRÉDITOS_")
                print(f"                                  R${valor_conta}")
                print("                                                  ")
                print("__________________________________________________")
            else:
                print("NÃO FOI DIGITADO O QUE FOI PEDIDO TENTE NOVAMENTE.")
        else:
            print("NÃO FOI DIGITADO O QUE FOI PEDIDO TENTE NOVAMENTE.")

        print("--------------------------------------------------")
        print("Neste momento, assim está as informações do seu razonete:")
        print("--------------------------------------------------")
        print(f"Nome da conta: {nome_conta}")
        print(f"Valor desta conta: {valor_conta}")
        print(f"Tipo da conta (D ou C): {tipo_conta}")
        print("--------------------------------------------------")

        print("Deseja adicionar mais valores em seu razonete?" )
        s_n = input("")

        if s_n == "s" or s_n == "sim" or s_n == "Sim":
            print(f"Você pretende adicionar valor na conta que você escolheu anteriormente: Seus dados são: Conta: {nome_conta}, Valor: {valor_conta}, e Tipo: {tipo_conta}")
            print("--------------------------------------------------")
            escolha = input("Pretende adicionar valor ao débito ou ao crédito? ")
            if escolha == "d" or escolha == "D" or escolha == "Débito" or escolha == "Debito" or escolha == "debito" or escolha == "débito":
                print(f"Você escolheu: {escolha}")
                print("--------------------------------------------------")
                print("Assim está o seu razonete")
                print("--------------------------------------------------")
                print(f"_DÉBITOS__________{nome_conta}__________CRÉDITOS_")
                print(f" R${valor_conta}                                 ")
                print("                                                  ")
                print("__________________________________________________")
                valor2_conta = float(input("Digite o valor para essa conta: "))
                print("--------------------------------------------------")
                print(f"_DÉBITOS__________{nome_conta}__________CRÉDITOS_")
                print(f" R${valor_conta}                                 ")
                print(f" R${valor2_conta}                                ")
                somad = valor_conta + valor2_conta
                print("__________________________________________________")
                print("SOMATORIO DOS D____________________SOMATORIO DOS C")
                print(f"R${somad}                                        ")
                print("--------------------------------------------------")
            elif escolha == "c" or escolha == "C" or escolha == "Crédito" or escolha == "Credito" or escolha == "credito" or escolha == "crédito":
                print(f"Você escolheu: {escolha}")
                print("--------------------------------------------------")
                print("Assim está o seu razonete")  
                print("--------------------------------------------------")
                print(f"_DÉBITOS__________{nome_conta}__________CRÉDITOS_")
                print(f" R${valor_conta}                                 ")
                print("                                                  ")
                print("__________________________________________________")  
                valor2_conta = float(input("Digite o valor para essa conta: "))
                print("--------------------------------------------------")
                print(f"_DÉBITOS__________{nome_conta}__________CRÉDITOS_")
                print(f" R${valor_conta}                                 ")
                print(f"                                R${valor2_conta} ")
                somad = valor_conta - valor2_conta
                print("__________________________________________________")
                print("SOMATORIO DOS D____________________SOMATORIO DOS C")
                print(f"R${valor_conta}                  R${valor2_conta}")
                print("--------------------------------------------------")
                print(f"                  R${somad}                      ") 
            
            else:
                print("")

        else:
            print("Você escolheu: NÃO -> FIM DO PROGRAMA")
    elif escolha == "3":
        Balancete_3()
    elif escolha == "4":
        Balanco_Patrimonial_4()
    elif escolha == "0":
        print("Saindo do programa. Até mais!")
        break  # Sai do loop se o usuário escolher sair
    else:
        print("Escolha inválida. Por favor, digite um número válido de módulo.")

# Perguntar se o usuário deseja escolher outro módulo
    escolha_nova = input("Deseja escolher outro módulo? (Digite 'sim' ou 'nao'): ")
    if escolha_nova.lower() != "sim":
        print("Saindo do programa. Até mais!")
        break  # Sai do loop se o usuário não quiser escolher outro módulo
