!/usr/bin/python3

class pai():
    a = 'Eu pertenço a classe Pai'
class mae():
    b = 'Eu pertenço a classe Mãe'
class filha(pai,mae):
    a = 'Eu sou de ninguém, fui criada sozinha'
    c = 'Eu pertenço a classe Filha'

filha = filha()
print(filha.a, filha.b, filha.c)

class Foo():
    def function():
        print('Executando')

Foo.function()