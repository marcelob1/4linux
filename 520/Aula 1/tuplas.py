#!/usr/bin/python3


# Manipulação de tuplas

tupla1 = ('valor1','valor2','valor3')

print(tupla1)
print(type(tupla1))

tupla2 = ('valor1','valor2',3,False)

#Criar uma tupla com valores aleatórios
#Acessar o primeiro índice
#Mostrar o terceiro índice em formato de título
#Mostrar a terceira letra do terceiro índice
#Converter a tupla para uma ista e mudar o primeiro índice para outro valor

tupla3 = ('maçã','banana','laranja','melancia',"pera")
print(tupla3[0])
print(tupla3[2].title())
print(tupla3[2][2])
lista = list(tupla3)
lista[0] = 'acerola'
print(lista)