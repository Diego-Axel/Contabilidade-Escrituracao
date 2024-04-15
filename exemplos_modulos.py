def exemplo_livro_diario():
    print("""
      
            |         LIVRO DIÁRIO          |
      
      data da operação: xx/xx/xxxx
      D - xxxx - R$ xx.xxx,xx
      C - xxxx - R$ xx.xxx,xx
      histórico: xxxxxxxxxxxx
      (Pode ter mais de uma conta de débito e crédito.)
      
    """)

def exemplo_livro_razao():
    print("""

        |         LIVRO RAZÃO           |
    
    _________________CAIXA___________________
      R$ xx.xxx,xx     |     R$ xx.xxx,xx
                       |
                       |
                       |
                       |
    ______TOTAL________|_________TOTAL________
      
    """)

def exemplo_balancete():
    print("""

             |       BALANCETE(OPCIONAL)       |
    
    ____________________________________________________
    |     CONTAS     |              SALDOS             |
    |________________|_____Débtios____|____Créditos____|
    |     Caixa      | R$ xx.xxxx,xx  |                |
    |     Banco      | R$ xx.xxxx,xx  |                |
    |   Fornecedor   |                | R$ xx.xxxx,xx  |
    |    Estoques    | R$ xx.xxxx,xx  |                | 
    |    Veículos    | R$ xx.xxxx,xx  |                |
    | Contas a pagar |                | R$ xx.xxxx,xx  |
    |________________|________________|________________|
    |______TOTAL_____|________________|_____ TOTAL_____|
    |__R$_xx.xxx,xx__|________=_______|__R$_xx.xxx,xx__|
    |________________|________________|________________|
      
    """)

