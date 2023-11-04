"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)   
    
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractclassmethod
from random import randint

class Account():
    # Essa classe recebe o número da agenca, conta e saldo
    # Tem o metodo de depositar nessa classe e o metodo sacar abstrado
    
    def __init__(self, agency, account_number, balance):
        self.agency = agency
        self.acount_number = account_number
        self.balance = balance
    
    def deposit(self, value):
        self.balance += value
        
    @abstractclassmethod
    def withdraw():...
    
    
class SavingsAccount(Account):   
    def __init__(self):
        super().__init__('001', randint(1000, 2000), 0)
        
class CurrentAccount(Account):
    def __init__(self):
        super().__init__('002', randint(2000, 3000), 0)
        

class Person(ABC):
    # Essa função cria e edita os dados da pessoa
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def edit_data(self):
        return self.name, self.age
    
    @edit_data.setter
    def edit_data(self, _data):
        name, age = _data
        self.name = name
        self.age = age
       
class Customer(Person):
    # Essa classe herda a criação de pessoas da classe Person 
    # Recebe a conta do banco já criada (Agregação da classe conta)
    
    def __init__(self, name= None, age= None, bank_account= None):
        super().__init__(name, age)
        self.bank_account = bank_account
        
    @property
    def insert_account(self):
        return self.bank_account
    
    @insert_account.setter
    def insert_account(self, account):
        self.bank_account = account
        
        
pablo = CurrentAccount()
pablo.deposit(200)

print(pablo.__dict__)