# FUNÇÃO DE INÍCIO -> ESCOLHA DO USUÁRIO:
def usuario_existente_1():
    print("|---------------------------------|")
    print("| Você escolheu Usuário Existente |")
    print("|---------------------------------|")
    print("") 
    print("Bem vindo(a) de volta!") # quando tiver com os dados e nome da empresa ou do mei fazer com a frase apareça "Bem vindop(a) NOME"
    print("")

def novo_usuario_2():
    print("|---------------------------------|")
    print("|   Você escolheu Novo Usuário    |")
    print("|---------------------------------|")
    print("") 
     # LOCAL DE CASDATRO
    print("________________________________________________________________________")
    print("|                                                                      |")
    print("|         Vamos seguir para o processo de cadastrar novo usuáriio.     |")
    print("|                                                                      |")
    print("|         Por favor, preeencha esses dados para dar continuidade.      |")
    print("|______________________________________________________________________|")
    print("")
        
    # NOME DA EMPRESA/MEI/USUARIO
    nome_empresa = input("Digite o nome da sua empresa/ou MEI: ")
    print("") 
    # CPF
    cpf = input("Digite o seu CPF: ")
    print("")  
    # CNPJ
    cnpj = input("Digite o seu cnpj: ")
    print("")
    # ENDEREÇO DE E-MAIL
    email = input("Digite o seu endereço de e-mail: ")
    print("")
    # TEL. PARA CONTATO(DA EMPRESA PREFERENCIALEMNTE) COM DDD
    telefone_empresa = input("Digite o número de telefone(da empresa preferencialmente) com DDD: ")
    print("")
    # ENDEREÇO DA EMPRESA
    endereco_empresa = input("Digite o endereço da empresa: ")
    print("")
    print("")
    print("Seus dados foram cadastrados com sucesso!")
    print("Dê uma conferida:")
    print("")
    # mostrnado os daods que o usuário introduziu no programa:
    print(" _________________________________________________")
    print("                                                  ")
    print("             Nome da empresa/ou MEI: %s           "%nome_empresa)
    print("                     CPF: %s                      "%cpf)
    print("                     CNPJ: %s                     "%cnpj)
    print("                     E-mail: %s                   "%email)
    print("              Telefone da Empresa: %s             "%telefone_empresa)
    print("              Endereço da Empresa: %s             "%endereco_empresa)
    print("__________________________________________________")

def sair_3():
    print("""




    """)