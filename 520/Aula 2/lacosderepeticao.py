#!/usr/bin/python3

x = 1

#loop enquanto (while)
while x < 10:
    print('Socorro')
    x += 1

menu = '1'
while menu == '1':
    menu = input('Deseja sair? 1 - não, outra coisa para sim: ')

#loop for
for x in range(10):
    print(x)
for x in range(0,51,2):
    print('Você comprou', x)
a = []
for x in range(7):
    a.append(x * 3)
    print(a[x])
print(a)