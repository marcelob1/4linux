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

# Criar o seguinte dicionário:
dados= {
    'cidade':{
        'saoPaulo':{
            'nome':'são paulo',
            'regiao':'sudeste',
            'municipios':'645',
            'populacao':12.18
        },
        'rioDeJaneiro':{
            'nome':'rioDeJaneiro',
            'regiao':'sudeste',
            'municipios':'92',
            'populacao':6.32
        }
    }
}

# Acessar o estado de São Paulo e mostrar a quantidade de pessoas, em milhões
# Acessar o estado do Rio de Janeiro e mostrar a região
# Modificar o nome do rioDeJaneiro para Rio de Janeiro
# Adicionar minasgerais ao dicionário com as seguintes características:
#
# nome - minas gerais
# região - sudeste
# municipios - 853
# populacao - 20.87

# Mostrar a população de Minas Gerais em milhões

print(dados['cidade']['saoPaulo']['populacao'] * 1000000)