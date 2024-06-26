'''
Arquivo para as minhas querys referentes a criação de tabelas dos débitos
'''

def create_table_deb():
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS debito (
            id SERIAL PRIMARY KEY,
            nome_conta VARCHAR(30),
            valor_conta NUMERIC
        );
        '''
    return create_table_query