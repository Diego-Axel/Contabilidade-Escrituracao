import datetime # biblioteca para puxar a data do computador
import time # da um tempo para as informações sumirem -> time.sleep(o segundo que você quiser aqui quendo dos parenteses)
import funcoes_diario

data = datetime.date.today()

dia = data.day
mes = data.month
ano = data.year

def livro_razao():
    print("oi")