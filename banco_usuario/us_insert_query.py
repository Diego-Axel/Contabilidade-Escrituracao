'''
Arquivo para as minhas querys referentes a inserção de valores nas tabelas dos usuários, INSERT INTO.
'''

def insert_into_us(): # us -> de USUÁRIO 
    insert_query = '''
        INSERT INTO usuarios (nome, sobrenome, satisfacao, melhoria)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
        '''
    return insert_query