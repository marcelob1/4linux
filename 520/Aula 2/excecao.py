#!/usr/bin/python3

#tratamento de exceções
try:
    int(input('Digite um número: '))
except ValueError as e:
    print('Isso não é um número',e)

try:
    #Criar uma entrada pra login
    login = input('Digite seu login: ').lower()
    #se o login for de um policial
    if login == 'policial':
        #vou alertar que não pode acessar nesse campo
        raise NameError('Você não tem acesso a esse login')
    #senão
    else:
        #ele pode entrar
        print(f'seja bem vindo, {login}')
#se o algoritmo encontrar erros
except NameError as e:
    #mostre ao usuário o erro encontrado
    print(e)