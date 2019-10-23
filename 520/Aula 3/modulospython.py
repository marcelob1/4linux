#!/usr/bin/python3
import sys, datetime
import csv
from os import system, listdir

print(listdir('..'))

print(sys.argv)

if len(sys.argv) == 2:
    print(f'O parâmetro passado foi {sys.argv[1]}')
if len(sys.argv) == 3:
    print(f'O parâmetro passado foi {sys.argv[1]}, {sys.argv[2]}')

print(datetime.datetime.now())
print(datetime.timedelta(50))
print(datetime.time(14,0,0))
print(datetime.date(2017,10,13))

acesso = datetime.datetime(2018,1,22,0,0,0)
atual = datetime.datetime.now()

print(acesso, atual)

print(atual - acesso)

with open('avengers.csv','r') as csvfile:
    for x in csv.reader('csvfile'):
        print(x)

with open('teste.csv','w') as csvfile:
    arquivo = csv.writer(csvfile,delimiter=',')
    arquivo.writerow(['Teste'] * 100)
