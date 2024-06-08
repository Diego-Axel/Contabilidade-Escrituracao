'''imports'''
import os
import time

'''INTERFACE MENU PRINCIPAL'''

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

'''INTERFACES DAS DEMONSTRAÇÕES'''

def livro_Diario(): # Interface do Livro Diário 
    print("""
     _    _               ___  _          _    
    | |  (_)_ ___ _ ___  |   \(_)__ _ _ _(_)___ 
    | |__| \ V / '_/ _ \ | |) | / _` | '_| / _  
    |____|_|\_/|_| \___/ |___/|_\__,_|_| |_\___/
          
    """)
    print("CARREGANDO...")
    print()
    time.sleep(.3)

'''---------------------------------------------------------------------------------------------------------------'''

def livro_razao(): # Interface do Livro Razão
    print("""
     _    _               ___                  
    | |  (_)_ ___ _ ___  | _ \__ _ _____ _ ___ 
    | |__| \ V / '_/ _ \ |   / _` |_ / _` / _  
    |____|_|\_/|_| \___/ |_|_\__,_/__\__,_\___/
                                            
    """)
    print("CARREGANDO...")
    print()
    time.sleep(.3)

'''---------------------------------------------------------------------------------------------------------------'''

def balancete(): # Interface do Balancete
    print("""
     ___      _                  _       
    | _ )__ _| |__ _ _ _  __ ___| |_ ___ 
    | _ \ _` | / _` | ' \/ _/ -_)  _/ -_)
    |___\__,_|_\__,_|_||_\__\___|\__\___|
                                      
    """)
    print("CARREGANDO...")
    print()
    time.sleep(.3)

'''---------------------------------------------------------------------------------------------------------------'''

def balanco_patrimonial(): # Interface do Balanço Patrimônial
    print("""
     ___      _                    ___      _       _                _      _ 
    | _ )__ _| |__ _ _ _  __ ___  | _ \__ _| |_ _ _(_)_ __  ___ _ _ (_)__ _| |
    | _ \ _` | / _` | ' \/ _/ _ \ |  _/ _` |  _| '_| | '  \/ _ \ ' \| / _` | |
    |___\__,_|_\__,_|_||_\__\___/ |_| \__,_|\__|_| |_|_|_|_\___/_||_|_\__,_|_|
                                                                           
    """)
    print("CARREGANDO...")
    print()
    time.sleep(.3)

'''---------------------------------------------------------------------------------------------------------------'''

'''INTERFACE SOBRE A ESCRITURAÇÃO CONTÁBIL'''

def sobre_escrituracao():
    print()


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