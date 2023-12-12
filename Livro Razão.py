# A proposta aqui é a seguinte = quando terminado o livro diário e o usuário tiver coloado todas as suas contas, seus débitos e seus créditos bem direitinho, está na hora da outra etapa deste programa, o LIVRO RAZÃO ou RAZONETE.


# Essa etapa pegará as contas da mesma espécie, vamos chamar assim, e ira fazer uma subtração. Por exemplo, eu tenho a conta caixa aparecendo mais de uma vez no livro diário, então a gente ira fazer uma subtração usando o livro razão dessas contas caixa, que são contas da mesma espécie.


# Agora, além dessas contas da mesma espécie(Caixa, banco, fornecedor, cliente, estoque,...) também teremos o tipo dessas contas, que são justamente o Débito(D) e o Crédito(C): Que é assim que iremos fazer a subtração, colocando as contas da mesma espécie e após isso, separamos em doi lados, como se fosse um "T" o lado do débito e o lado do crédito, o D é sempre na parte superior direita do T, e o C é na outra parte, o lado superior esquerdo do T. Ficaria mais ou menos assim:


# ___(DÉBITOS)_______(NOME DA CONTA)_______(CRÉDITOS)___
#                           |       
#                           |
#                           |
#                           |
#                           |
#                           |

# Perceba que, como falado em cima, o livro razão é em formato de "T" e com as contas, ele ficaria mais ou menos assim:


# ___(DÉBITOS)_______(CAIXA)_______(CRÉDITOS)___
#  R$ 10,500,00         |  R$ 2.000,00     
#  R$ 2.000,00          |  R$ 1.500,00
#  R$ 500,00            |
#                       |
# ______________________|_______________________                   
#   SOMATORIA (D)       |  SOMATORIO (C)            
#   R$ 13.000,00        |  R$ 3.500,00
# ______________________|________________________                

# Agora para finalizar, sera feito a subtração do total dos D e o total dos C, como D>C ele a conta caixa ficará no lado dos DÉBITOS, caso C<D ele iria ficar no local dos CRÉDITOS.

# ___(DÉBITOS)_______(CAIXA)_______(CRÉDITOS)___
#  R$ 10,500,00         |  R$ 2.000,00     
#  R$ 2.000,00          |  R$ 1.500,00
#  R$ 500,00            |
#                       |
# ______________________|_______________________                   
#   SOMATORIA (D)       |  SOMATORIO (C)            
#   R$ 13.000,00        |  R$ 3.500,00
# ______________________|________________________          
#  R$ 9.500,00          |


# Bom, basicamente é assim que eu pretendo fazer ele funcionar.

# Ressalto que eu deixarei ele junto co o livro Diário, as informações dele ja será complementadas pelo livro diário, porém, como eu vou ainda fazer toda sua base aqui, vou começar fazendo ele de forma independente mesmo e ver o resultado.

# Vou criar aqui como é para acontecer quando o programa for executado e após fazer todos os testes aqui e ver se está tudo bem e certo, vou repassar para o livro diário para fazer tudo junto, enfim.



print("--------------------------------------------------")
print("|                 LIVRO RAZÃO                    |")
print("--------------------------------------------------")

conta1 = input("Digite o nome da CONTA 1 (Primeira letra maiúscula): ")
valor_conta1 = float(input(f"Digite o valor de {conta1} "))

print("--------------------------------------------------")


print(f"________________{conta1}_________________")
print(f"                  |                    ")
print(f"                  |                    ")
print(f"                  |                    ")
print(f"                  |                    ")
print(f"                  |                    ")
print("_________________________________________")
print(f"                  |                    ")

print("--------------------------------------------------")


if conta1 == "Caixa":
    conta_tipo = input("Essa conta está no DÉBITO(D) OU NO CRÉDITO(C)? ")
    if conta_tipo == "D":
        print(f"______________________________________{conta1}____________________________________")
        print(f"  R${valor_conta1}                      |                                       ")
        print(f"                                         |                                       ")
        print(f"                                         |                                       ")
        print(f"                                         |                                       ")
        print(f"                                         |                                       ")
        print("__________________________________________________________________________________")
        print(f"                                         |                                       ")
    elif conta_tipo == "C":
        print(f"______________________________________{conta1}____________________________________")
        print(f"                                         |  R${valor_conta1}                     ")
        print(f"                                         |                                       ")
        print(f"                                         |                                       ")
        print(f"                                         |                                       ")
        print(f"                                         |                                       ")
        print("__________________________________________________________________________________")
        print(f"                                         |                                       ")
    else:
        print("")
else:
    print("")

print("--------------------------------------------------")
print(f"Adicione mais valores para a conta {conta1}:")
valor_caixa = float(input(f"Valor do {conta1} "))
print("--------------------------------------------------")

conta_tipo2 = input("Essa conta está no DÉBITO(D) OU NO CRÉDITO(C)? ")

if conta_tipo2 == "D":
    print(f"______________________________________{conta1}____________________________________")
    print(f" R${valor_conta1}                        |                                       ")
    print(f" R${valor_caixa}                                       |                                       ")
    print(f"                                         |                                       ")
    print(f"                                         |                                       ")
    print(f"                                         |                                       ")
    print("__________________________________________________________________________________")
    print(f"                                         |                                       ")
elif conta_tipo == "C":
    print(f"______________________________________{conta1}____________________________________")
    print(f"                                         |  R${valor_conta1}                     ")
    print(f"                                         |                                       ")
    print(f"                                         |                                       ")
    print(f"                                         |                                       ")
    print(f"                                         |                                       ")
    print("__________________________________________________________________________________")
    print(f"                                         |                                       ")
else:
    print("")















print("--------------------------------------------------")
conta2 = input("Digite o nome da CONTA 2 (Primeira letra maiúscula): ")
