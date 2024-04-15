# imports

import ascii
import datetime # biblioteca para puxar a data do computador
import os # biblioteca para interagir com o sistema operacional, estou usando para que tudo que esteja acima dela, seja removido. fica mais "limpo" de se vizualizar
import time # da um tempo para as informações sumirem -> time.sleep(o segundo que você quiser aqui quendo dos parenteses)


data = datetime.date.today()

dia = data.day
mes = data.month
ano = data.year

def livro_diario():
    os.system('clear || cls')

    print("""
     __       __  ____    ____ .______        ______       _______   __       ___      .______       __    ______   
    |  |     |  | \   \  /   / |   _  \      /  __  \     |       \ |  |     /   \     |   _  \     |  |  /  __  \  
    |  |     |  |  \   \/   /  |  |_)  |    |  |  |  |    |  .--.  ||  |    /  ^  \    |  |_)  |    |  | |  |  |  | 
    |  |     |  |   \      /   |      /     |  |  |  |    |  |  |  ||  |   /  /_\  \   |      /     |  | |  |  |  | 
    |  `----.|  |    \    /    |  |\  \----.|  `--'  |    |  '--'  ||  |  /  _____  \  |  |\  \----.|  | |  `--'  | 
    |_______||__|     \__/     | _| `._____| \______/     |_______/ |__| /__/     \__\ | _| `._____||__|  \______/ 
 
    """)

print("CARREGANDO...")
print()
time.sleep(4)
os.system('clear || cls')


# FIM DE FUNÇÕES DIÁRIO        

# OBS: Eu ainda vou fazer muito mais por aqui, mas, como ainda estou na fase de testes, estou fazendo com um tamanho reduzido.