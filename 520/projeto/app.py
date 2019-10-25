#!/usr/bin/env python3

import banco as banco
import threading

if __name__== "__main__":
    user = input('Nickname: ')
    try:
        f = threading.Thread(target=banco.select)
        f.start
    except Exception as e:
        print('Falha ao criar thread: {}'.format(e))
    # Enquanto o thread rodar em segundo plano
    while f.isAlive:
        mens = input()
        banco.cadastrar(user,mens)