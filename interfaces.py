'''INTERFACES'''

'''imports'''
import os


def menu_principal(): # Interface do Menu Principal 
    os.system('clear || cls')
    print("""
     ___                 _         _      __  __
    | _ )___ _ __   __ ___)_ _  __| |___ / /_ _ \ 
    | _ \ -_) '  \  \ V / | ' \/ _` / _ \ / _` | |
    |___\___|_|_|_|  \_/|_|_||_\__,_\___/ \__,_| |
                                         \_\  /_/ 
    """)
    
    print("---------------------------------------")
    print("|        ESCRITURAÇÃO CONTÁBIL        |")
    print("|-------------------------------------|")
    print("| 1 - Cadastro de Usuario Teste :)    |")
    print("| 2 - Escrituação Contábil (Program)  |")
    print("| 3 - Exemplos das Demonstrações      |")
    print("| 4 - Sobre a Escrituração            |")
    print("| 5 - Sobre o Programa                |")
    print("| 0 - Encerrar Programa               |")
    print("---------------------------------------")
    print()
    op_princ = input("| Escolha uma opção: ")
    return op_princ
'''---------------------------------------------------------------------------------------------------------------'''


def cadastro_usuario():
    os.system("clear || cls")
    print("--------------------------------------------")
    print("|           CADASTRO DE USUÁRIO            |")
    print("--------------------------------------------")
    print("| 1 - Cadastre-se                          |")
    print("| 0 - Sair                                 |")
    print("--------------------------------------------")
    print("| OBJ: Serve somente para FeedBack(s)...   |")
    print("--------------------------------------------")
    op_usuario = input("| Escolha sua opção: ")
    return op_usuario
'''---------------------------------------------------------------------------------------------------------------'''


def sobre_escrituracao():
    os.system('clear || cls')
    print("-------------------------------------------------")
    print("|              SOBRE A ESCRITURAÇÃO             |")
    print("|-----------------------------------------------|")
    print("| Segundo o site Contablizei ->                 |")
    print("| https://www.contabilizei.com.br <-            |")
    print("|                                               |")
    print("| 'A escrituração contábil consiste no registro |")
    print("| de todos os fatos e movimentos financeiros de |")
    print("| os fatos e movimentos financeiros de uma em-  |")
    print("| presa. O objetivo é o fornecimento de infor-  |")
    print("| mações sobre o controle de patriônio empresa- |")
    print("| rial.' Neste programa, você poderá fazer uma  |")
    print("| escrituração básica completa.                 |")
    print("-------------------------------------------------")
    print()
    input("tecle <ENTER> para retornao ao menu principal ")


'''INTERFACE SOBRE O PROGRAMA'''

def sobre_programa():
    os.system('clear || cls')
    print("------------------------------------------------")
    print("|               SOBRE O PROGRAMA               |")
    print("|----------------------------------------------|")
    print("| Este é um programa feito com intuito de faz- |")
    print("| er-se uma Escrituração Contábil Báscia com-  |")
    print("| pleta passando por todas as operações inici- |")
    print("| antes vistas no 1 ano de uma faculdade de -> |")
    print("| Ciências Contábeis <-                        |")
    print("|                                              |")
    print("| Desenvolvido por: Diêgo Axel                 |")
    print("| GitHub: Diego-Axel                           |")
    print("------------------------------------------------")
    print()
    input("tecle <ENTER> para retornao ao menu principal ")


'''INTERFACE DE ENCERRAMENTO DO PROGRAMA'''

def encerramento():
    os.system('clear || cls')
    print("""
     _    _  
    | *\_/*|________   
    ||_/-\_|______  |  
    | |           | |  
    | |   0   0   | |  
    | |     -     | |    <(Bye, Bye!)
    | |   \___/   | |  
    | |___________| |  
    |_______________|  
       _|________|_    
      / ********** \   
    /  ************  \ 
   --------------------
          
    """)
    print("Você encerrou o programa. Até breve.")
    print()