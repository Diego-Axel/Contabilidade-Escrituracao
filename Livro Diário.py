# PROGRAMA PARA SE UTILIZAR A CONTABILIDADE BÁSICA(DIÁRIO, RAZONETE, BALANECETE E BALANÇO PATRIMONIAL)

# PROJETO APENAS PARA USO PESSOAL COMO TREINAMENTO (NÃO SEI SE LEVAREI ISSO ADIANTE :D )

print("-----------------------------------------------")
print("|                LIVRO DIÁRIO                 |" )
print("-----------------------------------------------")

# Bom, a começar a explicar o que seria um diário para o mundo da contabilidade. Basicamente seria como se a gente estivesse fazendo um resgistro de toda a movimentação que ocorreu na empresa ou comércio da entidade(Pessoa Física ou Pessoa Jurídica), essa movimentação se da por: Compra de mercadoria, fluxo do caixa(Entrada e saída de U$$), recebimento de dinheiro de vendas, enfim, tudo aquilo que possa alterar o patrimônio  da entide.

print("-----------------------------------------------")
empresa = input("Qual o nome da sua empresa(LTda)? ")
print("-----------------------------------------------")
print(f" Empresa {empresa}, vamos fazer o levantamento do seu livro diário. ")
print("-----------------------------------------------")

# Após a pessoa ter dado o nome de sua empresa, agora chegou a hora de escolher o número de suas operações. É simples, a contabilidade tem uma linguagem única que utiliza o Débito(D) e o Crédito(C), mas esse débito e crédito não são os mesmos que são usados no nosso cotidiano, entenda aqui na contabulidade como débito=algo bom e crédito=oposto.

print("Quantas operações deseja realizar (Máximo de 10 (BETA))? ") #Ainda desenvolvendo...
numero_op = int(input(""))
#--------------------------------------------------------------
print("-----------------------------------------------")
print("Quantas contas você deseja adicionar? ")
numero_conta = input("")

if numero_conta == 2:
    print("Se você escolheu 2, então é porque você tem um (D) e um (C) -> a sua primeira conta será atribuida o valor ao débito e a segunda ao crédito.")
    print("-----------------------------------------------")

    conta1 = input("Digite o nome da sua conta (caixa, banco, mercadoria...)")
    conta2 = input("Digite o nome da sua conta (caixa, banco, mercadoria...)")
    print("-----------------------------------------------")

    valor_c1 = float(input(f"Qual o valor que será atribuido a conta {conta1}? "))
    valor_c2 = float(input(f"Qual o valor que será atribuido a conta {conta2}? "))
    print("-----------------------------------------------")

    d1 = conta1 
    c1 = conta2

    print(f"Você tem a conta {conta1} com um valor de R${valor_c1} ")
    print(f"Você tem a conta {conta2} com um valor de R${valor_c2} ")
    print("-----------------------------------------------")

    print("O lançamento ficou:")
    print("-->")
    print(f"D - {conta1}   R$ {valor_c1}")
    print(f"C - {conta2}   R$ {valor_c2}")

  
  
  
  
   
# CORPO ---> BASE
#
# Operação(x) data xx/xx/xxx
#
# D(débito) caixa - U$$ XX.XXXX,XX
# C(Crédito) Mercadoria - U$$ XX.XXXX,XX 
#
# Valores e contas superficiais só de base
#
# Histórico - xxxxxx.... 

print(f"Operação número {numero_op} data xx/xx/xxx") # cadastrar variaveis 
print(f"")
print(f"")
print(f"")
print(f"")
print("-----------------------------------------------")

print(f"Operação número {numero_op} data xx/xx/xxx") # cadastrar variaveis 
print(f"")
print(f"")
print(f"")
print(f"")
print("-----------------------------------------------")

print(f"Operação número {numero_op} data xx/xx/xxx") # cadastrar variaveis 
print(f"")
print(f"")
print(f"")
print(f"")
print("-----------------------------------------------")
