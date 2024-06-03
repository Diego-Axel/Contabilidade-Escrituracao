############################################################
######          ESCRITURAÇÃO CONTÁBIL BÁSICA          ######
######               OBJETIVO: TREINAR                ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RM                    ######
############################################################

'''imports'''
import os
import datetime
import diario

'''datetime'''
data = datetime.date.today()
dia = data.day
mes = data.month
ano = data.year

'''código principal'''
data = float(input("Digite o valor de D: "))

dr = diario.Livro_Diario(data)