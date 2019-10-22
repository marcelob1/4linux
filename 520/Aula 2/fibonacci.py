#!/usr/bin/python3

''' Calculo de Fibonacci

Esse modulo foi criado com os alunos do curso Python Fundamentals para realizar
sequência de Fibonacci'''
def calcula(valor=80):
    ''' Calcula uma sequência de fibonacci até 80 por padrão '''
    a = 1
    d = 1
    va = 0
    lista = []
    while d < valor:
        lista.append(d)
        va = d
        d += a
        a = va
        lista.sort(reverse=True)
    return lista

if __name__ = '__main__':
    a = print(calcula(()
    a.sort(reverse=True)
    calcula(50000)
    calcula(13)