#!/usr/bin/python3

class BancoMelhor():
    def __init__(self):
        self.usuario = 'root'
        self.senha = '123456'
        self.banco = 'mysql'
    def select(self):
        if self.usuario == 'root':
            return 'Dados do banco'
        else:
            return None
    def insert(self,dados)
        if self.usuario == 'root':
            return f'Dado {dados} inserido'
        else:
            return None
    def delete(self):
        if self.usuario == 'root':
            return 'Dado removido'
    def update(self,id):
        if self.usuario == 'root'
            return 'Atualizado com sucesso'