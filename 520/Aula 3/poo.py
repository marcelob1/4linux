#!/usr/bin/python3

import random
from bancodedados import BancoMelhor

# POO - Programação Orientada a Objeto

# Criação de uma classe

class Foo():
    pass

# Atributos

class Humano():
    nome = 'Daniel'
    idade = 24
    altura = 1.80
    peso = 'Desconhecido'

#Metodos

class Funcionario():
    def funcao(self): # Self é a referência ao objeto
        pass

#Objeto
#Para criar um objeto precisamos realizar uma instância da classe

objeto = Foo()

#Criando uma classe com métodos

class Fazendeiro():
    def capinar(self): # Self é a referência ao objeto
        print('Capinando...')

#Criando um objeto fazendeiro
gerson = Fazendeiro()
#Utilizando o método de capinagem
gerson.capinar() #Chamando o método

#Criando uma classe com métodos e atributos
class Meteorologista():
    a = 3
    #Método construtor, usado para passar atributos para os métodos
    def __init__(self,nome,idade,tv = True):
        #Definindo os atributos
        self.nome = nome
        self.idade = idade
        self.tv = tv
        self.emissora = 'Band'
    #Definir métodos
    def previsao(self):
        print(f'Boa tarde, meu nome é {self.nome}')
        if self.tv == True:
            print(f'Faço parte da Emissora {self.emissora}')
        print(f'Hoje está nublado')
        print(f'Só pra constar, eu tenho {self.idade}')
    def trocaNome(self,nome):
        self.nome = nome
    @staticmethod
    def oi():
        print('oi')

laura = Meteorologista('Laura',43, False)
laura.previsao()
laura.trocaNome('Rapadura')
laura.previsao()
print(laura.a)
laura.oi()

class Cachorro():
    #Método construtor, usado para passar atributos para os métodos
    def __init__(self,nome,idade,sexo,cor,raca):
        #Definindo os atributos
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cor = cor
        self.raca = raca
    #Definir métodos
    def latir(self):
        print(f'{self.nome}, {self.idade} anos, {self.sexo}, {self.cor}, {self.raca} está latindo...')
    def comer(self):
        print(f'{self.nome}, {self.idade} anos, {self.sexo}, {self.cor}, {self.raca} está comendo...')
    def cacar(self):
        print(f'{self.nome}, {self.idade} anos, {self.sexo}, {self.cor}, {self.raca} está caçando...')
    def trocaNome(self,nome):
        self.nome = nome
    @classmethod
    def funcaoObjeto(self, nome, idade, peso):
        print('Oi, Estou sendo executada')
        print(nome,idade,peso)
toto = Cachorro('Totó',10, 'macho', 'preto', 'Pastor Belga')
toto.latir()
toto.comer()
toto.cacar()
toto.trocaNome('Saturno')
toto.latir()
toto.comer()
toto.cacar()

class Humano():
    def __init__(self,idade,nome,genero):
        self.idade = idade
        self.nome = nome
        self.genero = genero
    def andar(self):
        return 'Andando'
    def comer(self):
        return 'Comendo'
    def dormir(self):
        return 'Dormindo'

class Funcionario(Humano):
    def __init__(self,profissao,nome,idade,genero):
        super(Humano).__init__(nome,idade,genero)
        self.profissao = profissao
    def trabalhar(self):
        return 'Trabalhando'

funcionario = Funcionario('Jogador de futebol','Gabigol',23,'Homo')


humano = Humano(19,'Lucas','Masculino')

print(dir(funcionario))

print(funcionario.dormir())
