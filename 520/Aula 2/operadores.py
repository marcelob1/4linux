#!/usr/bin/python3

# operadores aritméticos

num1 = 18
num2 = 5
soma = num1 + num2
subt = num1 - num2
mult = num1 * num2
div1 = num1 / num2
div = num1 // num2
mod = num1 % num2

num1 = 1
num1 += 2
num1 -= 2
num1 *= 2
num1 /= 2
num2 %= 2

# operadores relacionais
# retorna true ou false
num1 = 4
num2 = 6

num1 == num2 # igual?
num1 != num2 # diferente?
num1 < num2 # menor?
num1 <= num2 # menor ou igual?
num1 > num2 # maior?
num1 >= num2 # maior ou igual?
num1 > num2 is True # compara valor entre booleanos (valores Lógicos, True ou False)

#operadores Lógicos
verdadeiro = True
falso = False

#Somente se um valor ou outro for verdadeiro a condição será retornada True
verdadeiro or falso # True, porque um dos dois é verdadeiro
falso or falso # False, porque nenhum dos dois é verdadeiro
verdadeiro or verdadeiro # True, porque ambas são verdadeias

#Somente se ambos forem verdadeiros será retornado True
falso and falso # False, porque nenhum dos dois é verdadeiro
falso and verdadeiro # False, porque ambas tem de ser verdadeiras
verdadeiro and falso # False, porque ambas tem de ser verdadeiras
verdadeiro and verdadeiro # True, porque ambas são verdadeias

#Inverte o resultado da expressão
not falso and falso #True, porque nenhuma das duas é verdadeira, retornaria falso e inverteria 
not falso and verdadeiro #True, porque as duas tem que ser verdadeira
not verdadeiro and falso #True, porque as duas tem que ser verdadeira
not verdadeiro and verdadeiro #False, porque ambas são verdadeiras
