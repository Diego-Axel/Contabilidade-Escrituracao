'''
Arquivo para as minhas querys referentes a criação de tabelas
'''
'''FUNÇÕES'''

def create_table_us(): # us -> de USUÁRIO 
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(30),
            sobrenome VARCHAR(40),
            satisfacao TEXT,
            melhoria TEXT
        );
        '''
    return create_table_query


def create_table_deb():
    pass