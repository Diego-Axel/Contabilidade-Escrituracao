'''Banco de Dados (PRIVATE)'''

'''imports'''
import psycopg2 
import os

# Conectar ao banco de dados --> PostgreSQL

def usuarios():
    try:
        connection = psycopg2.connect(
            user= # "Seu usuário do Banco",
            password= # "A senha do seu banco",
            host= # O servidor (se for na sua máquina então será um -> localhost),
            port= # "porta que está no banco",
            database= # "o nome do database(banco)"
        )
        cursor = connection.cursor()

        # Criar Tabela
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(30),
            sobrenome VARCHAR(40),
            satisfacao TEXT,
            melhoria TEXT
        );
        '''
        cursor.execute(create_table_query)
        connection.commit()

        # Inserir dados na tabela
        os.system("clear || cls")
        print("------ REGISTRO PARA FEEDBACK ------")
        print()
        nome = input("| Digite o seu nome: ")
        print()
        sobrenome = input("| Digite o seu sobrenome: ")
        print()
        satisfacao = input("| O que achou do Programa? ")
        print()
        melhoria = input("| Tem alguma sugestão para melhoria? ")
        print()
        print("Dados salvos com sucesso!")
        input("telce <ENTER> para continuar...")

        insert_query = '''
        INSERT INTO usuarios (nome, sobrenome, satisfacao, melhoria)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
        '''
        cursor.execute(insert_query, (nome, sobrenome, satisfacao, melhoria))
        id_inserido = cursor.fetchone()[0]
        connection.commit()
        print(f"Dado inserido com ID: {id_inserido}")

        # Consultar os dados inseridos
        # select_query = "SELECT * FROM usuarios;"
        # cursor.execute(select_query)
        # records = cursor.fetchall()

        # print("Dados na tabela 'usuarios':")
        # for row in records:
        #     print(f"ID: {row[0]}, Nome: {row[1]}, Valor: {row[2]}")
            
    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ou operar no PostgreSQL", error)

    finally:
        # Fechar conexão
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com PostgreSQL fechada")


def banco_debito():
    try:
        connection = psycopg2.connect(
            user= # "Seu usuário do Banco",
            password= # "A senha do seu banco",
            host= # O servidor (se for na sua máquina então será um -> localhost),
            port= # "porta que está no banco",
            database= # "o nome do database(banco)"
        )
        cursor = connection.cursor()
        
        # Criar tabela
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS debito (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(30),
            valor NUMERIC
        );
        '''
        cursor.execute(create_table_query)
        connection.commit()

        # Inserir dados na tabela
        nome = input("Digite o nome da sua conta de Débito: ")
        valor = input("Digite o valor dessa conta: ")
        
        insert_query = '''
        INSERT INTO debito (nome, valor)
        VALUES (%s, %s)
        RETURNING id;
        '''
        cursor.execute(insert_query, (nome, valor))
        id_inserido = cursor.fetchone()[0]
        connection.commit()
        print(f"Dado inserido com ID: {id_inserido}")

        # Consultar os dados inseridos
        # select_query = "SELECT * FROM debito;"
        # cursor.execute(select_query)
        # records = cursor.fetchall()
        
        # print("Dados na tabela 'debito':")
        # for row in records:
        #     print(f"ID: {row[0]}, Nome: {row[1]}, Valor: {row[2]}")
            

    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ou operar no PostgreSQL", error)

    finally:
        # Fechar conexão
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com PostgreSQL fechada")


def banco_credito():
    try:
        connection = psycopg2.connect(
            user= # "Seu usuário do Banco",
            password= # "A senha do seu banco",
            host= # O servidor (se for na sua máquina então será um -> localhost),
            port= # "porta que está no banco",
            database= # "o nome do database(banco)"
        )
        cursor = connection.cursor()
        
        # Criar tabela
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS credito (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(30),
            valor NUMERIC
        );
        '''
        cursor.execute(create_table_query)
        connection.commit()

        # Inserir dados na tabela
        nome = input("Digite o nome da sua conta de Crédtio: ")
        valor = input("Digite o valor dessa conta: ")
        
        insert_query = '''
        INSERT INTO credito (nome, valor)
        VALUES (%s, %s)
        RETURNING id;
        '''
        cursor.execute(insert_query, (nome, valor))
        id_inserido = cursor.fetchone()[0]
        connection.commit()
        print(f"Dado inserido com ID: {id_inserido}")

        # Consultar os dados inseridos
        # select_query = "SELECT * FROM credito;"
        # cursor.execute(select_query)
        # records = cursor.fetchall()
        
        # print("Dados na tabela 'credito':")
        # for row in records:
        #     print(f"ID: {row[0]}, Nome: {row[1]}, Valor: {row[2]}")
            

    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ou operar no PostgreSQL", error)

    finally:
        # Fechar conexão
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com PostgreSQL fechada")


def banco_historico():
    print()