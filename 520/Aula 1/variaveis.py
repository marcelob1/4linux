#!/usr/bin/python3
#interpretador do python

numerica = 1
decimais = 10.3
texto = "Valor em texto"

#concatenação de variável
print("O valor da minha variável numérica é de: " + str(numerica))

#concatenação de variáveis com o f string
print(f"o valor da minha variável é: {numerica}")

print(f"o valor da minha variável numérica é de {numerica}\
 e o valor da minha variável decimal é de {decimais}")

#concatenação em format
print("O meu texto da variável é {}".format(texto))

nome = input("Qual é o seu nome? ")

print(f"O seu nome é: {nome}")

float()
int()
str()

## Input, 1 número
# + 2
#mostrar a saída

numero = input("Entre com um número: ")
num2 = int(numero) + 2
print(f"O número {numero} mais 2 é: {num2}")

# a + b
# a - b
# a / b
# a * b
# a ** b (a elevado a b)
# a ** 0.5 (raiz quadrada)
#a == b (a é igual a b - comparativo)
#a != b ( a é diferente de b - comparativo)
#a > b
#a < b

aluno = input("Digite o nome do aluno: ")
curso = input("Digite o curso: ")
print(f"Olá, seja bem vindo {aluno} ao curso {curso}")