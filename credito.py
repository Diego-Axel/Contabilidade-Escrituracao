import psycopg2 
import banco_credito.cre_create_query as create
import banco_credito.cre_insert_query as insert
import banco_credito.cre_sel_query as select
import time

def banco_credito():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="palmeiras123",
            host="localhost",
            port="5432",
            database="escrituracao"
        )
        cursor = connection.cursor()  
        # Criar tabela
        create.crete_table_cre()
        cursor.execute(create.crete_table_cre())
        connection.commit()
        # Inserir dados na tabela
        nome = input("Digite o nome da sua conta de Crédtio: ")
        valor = input("Digite o valor dessa conta: ")       
        insert.insert_into_cre()
        cursor.execute(insert.insert_into_cre(), (nome, valor))
        id_inserido = cursor.fetchone()[0]
        connection.commit()
        print()
        print(f"Dado inserido com ID: {id_inserido}")
        time.sleep(5)
    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ou operar no PostgreSQL", error)
    finally:
        # Fechar conexão
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com PostgreSQL fechada")