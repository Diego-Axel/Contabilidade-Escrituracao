############################################################
######          ESCRITURAÇÃO CONTÁBIL BÁSICA          ######
######               OBJETIVO: TREINAR                ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RM                    ######
############################################################

'''imports'''
import interfaces
import usuario

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
                usuario.usuarios()
    elif op_princ == "2":
        pass
    elif op_princ == "3":
        pass
    elif op_princ == "4":
        interfaces.sobre_escrituracao()
    elif op_princ == "5":
        interfaces.sobre_programa()
print()
interfaces.encerramento()

'''em desenvolvimento...'''