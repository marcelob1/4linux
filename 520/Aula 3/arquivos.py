#!/usr/bin/python3

### Manipulação de arquivos

# ponteiro = open('texto.txt','w')

# ponteiro.write('Esse testo foi escrito na linguagem python')

# ponteiro.close

with open('texto.txt','a') as ponteiro:
    ponteiro.write('Essa modificação é com o with open\n')

lista = ['indice1','indice2','indice3','indice4','indice5']
lista2 = ['indicel1','indicel2','indicel3','indicel4','indicel5']

with open('texto.txt','a') as ponteiro:
    for indice, item in enumerate(lista2):
        ponteiro.write(f'Indice {indice} = {item}\n')

with open('texto.txt','r') as ponteiro:
    a = ponteiro.readline(6)
    print(a)

def escrever(nomedoarquivo, *escrita):
    try:        
        with open(nomedoarquivo, 'a') as ponteiro:
            escrita = [str(x) for x in escrita]
            ponteiro.writelines(escrita)
    except Exception as e:
        print('Erro no módulo de escrever',e)

def ler(arquivo):
    with open(arquivo,'r') as ponteiro:
        return ponteiro.read()

a = ler('texto.txt')
print(a)