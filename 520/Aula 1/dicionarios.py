#!/usr/bin/python3

apresentacao = {
    'pirata' : 'argh',
    'paulista' : 'salve',
    'carioca' : 'eae',
    'acre' : 'não existe o Acre'
}

print(apresentacao['carioca'])

apresentacao['minas gerais'] = 'uai trem'
print(apresentacao)

print(apresentacao['minas gerais'])

print(apresentacao.keys())
print(apresentacao.values())

#Criar um dicionário com cep, logradouro, numero, quantidade de buracos
#Adicionar quantidade de postes
#Mostrar o Logradouro
#Mostrar a quantidade de buracos + 10
#Converter os valores de chaves para lista e mudar --na lista-- o primeiro valor

dicruas = {
    'cep' : '22031-072',
    'logradouro' : 'Rua Siqueira Campos',
    'numero' : '216',
    'buracos' : '1948'
}

dicruas['postes'] = '230'

print("CEP: "+dicruas['cep'])
print("Logradouro: "+dicruas['logradouro'])
print("Número de Buracos: "+str(int(dicruas['buracos'])+10))

lista = list(dicruas.keys())
print(lista)