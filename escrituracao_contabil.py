############################################################
######          ESCRITURAÇÃO CONTÁBIL BÁSICA          ######
######               OBJETIVO: TREINAR                ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RM                    ######
############################################################



# importações
import datetime

data = datetime.date.today()
dia = data.day
mes = data.month
ano = data.year


print("-----------------------------------------------------")
print("|               ESCRITURAÇÃO CONTABÍL               |")
print("-----------------------------------------------------")
# Módulos que esse sistemas tem a oferecer:
def Livro_Diario_1():
    print("---------------------------------------")
    print("|     Você escolheu LIVRO DIÁRIO      |")
    print("---------------------------------------")
    print("                                       ") # espaços
    print("                                       ")

def Livro_Razao_2():
    print("---------------------------------------")
    print("|     Você escolheu LIVRO RAZÃO       |")
    print("---------------------------------------")
    print("                                       ") # espaços
    print("                                       ")

def Balancete_3():
    print("---------------------------------------")
    print("|      Você escolheu BALANCETE        |")
    print("---------------------------------------")
    print("                                       ") # espaços
    print("                                       ")

def Balanco_Patrimonial_4():
    print("---------------------------------------")
    print("|  Você escolher BALANÇO PATRIMÔNIAL  |")
    print("---------------------------------------")
    print("                                       ") # espaços
    print("                                       ")

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

        print("Assim ficará o Livro Diário no decorrer desta ação:")
        print("                                                   ")

        print("Data da operação: xx/xx/xxxx")
        print("D(DÉBITO) - contaX1 - R$ xx.xxx,xx")
        print("C(CRÉDITO) - contaX2 - R$ xx.xxx,xx")
        print("Histórico referente a operação: xxxxx...") 
        print("                                                   ")
        print("OBS.: A depender da ocasião, pode-se ter mais de uma conta no Débito e mais de uma conta no crédito.") 
        print("Contanto que: As somas do Débitos seja igual a soma dos Crédtios, isso é obrigatório independente") 
        print("                                                   ")

        numero_operacoes = input("Digite quantas operações deseja realizar (1, 2, 3, 4, 5,) máximo de 5, por enqaunto: ")
        print("                                                                                                        ")

        if numero_operacoes == "1":
            print("Você escolheu 1 operação.")
            print("                         ")
            numero_contas = input("Agora escolha quantas contas terá nesta operação(Você já começa com 2 contas, um D e um C comm valor correspondente): ")
            if numero_contas == "3":
                print("                                                              ")
                print("Você escolheu %s contas"%numero_contas)
                print("                                                              ")
                qual_conta = input("Você já tem naturalmente, 1 conta de D e uma conta de crédito. Você decidiu adicionar mais uma ao seu Diário, qual será?(D ou C): ")
                if qual_conta == ("d" or "D" or "débito" or "Débito"):
                    print("")
                elif qual_conta ==("c" or "C" "crédito" or "Crédito"):
                    print("")
                else:
                    print("")

            else:
                print("")
        elif numero_operacoes == "2":
            print("Você escolheu 2 operações.")
            print("                         ")
            numero_contas = input("Agora escolha quantas contas terá nesta operção(Você já começa com 2 contas, um D e um C comm valor correspondente a ele): ")
        elif numero_operacoes == "3":
            print("Você escolheu 3 operações.")
            print("                         ")
            numero_contas = input("Agora escolha quantas contas terá nesta operação(Você já começa com 2 contas, um D e um C comm valor correspondente a ele): ")
        elif numero_operacoes == "4":
            print("Você escolheu 4 operações.")
            print("                         ")
            numero_contas = input("Agora escolha quantas contas terá nesta operação(Você já começa com 2 contas, um D e um C comm valor correspondente a ele): ")
        elif numero_operacoes == "5":
            print("Você escolheu 5 operações.")
            print("                         ")
            numero_contas = input("Agora escolha quantas contas terá nesta operação(Você já começa com 2 contas, um D e um C comm valor correspondente a ele): ")
        else:
            print("Não foi colodado o que se pede.")





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

        print("Assim ficará o Razonete no decorrer desta ação:")
        print("                                               ")

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
        print("______________________________________________________________________________________")
        print(" ########     ###    ##          ###    ##    ##  ######  ######## ######## ########  ")
        print(" ##     ##   ## ##   ##         ## ##   ###   ## ##    ## ##          ##    ##        ")
        print(" ##     ##  ##   ##  ##        ##   ##  ####  ## ##       ##          ##    ##        ")
        print(" ########  ##     ## ##       ##     ## ## ## ## ##       ######      ##    ######    ")
        print(" ##     ## ######### ##       ######### ##  #### ##       ##          ##    ##        ")
        print(" ##     ## ##     ## ##       ##     ## ##   ### ##    ## ##          ##    ##        ")
        print(" ########  ##     ## ######## ##     ## ##    ##  ######  ########    ##    ########  ")
        print("______________________________________________________________________________________")

        print("Assim ficará o Balamcete no decorrer desta operação")
        print("                                                   ")

        print("_________________________________________________________________")
        print("")



    elif escolha == "4":
        Balanco_Patrimonial_4()
        print("########     ###    ##          ###    ##    ##  ######   #######  ")
        print("##     ##   ## ##   ##         ## ##   ###   ## ##    ## ##     ## ")
        print("##     ##  ##   ##  ##        ##   ##  ####  ## ##       ##     ## ")
        print("########  ##     ## ##       ##     ## ## ## ## ##       ##     ## ")
        print("##     ## ######### ##       ######### ##  #### ##       ##     ## ")
        print("##     ## ##     ## ##       ##     ## ##   ### ##    ## ##     ## ")
        print("########  ##     ## ######## ##     ## ##    ##  ######   ####### " )
        print("                                                   ###             ")
        print("                                                    ##             ")
        print("                                                                   ")
        #---------------------------------------------------------------------------
        print("                                                         ###                                     ")
        print("                                                        ## ##                                    ")
        print("                                                       ##   ##                                   ")
        print("                                                                                                 ")
        print("########     ###    ######## ########  #### ##     ##  #######  ##    ## ####    ###    ##       ")
        print("##     ##   ## ##      ##    ##     ##  ##  ###   ### ##     ## ###   ##  ##    ## ##   ##       ")
        print("##     ##  ##   ##     ##    ##     ##  ##  #### #### ##     ## ####  ##  ##   ##   ##  ##       ")
        print("########  ##     ##    ##    ########   ##  ## ### ## ##     ## ## ## ##  ##  ##     ## ##       ")
        print("##        #########    ##    ##   ##    ##  ##     ## ##     ## ##  ####  ##  ######### ##       ")
        print("##        ##     ##    ##    ##    ##   ##  ##     ## ##     ## ##   ###  ##  ##     ## ##       ")
        print("##        ##     ##    ##    ##     ## #### ##     ##  #######  ##    ## #### ##     ## ######## ")
        print("                                                                                                 ")

        print("Assim ficará o Balanço Patrimônial no decorrer desta operação:")
        print("                                                              ")

        print("|_____________________________BALANÇO PATRIMÔNIAL___________________________|")
        print("|_____ATIVOS_____R$__________________|____________PASSIVOS_____R$___________|")
        print("| contaX         R$ xx.xxx.xx        |             contaX      R$ xx.xxx.xx |")
        print("| contaX         R$ xx.xxx.xx        |             contaX      R$ xx.xxx.xx |")
        print("| contaX         R$ xx.xxx.xx        |             contaX      R$ xx.xxx.xx |")
        print("| contaX         R$ xx.xxx.xx        |             contaX      R$ xx.xxx.xx |")
        print("| contaX         R$ xx.xxx.xx        |             contaX      R$ xx.xxx.xx |")
        print("|____________________________________|______________________________________|")
        print("|                                    |                                      |")
        print("|____________________________________|____PATRIMÔNIO LÍQUIDO___R$___________|")
        print("|                                    |          contaX         R$ xx.xxx.xx |")
        print("|                                    |          contaX         R$ xx.xxx.xx |")
        print("|                                    |          contaX         R$ xx.xxx.xx |")
        print("|____________________________________|______________________________________|")
        print("| TOTAL = xx.xxx.xx                  | TOTAL = xx.xxx.xx                    |")
        print("|____________________________________|______________________________________|")



        
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
