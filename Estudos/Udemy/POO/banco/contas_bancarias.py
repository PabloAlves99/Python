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
from random import randint

class Conta(ABC):
    def __init__(self, conta, agencia, numero_conta):
        self.conta = conta
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = 0
    
    @abstractmethod
    def tipo_conta(self):
        pass
        
    def visualizar_dados(self):
        return {
            'Conta': self.tipo_conta(),
            "Agência": self.agencia,
            "Número da Conta": self.numero_conta,
            "Saldo": self.saldo
        }
        
    def depositar(self):
        valor = float(input(f'Saldo atual: {self.saldo} \nDeseja depositar qual valor em sua conta? '))
        self.saldo += valor

class ContaCorrente(Conta):
    def __init__(self):
        super().__init__("Corrente", "001", '1' + f"{randint(100,200)}")

    def tipo_conta(self):
        return "Corrente"
    
class ContaPoupanca(Conta):
    def __init__(self):
        super().__init__("Poupança", "002", '2' + f"{randint(200,300)}")

    def tipo_conta(self):
        return "Poupança"

class Pessoa(ABC):
    def __init__(self, nome = None, idade= None):
        self.nome = nome
        self.idade = idade
        
    @property    
    def editar_pessoa(self):
        return self.nome, self.idade
    
    @editar_pessoa.setter
    def editar_pessoa(self, _dados):
        nome, idade = _dados
        self.nome = nome
        self.idade = idade       

class Cliente(Pessoa):
    def __init__(self, nome=None, idade=None, conta=None):
        super().__init__(nome, idade)   
        self.conta = conta    
        
    def ver_dados(self):
        _= {
            'Nome': self.nome,
            'Idade': self.idade
        }        
        return {**_, **self.conta.visualizar_dados()}
             
             
             
conta = ContaCorrente()
pablo = Cliente('Pablo', 23, conta)
pablo.conta.depositar()
print(pablo.ver_dados())
