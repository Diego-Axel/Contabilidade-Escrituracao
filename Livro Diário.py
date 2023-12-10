# PROGRAMA PARA SE UTILIZAR A CONTABILIDADE BÁSICA(DIÁRIO, RAZONETE, BALANECETE E BALANÇO PATRIMONIAL)

# PROJETO APENAS PARA USO PESSOAL COMO TREINAMENTO (NÃO SEI SE LEVAREI ISSO ADIANTE :D )

print("-----------------------------------------------")
print("|                LIVRO DIÁRIO                 |")
print("-----------------------------------------------")


print("-----------------------------------------------")
empresa = input("Qual o nome da sua empresa(LTda)? ")
print("-----------------------------------------------")
print(f"Empresa {empresa}, vamos fazer o levantamento do seu livro diário. ")
print("-----------------------------------------------")

# Após a pessoa ter dado o nome de sua empresa, agora chegou a hora de escolher o número de suas operações. É simples, a contabilidade tem uma linguagem única que utiliza o Débito(D) e o Crédito(C), mas esse débito e crédito não são os mesmos que são usados no nosso cotidiano, entenda aqui na contabulidade como débito=algo bom e crédito=oposto.

print("Quantas operações deseja realizar (Máximo de 10 (BETA))? ") #Ainda desenvolvendo...
numero_op = int(input(" "))
#--------------------------------------------------------------
print("-----------------------------------------------")
print("Quantas contas você deseja adicionar? ")
numero_conta = input("")
print("-----------------------------------------------")

if numero_op == 1: # É o seguinte, não sou expert em programação, então vai estar muito básico, mas espero que possam ter uma pequena amostra do que planejo fazer com esse proejto mais para frente, quando eu for aprimorando minhas habilidades e conhecimentos...
    print(f"Você escolheu {numero_op} operações. Número de contas você escolheu {numero_conta}, então é porque você tem um (D) e um (C) -> a sua primeira conta será atribuida o valor ao débito e a segunda ao crédito.")
    print("-----------------------------------------------")

    print("--------------------------------------------------")
    print("|                PRIMEIRA OPERAÇÃO               |")
    print("--------------------------------------------------")

    data1 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta1 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta2 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico1 = input("Digite o Histórico referente a esta operação: ")
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
    print("-----------------------------------------------")   
    print(f"Data da operação: {data1}")
    print(f"D - {conta1}   R$ {valor_c1}")
    print(f"C - {conta2}   R$ {valor_c2}")
    print(f"Hitórico da operação: {historico1}")
    print("-----------------------------------------------")    
elif numero_op == 2:
    print(f"Você escolheu {numero_op} operações. Número de contas você escolheu {numero_conta}, então é porque você tem um (D) e um (C) -> a sua primeira conta será atribuida o valor ao débito e a segunda ao crédito.")
    print("-----------------------------------------------")

    print("--------------------------------------------------")
    print("|                PRIMEIRA OPERAÇÃO               |")
    print("--------------------------------------------------")

    data1 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta1 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta2 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico1 = input("Digite o Histórico referente a esta operação: ")
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
    print("-----------------------------------------------")
    print(f"Data da operação: {data1}")
    print(f"D - {conta1}   R$ {valor_c1}")
    print(f"C - {conta2}   R$ {valor_c2}")
    print(f"Hitórico da operação: {historico1}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                SEGUNDA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data2 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta3 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta4 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico2 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c3 = float(input(f"Qual o valor que será atribuido a conta {conta3}? "))
    valor_c4 = float(input(f"Qual o valor que será atribuido a conta {conta4}? "))
    print("-----------------------------------------------")

    d2 = conta3 
    c2 = conta4  

    print(f"Você tem a conta {conta3} com um valor de R${valor_c3} ")
    print(f"Você tem a conta {conta4} com um valor de R${valor_c4} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data2}")
    print(f"D - {conta3}   R$ {valor_c3}")
    print(f"C - {conta4}   R$ {valor_c4}")
    print(f"Hitórico da operação: {historico2}")
    print("-----------------------------------------------")
elif numero_op == 3:
    print(f"Você escolheu {numero_op} operações. Número de contas você escolheu {numero_conta}, então é porque você tem um (D) e um (C) -> a sua primeira conta será atribuida o valor ao débito e a segunda ao crédito.")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                PRIMEIRA OPERAÇÃO               |")
    print("--------------------------------------------------")

    data1 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta1 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta2 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico1 = input("Digite o Histórico referente a esta operação: ")
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
    print("-----------------------------------------------")
    print(f"Data da operação: {data1}")
    print(f"D - {conta1}   R$ {valor_c1}")
    print(f"C - {conta2}   R$ {valor_c2}")
    print(f"Hitórico da operação: {historico1}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                SEGUNDA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data2 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta3 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta4 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico2 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c3 = float(input(f"Qual o valor que será atribuido a conta {conta3}? "))
    valor_c4 = float(input(f"Qual o valor que será atribuido a conta {conta4}? "))
    print("-----------------------------------------------")

    d2 = conta3 
    c2 = conta4  

    print(f"Você tem a conta {conta3} com um valor de R${valor_c3} ")
    print(f"Você tem a conta {conta4} com um valor de R${valor_c4} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data2}")
    print(f"D - {conta3}   R$ {valor_c3}")
    print(f"C - {conta4}   R$ {valor_c4}")
    print(f"Hitórico da operação: {historico2}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                TERCEIRA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data3 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta5 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta6 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico3 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c5 = float(input(f"Qual o valor que será atribuido a conta {conta5}? "))
    valor_c6 = float(input(f"Qual o valor que será atribuido a conta {conta6}? "))
    print("-----------------------------------------------")

    d3 = conta5 
    c3 = conta6  

    print(f"Você tem a conta {conta5} com um valor de R${valor_c5} ")
    print(f"Você tem a conta {conta6} com um valor de R${valor_c6} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data3}")
    print(f"D - {conta5}   R$ {valor_c5}")
    print(f"C - {conta6}   R$ {valor_c6}")
    print(f"Hitórico da operação: {historico3}")
    print("-----------------------------------------------")
elif numero_op == 4:
    print(f"Você escolheu {numero_op} operações. Número de contas você escolheu {numero_conta}, então é porque você tem um (D) e um (C) -> a sua primeira conta será atribuida o valor ao débito e a segunda ao crédito.")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                PRIMEIRA OPERAÇÃO               |")
    print("--------------------------------------------------")

    data1 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta1 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta2 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico1 = input("Digite o Histórico referente a esta operação: ")
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
    print("-----------------------------------------------")
    print(f"Data da operação: {data1}")
    print(f"D - {conta1}   R$ {valor_c1}")
    print(f"C - {conta2}   R$ {valor_c2}")
    print(f"Hitórico da operação: {historico1}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                SEGUNDA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data2 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta3 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta4 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico2 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c3 = float(input(f"Qual o valor que será atribuido a conta {conta3}? "))
    valor_c4 = float(input(f"Qual o valor que será atribuido a conta {conta4}? "))
    print("-----------------------------------------------")

    d2 = conta3 
    c2 = conta4  

    print(f"Você tem a conta {conta3} com um valor de R${valor_c3} ")
    print(f"Você tem a conta {conta4} com um valor de R${valor_c4} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data2}")
    print(f"D - {conta3}   R$ {valor_c3}")
    print(f"C - {conta4}   R$ {valor_c4}")
    print(f"Hitórico da operação: {historico2}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                TERCEIRA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data3 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta5 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta6 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico3 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c5 = float(input(f"Qual o valor que será atribuido a conta {conta5}? "))
    valor_c6 = float(input(f"Qual o valor que será atribuido a conta {conta6}? "))
    print("-----------------------------------------------")

    d3 = conta5 
    c3 = conta6  

    print(f"Você tem a conta {conta5} com um valor de R${valor_c5} ")
    print(f"Você tem a conta {conta6} com um valor de R${valor_c6} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data3}")
    print(f"D - {conta5}   R$ {valor_c5}")
    print(f"C - {conta6}   R$ {valor_c6}")
    print(f"Hitórico da operação: {historico3}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                QUARTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data4 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta7 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta8 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico4 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c7 = float(input(f"Qual o valor que será atribuido a conta {conta7}? "))
    valor_c8 = float(input(f"Qual o valor que será atribuido a conta {conta8}? "))
    print("-----------------------------------------------")

    d4 = conta7 
    c4 = conta8  

    print(f"Você tem a conta {conta7} com um valor de R${valor_c7} ")
    print(f"Você tem a conta {conta8} com um valor de R${valor_c8} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data4}")
    print(f"D - {conta7}   R$ {valor_c7}")
    print(f"C - {conta8}   R$ {valor_c8}")
    print(f"Hitórico da operação: {historico4}")
    print("-----------------------------------------------")
elif numero_op == 5:
    print(f"Você escolheu {numero_op} operações. Número de contas você escolheu {numero_conta}, então é porque você tem um (D) e um (C) -> a sua primeira conta será atribuida o valor ao débito e a segunda ao crédito.")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                PRIMEIRA OPERAÇÃO               |")
    print("--------------------------------------------------")

    data1 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta1 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta2 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico1 = input("Digite o Histórico referente a esta operação: ")
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
    print("-----------------------------------------------")
    print(f"Data da operação: {data1}")
    print(f"D - {conta1}   R$ {valor_c1}")
    print(f"C - {conta2}   R$ {valor_c2}")
    print(f"Hitórico da operação: {historico1}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                SEGUNDA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data2 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta3 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta4 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico2 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c3 = float(input(f"Qual o valor que será atribuido a conta {conta3}? "))
    valor_c4 = float(input(f"Qual o valor que será atribuido a conta {conta4}? "))
    print("-----------------------------------------------")

    d2 = conta3 
    c2 = conta4  

    print(f"Você tem a conta {conta3} com um valor de R${valor_c3} ")
    print(f"Você tem a conta {conta4} com um valor de R${valor_c4} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data2}")
    print(f"D - {conta3}   R$ {valor_c3}")
    print(f"C - {conta4}   R$ {valor_c4}")
    print(f"Hitórico da operação: {historico2}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                TERCEIRA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data3 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta5 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta6 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico3 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c5 = float(input(f"Qual o valor que será atribuido a conta {conta5}? "))
    valor_c6 = float(input(f"Qual o valor que será atribuido a conta {conta6}? "))
    print("-----------------------------------------------")

    d3 = conta5 
    c3 = conta6  

    print(f"Você tem a conta {conta5} com um valor de R${valor_c5} ")
    print(f"Você tem a conta {conta6} com um valor de R${valor_c6} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data3}")
    print(f"D - {conta5}   R$ {valor_c5}")
    print(f"C - {conta6}   R$ {valor_c6}")
    print(f"Hitórico da operação: {historico3}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                QUARTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data4 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta7 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta8 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico4 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c7 = float(input(f"Qual o valor que será atribuido a conta {conta7}? "))
    valor_c8 = float(input(f"Qual o valor que será atribuido a conta {conta8}? "))
    print("-----------------------------------------------")

    d4 = conta7 
    c4 = conta8  

    print(f"Você tem a conta {conta7} com um valor de R${valor_c7} ")
    print(f"Você tem a conta {conta8} com um valor de R${valor_c8} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data4}")
    print(f"D - {conta7}   R$ {valor_c7}")
    print(f"C - {conta8}   R$ {valor_c8}")
    print(f"Hitórico da operação: {historico4}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                QUINTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data5 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta9 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta10 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico5 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c9 = float(input(f"Qual o valor que será atribuido a conta {conta9}? "))
    valor_c10 = float(input(f"Qual o valor que será atribuido a conta {conta10}? "))
    print("-----------------------------------------------")

    d5 = conta9 
    c5 = conta10  

    print(f"Você tem a conta {conta9} com um valor de R${valor_c9} ")
    print(f"Você tem a conta {conta10} com um valor de R${valor_c10} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data5}")
    print(f"D - {conta9}   R$ {valor_c9}")
    print(f"C - {conta10}   R$ {valor_c10}")
    print(f"Hitórico da operação: {historico5}")
    print("-----------------------------------------------")
elif numero_op == 6:
    print(f"Você escolheu {numero_op} operações. Número de contas você escolheu {numero_conta}, então é porque você tem um (D) e um (C) -> a sua primeira conta será atribuida o valor ao débito e a segunda ao crédito.")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                PRIMEIRA OPERAÇÃO               |")
    print("--------------------------------------------------")

    data1 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta1 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta2 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico1 = input("Digite o Histórico referente a esta operação: ")
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
    print("-----------------------------------------------")
    print(f"Data da operação: {data1}")
    print(f"D - {conta1}   R$ {valor_c1}")
    print(f"C - {conta2}   R$ {valor_c2}")
    print(f"Hitórico da operação: {historico1}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                SEGUNDA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data2 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta3 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta4 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico2 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c3 = float(input(f"Qual o valor que será atribuido a conta {conta3}? "))
    valor_c4 = float(input(f"Qual o valor que será atribuido a conta {conta4}? "))
    print("-----------------------------------------------")

    d2 = conta3 
    c2 = conta4  

    print(f"Você tem a conta {conta3} com um valor de R${valor_c3} ")
    print(f"Você tem a conta {conta4} com um valor de R${valor_c4} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data2}")
    print(f"D - {conta3}   R$ {valor_c3}")
    print(f"C - {conta4}   R$ {valor_c4}")
    print(f"Hitórico da operação: {historico2}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                TERCEIRA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data3 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta5 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta6 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico3 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c5 = float(input(f"Qual o valor que será atribuido a conta {conta5}? "))
    valor_c6 = float(input(f"Qual o valor que será atribuido a conta {conta6}? "))
    print("-----------------------------------------------")

    d3 = conta5 
    c3 = conta6  

    print(f"Você tem a conta {conta5} com um valor de R${valor_c5} ")
    print(f"Você tem a conta {conta6} com um valor de R${valor_c6} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data3}")
    print(f"D - {conta5}   R$ {valor_c5}")
    print(f"C - {conta6}   R$ {valor_c6}")
    print(f"Hitórico da operação: {historico3}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                QUARTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data4 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta7 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta8 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico4 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c7 = float(input(f"Qual o valor que será atribuido a conta {conta7}? "))
    valor_c8 = float(input(f"Qual o valor que será atribuido a conta {conta8}? "))
    print("-----------------------------------------------")

    d4 = conta7 
    c4 = conta8  

    print(f"Você tem a conta {conta7} com um valor de R${valor_c7} ")
    print(f"Você tem a conta {conta8} com um valor de R${valor_c8} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data4}")
    print(f"D - {conta7}   R$ {valor_c7}")
    print(f"C - {conta8}   R$ {valor_c8}")
    print(f"Hitórico da operação: {historico4}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                QUINTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data5 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta9 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta10 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico5 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c9 = float(input(f"Qual o valor que será atribuido a conta {conta9}? "))
    valor_c10 = float(input(f"Qual o valor que será atribuido a conta {conta10}? "))
    print("-----------------------------------------------")

    d5 = conta9 
    c5 = conta10  

    print(f"Você tem a conta {conta9} com um valor de R${valor_c9} ")
    print(f"Você tem a conta {conta10} com um valor de R${valor_c10} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data5}")
    print(f"D - {conta9}   R$ {valor_c9}")
    print(f"C - {conta10}   R$ {valor_c10}")
    print(f"Hitórico da operação: {historico5}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                 SEXTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data6 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta11 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta12 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico6 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c11 = float(input(f"Qual o valor que será atribuido a conta {conta11}? "))
    valor_c12 = float(input(f"Qual o valor que será atribuido a conta {conta12}? "))
    print("-----------------------------------------------")

    d6 = conta11 
    c6 = conta12  

    print(f"Você tem a conta {conta11} com um valor de R${valor_c11} ")
    print(f"Você tem a conta {conta12} com um valor de R${valor_c12} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data6}")
    print(f"D - {conta11}   R$ {valor_c11}")
    print(f"C - {conta12}   R$ {valor_c12}")
    print(f"Hitórico da operação: {historico6}")
    print("-----------------------------------------------")
elif numero_op == 7:
    print(f"Você escolheu {numero_op} operações. Número de contas você escolheu {numero_conta}, então é porque você tem um (D) e um (C) -> a sua primeira conta será atribuida o valor ao débito e a segunda ao crédito.")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                PRIMEIRA OPERAÇÃO               |")
    print("--------------------------------------------------")

    data1 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta1 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta2 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico1 = input("Digite o Histórico referente a esta operação: ")
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
    print("-----------------------------------------------")
    print(f"Data da operação: {data1}")
    print(f"D - {conta1}   R$ {valor_c1}")
    print(f"C - {conta2}   R$ {valor_c2}")
    print(f"Hitórico da operação: {historico1}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                SEGUNDA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data2 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta3 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta4 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico2 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c3 = float(input(f"Qual o valor que será atribuido a conta {conta3}? "))
    valor_c4 = float(input(f"Qual o valor que será atribuido a conta {conta4}? "))
    print("-----------------------------------------------")

    d2 = conta3 
    c2 = conta4  

    print(f"Você tem a conta {conta3} com um valor de R${valor_c3} ")
    print(f"Você tem a conta {conta4} com um valor de R${valor_c4} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data2}")
    print(f"D - {conta3}   R$ {valor_c3}")
    print(f"C - {conta4}   R$ {valor_c4}")
    print(f"Hitórico da operação: {historico2}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                TERCEIRA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data3 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta5 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta6 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico3 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c5 = float(input(f"Qual o valor que será atribuido a conta {conta5}? "))
    valor_c6 = float(input(f"Qual o valor que será atribuido a conta {conta6}? "))
    print("-----------------------------------------------")

    d3 = conta5 
    c3 = conta6  

    print(f"Você tem a conta {conta5} com um valor de R${valor_c5} ")
    print(f"Você tem a conta {conta6} com um valor de R${valor_c6} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data3}")
    print(f"D - {conta5}   R$ {valor_c5}")
    print(f"C - {conta6}   R$ {valor_c6}")
    print(f"Hitórico da operação: {historico3}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                QUARTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data4 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta7 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta8 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico4 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c7 = float(input(f"Qual o valor que será atribuido a conta {conta7}? "))
    valor_c8 = float(input(f"Qual o valor que será atribuido a conta {conta8}? "))
    print("-----------------------------------------------")

    d4 = conta7 
    c4 = conta8  

    print(f"Você tem a conta {conta7} com um valor de R${valor_c7} ")
    print(f"Você tem a conta {conta8} com um valor de R${valor_c8} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data4}")
    print(f"D - {conta7}   R$ {valor_c7}")
    print(f"C - {conta8}   R$ {valor_c8}")
    print(f"Hitórico da operação: {historico4}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                QUINTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data5 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta9 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta10 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico5 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c9 = float(input(f"Qual o valor que será atribuido a conta {conta9}? "))
    valor_c10 = float(input(f"Qual o valor que será atribuido a conta {conta10}? "))
    print("-----------------------------------------------")

    d5 = conta9 
    c5 = conta10  

    print(f"Você tem a conta {conta9} com um valor de R${valor_c9} ")
    print(f"Você tem a conta {conta10} com um valor de R${valor_c10} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data5}")
    print(f"D - {conta9}   R$ {valor_c9}")
    print(f"C - {conta10}   R$ {valor_c10}")
    print(f"Hitórico da operação: {historico5}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                 SEXTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data6 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta11 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta12 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico6 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c11 = float(input(f"Qual o valor que será atribuido a conta {conta11}? "))
    valor_c12 = float(input(f"Qual o valor que será atribuido a conta {conta12}? "))
    print("-----------------------------------------------")

    d6 = conta11 
    c6 = conta12  

    print(f"Você tem a conta {conta11} com um valor de R${valor_c11} ")
    print(f"Você tem a conta {conta12} com um valor de R${valor_c12} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data6}")
    print(f"D - {conta11}   R$ {valor_c11}")
    print(f"C - {conta12}   R$ {valor_c12}")
    print(f"Hitórico da operação: {historico6}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                SÉTIMA OPERAÇÃO                  |")
    print("--------------------------------------------------")

    data7 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta13 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta14 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico7 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c13 = float(input(f"Qual o valor que será atribuido a conta {conta13}? "))
    valor_c14 = float(input(f"Qual o valor que será atribuido a conta {conta14}? "))
    print("-----------------------------------------------")

    d7 = conta13 
    c7 = conta14  

    print(f"Você tem a conta {conta13} com um valor de R${valor_c13} ")
    print(f"Você tem a conta {conta14} com um valor de R${valor_c14} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data7}")
    print(f"D - {conta13}   R$ {valor_c13}")
    print(f"C - {conta14}   R$ {valor_c14}")
    print(f"Hitórico da operação: {historico7}")
    print("-----------------------------------------------")
elif numero_op == 8:
    print(f"Você escolheu {numero_op} operações. Número de contas você escolheu {numero_conta}, então é porque você tem um (D) e um (C) -> a sua primeira conta será atribuida o valor ao débito e a segunda ao crédito.")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                PRIMEIRA OPERAÇÃO               |")
    print("--------------------------------------------------")

    data1 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta1 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta2 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico1 = input("Digite o Histórico referente a esta operação: ")
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
    print("-----------------------------------------------")
    print(f"Data da operação: {data1}")
    print(f"D - {conta1}   R$ {valor_c1}")
    print(f"C - {conta2}   R$ {valor_c2}")
    print(f"Hitórico da operação: {historico1}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                SEGUNDA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data2 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta3 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta4 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico2 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c3 = float(input(f"Qual o valor que será atribuido a conta {conta3}? "))
    valor_c4 = float(input(f"Qual o valor que será atribuido a conta {conta4}? "))
    print("-----------------------------------------------")

    d2 = conta3 
    c2 = conta4  

    print(f"Você tem a conta {conta3} com um valor de R${valor_c3} ")
    print(f"Você tem a conta {conta4} com um valor de R${valor_c4} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data2}")
    print(f"D - {conta3}   R$ {valor_c3}")
    print(f"C - {conta4}   R$ {valor_c4}")
    print(f"Hitórico da operação: {historico2}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                TERCEIRA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data3 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta5 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta6 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico3 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c5 = float(input(f"Qual o valor que será atribuido a conta {conta5}? "))
    valor_c6 = float(input(f"Qual o valor que será atribuido a conta {conta6}? "))
    print("-----------------------------------------------")

    d3 = conta5 
    c3 = conta6  

    print(f"Você tem a conta {conta5} com um valor de R${valor_c5} ")
    print(f"Você tem a conta {conta6} com um valor de R${valor_c6} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data3}")
    print(f"D - {conta5}   R$ {valor_c5}")
    print(f"C - {conta6}   R$ {valor_c6}")
    print(f"Hitórico da operação: {historico3}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                QUARTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data4 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta7 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta8 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico4 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c7 = float(input(f"Qual o valor que será atribuido a conta {conta7}? "))
    valor_c8 = float(input(f"Qual o valor que será atribuido a conta {conta8}? "))
    print("-----------------------------------------------")

    d4 = conta7 
    c4 = conta8  

    print(f"Você tem a conta {conta7} com um valor de R${valor_c7} ")
    print(f"Você tem a conta {conta8} com um valor de R${valor_c8} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data4}")
    print(f"D - {conta7}   R$ {valor_c7}")
    print(f"C - {conta8}   R$ {valor_c8}")
    print(f"Hitórico da operação: {historico4}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                QUINTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data5 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta9 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta10 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico5 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c9 = float(input(f"Qual o valor que será atribuido a conta {conta9}? "))
    valor_c10 = float(input(f"Qual o valor que será atribuido a conta {conta10}? "))
    print("-----------------------------------------------")

    d5 = conta9 
    c5 = conta10  

    print(f"Você tem a conta {conta9} com um valor de R${valor_c9} ")
    print(f"Você tem a conta {conta10} com um valor de R${valor_c10} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data5}")
    print(f"D - {conta9}   R$ {valor_c9}")
    print(f"C - {conta10}   R$ {valor_c10}")
    print(f"Hitórico da operação: {historico5}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                 SEXTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data6 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta11 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta12 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico6 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c11 = float(input(f"Qual o valor que será atribuido a conta {conta11}? "))
    valor_c12 = float(input(f"Qual o valor que será atribuido a conta {conta12}? "))
    print("-----------------------------------------------")

    d6 = conta11 
    c6 = conta12  

    print(f"Você tem a conta {conta11} com um valor de R${valor_c11} ")
    print(f"Você tem a conta {conta12} com um valor de R${valor_c12} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data6}")
    print(f"D - {conta11}   R$ {valor_c11}")
    print(f"C - {conta12}   R$ {valor_c12}")
    print(f"Hitórico da operação: {historico6}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                SÉTIMA OPERAÇÃO                  |")
    print("--------------------------------------------------")

    data7 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta13 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta14 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico7 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c13 = float(input(f"Qual o valor que será atribuido a conta {conta13}? "))
    valor_c14 = float(input(f"Qual o valor que será atribuido a conta {conta14}? "))
    print("-----------------------------------------------")

    d7 = conta13 
    c7 = conta14  

    print(f"Você tem a conta {conta13} com um valor de R${valor_c13} ")
    print(f"Você tem a conta {conta14} com um valor de R${valor_c14} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data7}")
    print(f"D - {conta13}   R$ {valor_c13}")
    print(f"C - {conta14}   R$ {valor_c14}")
    print(f"Hitórico da operação: {historico7}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                 OITAVA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data8 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta15 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta16 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico8 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c15 = float(input(f"Qual o valor que será atribuido a conta {conta15}? "))
    valor_c16 = float(input(f"Qual o valor que será atribuido a conta {conta16}? "))
    print("-----------------------------------------------")

    d8 = conta15 
    c8 = conta16  

    print(f"Você tem a conta {conta15} com um valor de R${valor_c15} ")
    print(f"Você tem a conta {conta16} com um valor de R${valor_c16} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data8}")
    print(f"D - {conta15}   R$ {valor_c15}")
    print(f"C - {conta16}   R$ {valor_c16}")
    print(f"Hitórico da operação: {historico8}")
    print("-----------------------------------------------")
elif numero_op == 9:
    print(f"Você escolheu {numero_op} operações. Número de contas você escolheu {numero_conta}, então é porque você tem um (D) e um (C) -> a sua primeira conta será atribuida o valor ao débito e a segunda ao crédito.")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                PRIMEIRA OPERAÇÃO               |")
    print("--------------------------------------------------")

    data1 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta1 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta2 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico1 = input("Digite o Histórico referente a esta operação: ")
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
    print("-----------------------------------------------")
    print(f"Data da operação: {data1}")
    print(f"D - {conta1}   R$ {valor_c1}")
    print(f"C - {conta2}   R$ {valor_c2}")
    print(f"Hitórico da operação: {historico1}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                SEGUNDA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data2 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta3 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta4 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico2 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c3 = float(input(f"Qual o valor que será atribuido a conta {conta3}? "))
    valor_c4 = float(input(f"Qual o valor que será atribuido a conta {conta4}? "))
    print("-----------------------------------------------")

    d2 = conta3 
    c2 = conta4  

    print(f"Você tem a conta {conta3} com um valor de R${valor_c3} ")
    print(f"Você tem a conta {conta4} com um valor de R${valor_c4} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data2}")
    print(f"D - {conta3}   R$ {valor_c3}")
    print(f"C - {conta4}   R$ {valor_c4}")
    print(f"Hitórico da operação: {historico2}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                TERCEIRA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data3 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta5 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta6 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico3 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c5 = float(input(f"Qual o valor que será atribuido a conta {conta5}? "))
    valor_c6 = float(input(f"Qual o valor que será atribuido a conta {conta6}? "))
    print("-----------------------------------------------")

    d3 = conta5 
    c3 = conta6  

    print(f"Você tem a conta {conta5} com um valor de R${valor_c5} ")
    print(f"Você tem a conta {conta6} com um valor de R${valor_c6} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data3}")
    print(f"D - {conta5}   R$ {valor_c5}")
    print(f"C - {conta6}   R$ {valor_c6}")
    print(f"Hitórico da operação: {historico3}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                QUARTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data4 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta7 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta8 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico4 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c7 = float(input(f"Qual o valor que será atribuido a conta {conta7}? "))
    valor_c8 = float(input(f"Qual o valor que será atribuido a conta {conta8}? "))
    print("-----------------------------------------------")

    d4 = conta7 
    c4 = conta8  

    print(f"Você tem a conta {conta7} com um valor de R${valor_c7} ")
    print(f"Você tem a conta {conta8} com um valor de R${valor_c8} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data4}")
    print(f"D - {conta7}   R$ {valor_c7}")
    print(f"C - {conta8}   R$ {valor_c8}")
    print(f"Hitórico da operação: {historico4}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                QUINTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data5 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta9 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta10 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico5 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c9 = float(input(f"Qual o valor que será atribuido a conta {conta9}? "))
    valor_c10 = float(input(f"Qual o valor que será atribuido a conta {conta10}? "))
    print("-----------------------------------------------")

    d5 = conta9 
    c5 = conta10  

    print(f"Você tem a conta {conta9} com um valor de R${valor_c9} ")
    print(f"Você tem a conta {conta10} com um valor de R${valor_c10} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data5}")
    print(f"D - {conta9}   R$ {valor_c9}")
    print(f"C - {conta10}   R$ {valor_c10}")
    print(f"Hitórico da operação: {historico5}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                 SEXTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data6 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta11 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta12 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico6 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c11 = float(input(f"Qual o valor que será atribuido a conta {conta11}? "))
    valor_c12 = float(input(f"Qual o valor que será atribuido a conta {conta12}? "))
    print("-----------------------------------------------")

    d6 = conta11 
    c6 = conta12  

    print(f"Você tem a conta {conta11} com um valor de R${valor_c11} ")
    print(f"Você tem a conta {conta12} com um valor de R${valor_c12} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data6}")
    print(f"D - {conta11}   R$ {valor_c11}")
    print(f"C - {conta12}   R$ {valor_c12}")
    print(f"Hitórico da operação: {historico6}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                SÉTIMA OPERAÇÃO                  |")
    print("--------------------------------------------------")

    data7 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta13 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta14 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico7 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c13 = float(input(f"Qual o valor que será atribuido a conta {conta13}? "))
    valor_c14 = float(input(f"Qual o valor que será atribuido a conta {conta14}? "))
    print("-----------------------------------------------")

    d7 = conta13 
    c7 = conta14  

    print(f"Você tem a conta {conta13} com um valor de R${valor_c13} ")
    print(f"Você tem a conta {conta14} com um valor de R${valor_c14} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data7}")
    print(f"D - {conta13}   R$ {valor_c13}")
    print(f"C - {conta14}   R$ {valor_c14}")
    print(f"Hitórico da operação: {historico7}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                 OITAVA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data8 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta15 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta16 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico8 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c15 = float(input(f"Qual o valor que será atribuido a conta {conta15}? "))
    valor_c16 = float(input(f"Qual o valor que será atribuido a conta {conta16}? "))
    print("-----------------------------------------------")

    d8 = conta15 
    c8 = conta16  

    print(f"Você tem a conta {conta15} com um valor de R${valor_c15} ")
    print(f"Você tem a conta {conta16} com um valor de R${valor_c16} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data8}")
    print(f"D - {conta15}   R$ {valor_c15}")
    print(f"C - {conta16}   R$ {valor_c16}")
    print(f"Hitórico da operação: {historico8}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                 NONA OPERAÇÃO                  |")
    print("--------------------------------------------------")

    data9 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta17 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta18 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico9 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c17 = float(input(f"Qual o valor que será atribuido a conta {conta17}? "))
    valor_c18 = float(input(f"Qual o valor que será atribuido a conta {conta18}? "))
    print("-----------------------------------------------")

    d9 = conta17 
    c9 = conta18  

    print(f"Você tem a conta {conta17} com um valor de R${valor_c17} ")
    print(f"Você tem a conta {conta18} com um valor de R${valor_c18} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data9}")
    print(f"D - {conta17}   R$ {valor_c17}")
    print(f"C - {conta18}   R$ {valor_c18}")
    print(f"Hitórico da operação: {historico9}")
    print("-----------------------------------------------")
elif numero_op == 10:
    print(f"Você escolheu {numero_op} operações. Número de contas você escolheu {numero_conta}, então é porque você tem um (D) e um (C) -> a sua primeira conta será atribuida o valor ao débito e a segunda ao crédito.")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                PRIMEIRA OPERAÇÃO               |")
    print("--------------------------------------------------")

    data1 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta1 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta2 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico1 = input("Digite o Histórico referente a esta operação: ")
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
    print("-----------------------------------------------")
    print(f"Data da operação: {data1}")
    print(f"D - {conta1}   R$ {valor_c1}")
    print(f"C - {conta2}   R$ {valor_c2}")
    print(f"Hitórico da operação: {historico1}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                SEGUNDA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data2 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta3 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta4 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico2 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c3 = float(input(f"Qual o valor que será atribuido a conta {conta3}? "))
    valor_c4 = float(input(f"Qual o valor que será atribuido a conta {conta4}? "))
    print("-----------------------------------------------")

    d2 = conta3 
    c2 = conta4  

    print(f"Você tem a conta {conta3} com um valor de R${valor_c3} ")
    print(f"Você tem a conta {conta4} com um valor de R${valor_c4} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data2}")
    print(f"D - {conta3}   R$ {valor_c3}")
    print(f"C - {conta4}   R$ {valor_c4}")
    print(f"Hitórico da operação: {historico2}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                TERCEIRA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data3 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta5 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta6 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico3 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c5 = float(input(f"Qual o valor que será atribuido a conta {conta5}? "))
    valor_c6 = float(input(f"Qual o valor que será atribuido a conta {conta6}? "))
    print("-----------------------------------------------")

    d3 = conta5 
    c3 = conta6  

    print(f"Você tem a conta {conta5} com um valor de R${valor_c5} ")
    print(f"Você tem a conta {conta6} com um valor de R${valor_c6} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data3}")
    print(f"D - {conta5}   R$ {valor_c5}")
    print(f"C - {conta6}   R$ {valor_c6}")
    print(f"Hitórico da operação: {historico3}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                QUARTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data4 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta7 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta8 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico4 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c7 = float(input(f"Qual o valor que será atribuido a conta {conta7}? "))
    valor_c8 = float(input(f"Qual o valor que será atribuido a conta {conta8}? "))
    print("-----------------------------------------------")

    d4 = conta7 
    c4 = conta8  

    print(f"Você tem a conta {conta7} com um valor de R${valor_c7} ")
    print(f"Você tem a conta {conta8} com um valor de R${valor_c8} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data4}")
    print(f"D - {conta7}   R$ {valor_c7}")
    print(f"C - {conta8}   R$ {valor_c8}")
    print(f"Hitórico da operação: {historico4}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                QUINTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data5 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta9 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta10 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico5 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c9 = float(input(f"Qual o valor que será atribuido a conta {conta9}? "))
    valor_c10 = float(input(f"Qual o valor que será atribuido a conta {conta10}? "))
    print("-----------------------------------------------")

    d5 = conta9 
    c5 = conta10  

    print(f"Você tem a conta {conta9} com um valor de R${valor_c9} ")
    print(f"Você tem a conta {conta10} com um valor de R${valor_c10} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data5}")
    print(f"D - {conta9}   R$ {valor_c9}")
    print(f"C - {conta10}   R$ {valor_c10}")
    print(f"Hitórico da operação: {historico5}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                 SEXTA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data6 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta11 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta12 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico6 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c11 = float(input(f"Qual o valor que será atribuido a conta {conta11}? "))
    valor_c12 = float(input(f"Qual o valor que será atribuido a conta {conta12}? "))
    print("-----------------------------------------------")

    d6 = conta11 
    c6 = conta12  

    print(f"Você tem a conta {conta11} com um valor de R${valor_c11} ")
    print(f"Você tem a conta {conta12} com um valor de R${valor_c12} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data6}")
    print(f"D - {conta11}   R$ {valor_c11}")
    print(f"C - {conta12}   R$ {valor_c12}")
    print(f"Hitórico da operação: {historico6}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                SÉTIMA OPERAÇÃO                  |")
    print("--------------------------------------------------")

    data7 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta13 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta14 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico7 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c13 = float(input(f"Qual o valor que será atribuido a conta {conta13}? "))
    valor_c14 = float(input(f"Qual o valor que será atribuido a conta {conta14}? "))
    print("-----------------------------------------------")

    d7 = conta13 
    c7 = conta14  

    print(f"Você tem a conta {conta13} com um valor de R${valor_c13} ")
    print(f"Você tem a conta {conta14} com um valor de R${valor_c14} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data7}")
    print(f"D - {conta13}   R$ {valor_c13}")
    print(f"C - {conta14}   R$ {valor_c14}")
    print(f"Hitórico da operação: {historico7}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                 OITAVA OPERAÇÃO                |")
    print("--------------------------------------------------")

    data8 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta15 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta16 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico8 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c15 = float(input(f"Qual o valor que será atribuido a conta {conta15}? "))
    valor_c16 = float(input(f"Qual o valor que será atribuido a conta {conta16}? "))
    print("-----------------------------------------------")

    d8 = conta15 
    c8 = conta16  

    print(f"Você tem a conta {conta15} com um valor de R${valor_c15} ")
    print(f"Você tem a conta {conta16} com um valor de R${valor_c16} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data8}")
    print(f"D - {conta15}   R$ {valor_c15}")
    print(f"C - {conta16}   R$ {valor_c16}")
    print(f"Hitórico da operação: {historico8}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                 NONA OPERAÇÃO                  |")
    print("--------------------------------------------------")

    data9 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta17 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta18 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico9 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c17 = float(input(f"Qual o valor que será atribuido a conta {conta17}? "))
    valor_c18 = float(input(f"Qual o valor que será atribuido a conta {conta18}? "))
    print("-----------------------------------------------")

    d9 = conta17 
    c9 = conta18  

    print(f"Você tem a conta {conta17} com um valor de R${valor_c17} ")
    print(f"Você tem a conta {conta18} com um valor de R${valor_c18} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data9}")
    print(f"D - {conta17}   R$ {valor_c17}")
    print(f"C - {conta18}   R$ {valor_c18}")
    print(f"Hitórico da operação: {historico9}")
    print("-----------------------------------------------")


    print("--------------------------------------------------")
    print("|                 DÉCIMA OPERAÇÃO                 |")
    print("--------------------------------------------------")

    data10 = input("Digite a data desta operação -> xx/xx/xxxx: ")
    conta19 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    conta20 = input("Digite o nome da sua conta (caixa, banco, mercadoria...) ")
    historico10 = input("Digite o Histórico referente a esta operação: ")
    print("-----------------------------------------------")

    valor_c19 = float(input(f"Qual o valor que será atribuido a conta {conta19}? "))
    valor_c20 = float(input(f"Qual o valor que será atribuido a conta {conta20}? "))
    print("-----------------------------------------------")

    d10 = conta19 
    c10 = conta20  

    print(f"Você tem a conta {conta19} com um valor de R${valor_c19} ")
    print(f"Você tem a conta {conta20} com um valor de R${valor_c20} ")
    print("-----------------------------------------------")  
    
    print("O lançamento ficou:")
    print("-----------------------------------------------")
    print(f"Data da operação: {data10}")
    print(f"D - {conta19}   R$ {valor_c19}")
    print(f"C - {conta20}   R$ {valor_c20}")
    print(f"Hitórico da operação: {historico10}")
    print("-----------------------------------------------")
else:
    print("END")


print(f" Empresa {empresa}, agora vamos dar continuidade ao Livro Razão(RAZONETE) ")




   
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

# print(f"Operação número {numero_op} data xx/xx/xxx") # cadastrar variaveis 
# print(f"")
# print(f"")
# print(f"")
# print(f"")
# print("-----------------------------------------------")

# print(f"Operação número {numero_op} data xx/xx/xxx") # cadastrar variaveis 
# print(f"")
# print(f"")
# print(f"")
# print(f"")
# print("-----------------------------------------------")

# print(f"Operação número {numero_op} data xx/xx/xxx") # cadastrar variaveis 
# print(f"")
# print(f"")
# print(f"")
# print(f"")
# print("-----------------------------------------------")