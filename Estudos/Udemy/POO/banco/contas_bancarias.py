# Criar classe Cliente que herda da classe Pessoa (Herança)
#     Pessoa tem nome e idade (com getters)
#     Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)  


# Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
#     ContaCorrente deve ter um limite extra
#     Contas têm agência, número da conta e saldo
#     Contas devem ter método para depósito
#     Conta (super classe) deve ter o método sacar abstrato (Abstração e
#     polimorfismo - as subclasses que implementam o método sacar)
# Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
# Banco será responsável autenticar o cliente e as contas da seguinte maneira:
#     Banco tem contas e clientes (Agregação)
#     * Checar se a agência é daquele banco
#     * Checar se o cliente é daquele banco
#     * Checar se a conta é daquele banco
# Só será possível sacar se passar na autenticação do banco (descrita acima)
# Banco autentica por um método.

from abc import ABC, abstractmethod

class Conta(ABC):
    # Agregação da classe ContaCorrente ou ContaPoupanca
    pass

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
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
