#!/usr/bin/python3

def corazul(texto):
    def modificatexto():
        a = texto()
        print(f'\033[94m{a}\033[0m')
        return modificatexto
    return modificatexto

def coramarelo(texto):
    def modificatexto():
        a = texto()
        print(f'\033[93m{a}\033[0m')
        return modificatexto
    return modificatexto

@corazul
def mostratexto():
    return 'Turma python fundamentals'

mostratexto()

@coramarelo
def mostratexto():
    return 'Turma python fundamentals'

mostratexto()