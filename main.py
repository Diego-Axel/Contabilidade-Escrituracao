############################################################
######          ESCRITURAÇÃO CONTÁBIL BÁSICA          ######
######               OBJETIVO: TREINAR                ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RM                    ######
############################################################

'''imports'''
import funcoes
import interfaces
import banco

'''programa principal'''

op_princ = ""
while op_princ != "0":
    op_princ = interfaces.menu_principal()
    print()
    if op_princ == "1":
        op_usuario = ""
        while op_usuario != "0":
            op_usuario = interfaces.cadastro_usuario()
            print()
            if op_usuario == "1":
                banco.usuarios()
print()
interfaces.encerramento()

'''em desenvolvimento...'''