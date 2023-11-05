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
from abc import ABC, abstractmethod
from random import randint

class Account(ABC):
    # Essa classe recebe o número da agenca, conta e saldo
    # Tem o metodo de depositar nessa classe e o metodo sacar abstrado
    
    def __init__(self, agency, account_number, balance):
        self.agency = agency
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, value):
        self.balance += value
        
    @abstractmethod
    def withdraw(self, value):
        pass
    
    @abstractmethod
    def account_type(self):
        ...
    
    def account_data(self):
        return {
            'Conta': self.account_type(),
            'Agency': self.agency,
            'Account number': self.account_number,
            'Balance': self.balance,
        }


class SavingsAccount(Account):   
    def __init__(self):
        super().__init__('001', randint(1000, 2000), 0)  
    
    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
        else:
            print('Saldo insuficiente')
            
    def account_type(self):
        return "Poupança"
    
class CurrentAccount(Account):
    def __init__(self):
        super().__init__('002', randint(2000, 3000), 0)
         
    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
        else:
            print('Saldo insuficiente')
    
    def account_type(self):
        return "Corrente"
    
class Person(ABC):
    # Essa função cria a pessoa
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def contact(self):
        # Essa função foi criada apenas para ter mais funcionalidades, precisa editar
        self.email = input('Digite seu email: ')
        self.number = input('Digite seu número: ')

       
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
        
    def complete_data(self):
        _data = {
            'Name': self.name,
            'Age': self.age,    
            'Email': self.email,
            'Number': self.number       
        }
        account_data = self.bank_account.account_data() if self.bank_account else {}
        return {**_data, **account_data}
    
pablo = Customer('Pablo Alves', 23, CurrentAccount())
pablo.contact()

for data, value in pablo.complete_data().items():
    print(f'{data}: {value}')
