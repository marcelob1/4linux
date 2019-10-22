#!/usr/bin/python3

# contente = 'Sim'

# if contente == 'Nao':
#     print('palmas')
# print('Fim da execução')

# nome = input('Digite seu nome: ')

# print('Olá', nome, 'Tudo bem?')
# if nome == 'Daniel':
#     print('Você é professor da 4linux')
# else:
#     print(f'{nome}, você é um aluno')

# if nome == 'Daniel' or nome == 'Renato':
#     print(f'{nome} é funcionário da 4Linux')
# else:
#     print('Você não é funcionário da 4Linux,\n mas deixe seu curriculo conosco')

# # Faça uma lógica para venda de bebidas
# # A pessoa não pode comprar bebidas se ela for menos de 18 anos

# nome = input('Digite seu nome: ')
# bebida = input('O que deseja comprar: ')
# idade = int(input('Qual a sua idade: '))

# if idade < 18 and (bebida =='rum' or bebida =='vinho' or bebida =='cerveja'):
#     print(f'{nome}, você não pode comprar {bebida}')

nome = input('Digite seu nome: ')

while True:
    try:
        idade = int(input('Digite sua idade: '))
        if idade < 16:
            print(f'{nome}, você não pode comprar bebida nem ter título de eleitor')
            break
        elif idade >= 16 and idade < 18:
            print(f'{nome}, você não pode comprar bebida, mas pode ter título de eleitor')
            break
        else:
            print(f'{nome}, você pode comprar bebida e pode ter título de eleitor')
            break
    except Exception:
        print('Insira im número, não letra')
        continue