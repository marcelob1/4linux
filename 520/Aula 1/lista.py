#!/usr/bin/python3

lista = ['arroz','feijão','açucar']

#print(lista[0])
#print(lista[1])
#print(lista[2])

vetor = [
    ['celular','copo','prato'],
    ['joias','relogio','brinco'],
    ['chocolate','bala','biscoito']
    ]

print(vetor[0][1])
print(vetor[1])
print(vetor[2][0][2])
print(vetor[1][2])
print(vetor[0][1:])
print(vetor[0][0:2])

#alteração de lista

letras = ['a','b','d','e','c','f']
letras.sort()
print(letras)

letras[1]='x'

print(letras)
