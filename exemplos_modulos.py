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

def exemplo_balanco_patrimonial():
    print("""

            |       BALANÇO PATRIMÔNIAL       |
    ____________________________________________________
    |        ATIVOS         |         PASSIVOS         |
    |_______________________|__________________________|
    |  Caixa R$ xx.xxx,xx   |  Fornecedor R$ xx.xxx,xx |
    |  Banco R$ xx.xxx,xx   | Conta/pagar R$ xx.xxx,xx |
    | Estoques R$ xx.xxx,xx |                          |
    | Veículos R$ xx.xxx,xx |                          |
    |_______________________|__________________________|
    |                       |    PATRIMÔNIO LÍQUIDO    |
    |_______________________|__________________________|
    |                       | Cap.Social  R$ xx.xxx,xx |
    |                       |                          |
    |_______________________|__________________________|
    |___TOTAL ATIVOS (R$)___|___TOTAL PASSIVOS + PL____|
    |_______________________|__________________________|
      
    """)