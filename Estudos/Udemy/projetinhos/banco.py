"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

"""
from abc import ABC, abstractmethod
from random import randint

class PabloBank():
    # def register(self, name):
    #     # Criando um doc com todos os nomes seria melhor
    #     # EX:
    #     # with open('name_customers.json', 'w+') as arquivo:
    #     #     ...
    #     # Não será implementado porque esta é uma verificação simples
    #     pass
    
    def to_check(self,agency, account):
        __agency = ['001', '002']
        check_agency = agency in __agency
        check_account = account >= 1000 and account <= 3000
        
        if check_agency and check_account:
            return True
        else:
            return False 
         
        

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
        self.check_bank = PabloBank()
    
    def withdraw(self, value):
        __agency = self.agency
        __account = self.account_number
        
        if self.check_bank.to_check(__agency, __account):
            if self.balance >= value:
                self.balance -= value
            else:
                print('Saldo insuficiente')
        else:
            print('Erro em validar com o Banco')
            
    def account_type(self):
        return "Poupança"
    
class CurrentAccount(Account):   
    def __init__(self):
        super().__init__('002', randint(2000, 3000), 0)
        self.check_bank = PabloBank()
        self.extra_value = 200
         
    def withdraw(self, value):
        # Função de saque, aqui é verificado no banco se as informações pertinentes são verdadeiras e a conta corrente conta com 200 a mais de limite pro saque
        __agency = self.agency
        __account = self.account_number
        
        if self.check_bank.to_check(__agency, __account): # Verificar no banco
            
            if self.balance >= value: # Verificar o saldo
                self.balance -= value
            elif self.extra_value >= value - self.balance:
                self.extra_value -= value - self.balance  
                print(f'Você ainda tem R${self.extra_value} para ser utilizado como extra.')
                self.balance = 0
            else:
                print('Saldo insuficiente')
        else:
            print('Erro em validar com o Banco')
    
    def account_type(self):
        return "Corrente"
    
    
class Person(ABC):
    # Essa função cria a pessoa. Totalmente desnecessária, entretanto feita a pedido do professor.
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # def contact(self):
    # #     Essa função foi criada apenas para ter mais funcionalidades, precisa editar
    #     self.email = input('Digite seu email: ')
    #     self.number = input('Digite seu número: ')

       
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
            # 'Email': self.email,
            # 'Number': self.number       
        }
        account_data = self.bank_account.account_data() if self.bank_account else {}
        return {**_data, **account_data}
    
if __name__ == '__main__':
    pablo = Customer('Pablo Alves', 23, CurrentAccount())
    pablo.bank_account.deposit(150)
    pablo.bank_account.withdraw(250)

    for data, value in pablo.complete_data().items():
        print(f'{data}: {value}')
