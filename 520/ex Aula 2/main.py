#!/usr/bin/python3

#Criar uma função que retorne um texto colorido
def vermelho(string):
    return f'\033[31m{string}\033[0m'

print(vermelho('Eu sou uma frase em vermelho'))
#Criar uma função para cálculo de raiz quadrada de dois número somados

def calculaRaiz(x,y):
    try:
        return (x+y)**0.5
    except Exception:
        raise ValueError('Insira somente números')

print(calculaRaiz(5,4))

#Criar uma função para formatar uma string como todos os métodos
#de string em uma lista

def formatar(string):
    a = []
    a.append(string.title())
    a.append(string.lower())
    a.append(string.upper())
    a.append(string.strip())
    a.append(string.isnumeric())
    return a

print(formatar('Batatinha'))