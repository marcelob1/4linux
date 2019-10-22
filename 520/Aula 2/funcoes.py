#!/usr/bin/python3
import fibonacci
#Como criar uma função

def media(n1,n2,n3):
    media = (n1+n2+n3)/3
    return(media)

print(media(5,9,7))
fibonacci.calcula(10**1300)

var = 'Daniel'

def mudaNome():
    print(var)
    var = 'Douglas'
    print(var)

mudaNome()
input('Tecle enter para continuar')
print(var)

def media(*numeros):
    x = [numeros for numeros in numeros]
    return sum(x)

media(1,2,3,4,5,6)