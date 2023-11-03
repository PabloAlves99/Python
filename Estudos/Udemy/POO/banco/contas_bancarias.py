from abc import ABC, abstractmethod


class ContaCorrente():
    pass

class ContaPoupanca():
    pass

class Conta(ABC):
    # Agregação da classe ContaCorrente ou ContaPoupanca
    pass

class Pessoa(ABC):
    def __init__(self, nome = None, idade= None):
        self.nome = nome
        self.idade = idade
        
    @property    
    def criar_pessoa(self):
        return self.nome, self.idade
    
    @criar_pessoa.setter
    def criar_pessoa(self, _dados):
        nome, idade = _dados
        self.nome = nome
        self.idade = idade
        return 'Cadastrado com sucesso'
        

class Cliente(Pessoa, Conta):
    def __init__(self, nome=None, idade=None, conta=None):
        super().__init__(nome, idade)
        self.conta = conta       
