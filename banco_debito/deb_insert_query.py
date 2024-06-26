'''
Arquivo para as minhas querys referentes a inserção de valores nas tabelas dos débitos, INSERT INTO.
'''

def insert_into_deb():
    insert_query = '''
        INSERT INTO debito (nome, valor)
        VALUES (%s, %s)
        RETURNING id;
        '''
    return insert_query