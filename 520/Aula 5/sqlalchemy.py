# #!/usr/bin/python3

# import sqlite3

# conexao = sqlite3.connect('example.db')

# cursor = conexao.cursor()

# cursor.execute('''
#                 CREATE TABLE person
#                 (id INTEGER PRIMARY KEY ASC,
#                      name VARCHAR(250) NOT NULL)
#                 ''')

# cursor.execute('''
#                 CREATE TABLE adress
#                 (id INTEGER PRIMARY KEY ASC,
#                      street_name VARCHAR(250) NOT NULL,
#                      street_number INT NOT NULL)
#                 ''')

# cursor.execute('''
#     INSERT INTO person VALUES (1, 'Daniel')
# ''')
# cursor.execute('''
#     INSERT INTO adress VALUES (1, 'Vergueiro',3057)
# ''')

# conexao.commit()
# conexao.close()

#MANEIRA ORM
import os
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Person(base):
    __tablename__='person'
    id = Column(Integer, primary_key=True)
    name = COLUMN(String(250), nullable=False)

class Address(Base):
    __tablename__='address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(Integer)