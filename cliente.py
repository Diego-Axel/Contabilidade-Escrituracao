
import os # biblioteca para que tudo que estiver acima dela suma, deixa visualmente mais limpo
import time # da um tempo para as informações sumirem -> time.sleep(o segundo que você quiser aqui quendo dos parenteses)

def usuario_existente_1():
    os.system('clear || cls')
    print("|---------------------------------|")
    print("| Você escolheu Usuário Existente |")
    print("|---------------------------------|")
    print("") 
    print("Bem vindo(a) de volta!") # quando tiver com os dados e nome da empresa ou do mei fazer com a frase apareça "Bem vindop(a) NOME"
    print("")
    print("CARREGANDO...")
    time.sleep(4)

def novo_usuario_2():
    os.system('clear || cls')
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
    nome_empresa = nome_empresa.upper() # DEIXANDO O NOME DA EMPRESA MAISCULO -> 
    print("") 
    # CPF
    cpf = input("Digite o seu CPF: ") # São string pois não vou usar esses dados para fazer operações matemáticas.
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
    endereco_empresa = endereco_empresa.upper()
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
    print("")
    time.sleep(.4)
    enter = input("APERTE ENTER PARA SAIR ")


# FIM CLIENTES