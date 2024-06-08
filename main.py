############################################################
######          ESCRITURAÇÃO CONTÁBIL BÁSICA          ######
######               OBJETIVO: TREINAR                ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RM                    ######
############################################################

'''imports'''
import os
import funcoes
import interfaces
import banco

'''programa principal'''

op_princ = ""
while op_princ != "0":
    op_princ = interfaces.menu_principal()
    print()
    if op_princ == "1":
        print()
print()
interfaces.encerramento()