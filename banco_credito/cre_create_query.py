'''
Arquivo para as minhas querys referentes a criação de tabelas dos créditos
'''

def crete_table_cre():
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS credito (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(30),
            valor NUMERIC
        );
        '''
    return create_table_query