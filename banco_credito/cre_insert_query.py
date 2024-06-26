'''
Arquivo para as minhas querys referentes a inserção de valores nas tabelas dos créditos, INSERT INTO.
'''

def insert_into_cre():
    insert_query = '''
        INSERT INTO credito (nome, valor)
        VALUES (%s, %s)
        RETURNING id;
        '''
    return insert_query