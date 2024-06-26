'''imports'''
import psycopg2 
import banco_usuario.us_create_query as create
import banco_usuario.us_insert_query as insert
import os
import time

# Conectar ao banco de dados --> PostgreSQL

def usuarios():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="palmeiras123",
            host="localhost",
            port="5432",
            database="escrituracao"
        )
        cursor = connection.cursor()
        # Criar Tabela
        create.create_table_us()
        cursor.execute(create.create_table_us())
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
        # INSERT INTO
        insert.insert_into_us()
        cursor.execute(insert.insert_into_us(), (nome, sobrenome, satisfacao, melhoria))
        id_inserido = cursor.fetchone()[0]
        connection.commit()
        print()
        print(f"Usuário inserido com ID: {id_inserido}")
        time.sleep(5)           
    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ou operar no PostgreSQL", error)
    finally:
        # Fechar conexão
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com PostgreSQL fechada")