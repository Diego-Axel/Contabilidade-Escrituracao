# Uma breve explicação de o que seria escrituração contábil e como eu planejo fazer ela "rodar" em PYTHON

# Basicamente a escrituração contábil é meio que você pegar os fatos contábeis, que é tudo aquilo que altera o patrimônio da empresa, e esses fatos podem ser a entrada e saída de dinheiro no caixa da empresa, vendas de mercadorias, estoques, enfim, tudo que estiver envolvido em alteração do patrimônio.

# A escrituração ela é divida em algumas parte ->
# 1º Livro Diário, onde nele vai ter o Débito(D) e o Crédito(C) que a soma dos débitos e a soma dos créditos, se houver mais de uma daram o mesmo resultado. Para deixar bem claro, no livro Diário, pelo menos no momento deste commit, ele está na fase de aperfeiçoamento. Eu ainda deixarei ele mais automatizado no decorrer que eu for ganahando experiência.
#--------------------------------------------------------------------------------------------------------------------------------------
# 2º Livro Razão(RAZONETE) que é representado da seguinte forma:
#
# ->
#    
# (nome da conta)
#  _____________            
#       |
#       |
#       |
#       |
#
# São representados em formato de "T" onde em cima desse "T" fica o nome da conta(Caixa, banco, estoques, fornecedor, clientes,...) do lado esquerdo, os débitos e o lado esquerdo, é a parte dos créditos. É por meio do Razonete que são feitos os registros individuais por conta.
#--------------------------------------------------------------------------------------------------------------------------------------
# 3º É o Balanço Patrimonial que é um relatório que demonstra de maneira clara e precisa a situação financeira de uma empresa. Para isso, são considerados todos os ativos e passivos de um negócio, ou seja, seus bens, dívidas e lucros.
#
#
# Bom como eu estou falando de contabilidade básica, o Balanço Patrimonial(BP) ele será também feito assim como é visto na faculdade de contabilidade bem ao básico mesmo --->
#
# Com o lado esquerdo tendo seus ativos, as suas contas com o seu saldo e o lado direito o passivo que assim oomo o ativo tem suas contas e o seus saldos e logo abaixo do passivo no mesmo lado temos o patrimônio Líquido com seu capital(R$)
#
# E ao final de cada um dos dois lados vamos ter o total, que na contabilidade, ATIVO = PASSIVO + PATRIMÔNIO LÍQUIDO.
#
# O balanço patrimonial é feito com base em um período de tempo, uma vez ao ano. Portanto, é preciso definir quais serão os meses analisados, o que pode variar conforme as necessidades do negócio. 