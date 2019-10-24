#!/usr/bin/python3
#Usar o Modulo de conexão psycopg2
import psycopg2

#Fazer a conexão com o postgresql

try:
    #Abrir um ponto de conexão
    postgre = psycopg2.connect(
        'host=127.0.0.1\
        dbname=biblioteca\
        user=admin\
        password=4linux'
    )
    #Abrir um cursor
    res = postgre.cursor()
    #Cursor executa comandos
    res.execute("insert into clientes(nome,sobrenome) values\
         ('Lucas','Teles')")
    res.execute("select * from clientes")
    #trás as respostas dos meus comandos a tona
    print(res.fetchall())
    #update
    res.execute("UPDATE clientes set nome='Batatinha'\
         where nome='Lucas'")
    #select
    res.execute("select * from clientes")
    #Mostrar os resultados
    print(res.fetchall())
    #encerro a conexão com o banco
    res.close()
except Exception as e:
    print(e)
    res.close()

import psycopg2

class BancoPsql():
    def __init__(self):
        try:
            conexao = psycopg2.connect(        
            'host=127.0.0.1\
            dbname=biblioteca\
            user=admin\
            password=4linux'
            )
            self.cursor = conexao.cursor()
        except Exception as e:
            print(f'Falha na conexão com o banco: {e}')
    def select(self,tabela,item='*'):
        self.cursor.execute(f'SELECT {item} FROM {tabela}')
        print(self.cursor.fetchall())
banco = BancoPsql()
banco.select('clientes')
banco.update('clientes','nome','Josivaldo','6')