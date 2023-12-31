"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

"""
from abc import ABC, abstractmethod
from random import randint
from dataclasses import dataclass


class PabloBank():
    """
    Banco responsável pela verificação de contas.
    """

    def verify_account(self, agency: str, account: float) -> bool:
        """
        Verifica se a agência e número da conta estão dentro dos limites
        permitidos.

        Parameters:
        agency (str): Número da agência.
        account (int): Número da conta.

        Returns:
        bool: True se a conta for válida, False caso contrário.
        """
        __agency = ['001', '002']
        check_agency = agency in __agency
        check_account = account >= 1000 and account <= 3000

        if check_agency and check_account:
            return True
        else:
            return False


class Account(ABC):
    """
    Classe abstrata representando uma conta genérica.
    """

    def __init__(self, agency: str, account_number: int, balance: float = 0):
        """
        Inicializa uma conta com a agência, número e saldo.

        Parameters:
        agency (str): Número da agência.
        account_number (int): Número da conta.
        balance (float): Saldo inicial.
        """
        self.agency = agency
        self.account_number = account_number
        self.balance = balance

    def deposit(self, value: float = 0):
        """
        Realiza um depósito na conta.

        Parameters:
        value (float): Valor a ser depositado.
        """
        self.balance += value
        self._balance('Depositar', value)

    @abstractmethod
    def withdraw(self, value: float = 0):
        """
        Método abstrato para saque.
        """

    @abstractmethod
    def account_type(self):
        """
        Método abstrato para o tipo de conta.
        """

    def account_details(self):
        """
        Obtém os detalhes da conta.

        Returns:
        dict: Detalhes da conta, incluindo o tipo, agência, número e saldo.
        """
        # Poderia usar o repr no lugar de criar a função para mostrar os dados
        return {
            'Conta': self.account_type(),
            'Agency': self.agency,
            'Account number': self.account_number,
            'Balance': self.balance,
        }

    def _balance(self, _type, value):
        print(f'Você acabou de {_type} R${value}.')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'(Agency: {self.agency!r},' \
            f' Account Number: {self.account_number!r},'\
            f' Balance: {self.balance!r})'

        return f'{class_name}{attrs}'


@dataclass
class SavingsAccount(Account):
    """
    Classe representando uma conta poupança.

    Args:
        Account (class): Classe base para contas.

    Returns:
        str: Tipo de conta (poupança).
    """
    agency: str = '001'
    balance: float = 0

    def __init__(self):
        self.number_account = randint(2000, 3000)
        super().__init__(SavingsAccount.agency, self.number_account,
                         SavingsAccount.balance)
        self.check_bank = PabloBank()

    def withdraw(self, value: float = 0):
        __agency = self.agency
        __account = self.account_number

        if self.check_bank.verify_account(__agency, __account):

            if self.balance >= value:
                self.balance -= value
                self._balance('Sacar', value)
            else:
                print('Saldo insuficiente')

        else:
            print('Erro em validar com o Banco')

    def account_type(self):
        return "Poupança"


@dataclass(repr=False)
class CurrentAccount(Account):
    """
    Classe representando uma conta corrente.

    Args:
        Account (class): Classe base para contas.

    Returns:
        str: Tipo de conta (corrente).
    """
    agency: str = '002'
    balance: float = 0

    def __init__(self):
        self.number_account = randint(2000, 3000)
        super().__init__(CurrentAccount.agency, self.number_account,
                         CurrentAccount.balance)
        self.check_bank = PabloBank()
        self.extra_value = 200

    def withdraw(self, value: float = 0):
        __agency = self.agency
        __account = self.account_number

        # Verificar no banco
        if self.check_bank.verify_account(__agency, __account):

            if self.balance >= value:  # Verificar o saldo
                self.balance -= value
                self._balance('Sacar', value)
            elif self.extra_value >= value - self.balance:
                self.extra_value -= value - self.balance
                self._balance('Sacar', value)
                print(f'Você ainda tem R${self.extra_value} para ser '
                      'utilizado como extra.')
                self.balance = 0
            else:
                print('Saldo insuficiente')

        else:
            print('Erro em validar com o Banco')

    def account_type(self):
        return "Corrente"


class Person:
    """ Classe abstrata para criar pessoa
    Incluída a pedido do professor, mas é uma classe desnecessária.
    """
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    # def contact(self):
    # #     Essa função foi criada apenas para ter mais funcionalidades.
    # Entretanto não é tão necessária.
    # Mas poderia ajudar a obter informações para um possível contato com o
    # cliente.
    #     self.email = input('Digite seu email: ')
    #     self.number = input('Digite seu número: ')


class Customer(Person):
    """
    Classe representando um cliente.

    Args:
        Person (class): Classe base para pessoas.

    Attributes:
        name (str): Nome do cliente.
        age (int): Idade do cliente.
        bank_account (Account): Conta bancária associada ao cliente.

    Methods:
        set_account (property): Propriedade para obter a conta bancária
        associada.
        set_account (setter): Método para definir a conta bancária associada.
        fetch_account_info: Método para obter os detalhes do cliente e da
        conta associada.

    Returns:
        None
    """

    def __init__(self, name: str, age: int, bank_account: Account):
        super().__init__(name, age)
        self.bank_account = bank_account

    @property
    def set_account(self):
        """
        Propriedade para obter a conta bancária associada.

        Returns:
            Account: Conta bancária associada ao cliente.
        """
        return self.bank_account

    @set_account.setter
    def set_account(self, account: Account):
        self.bank_account = account

    def fetch_account_info(self):
        """
        Obtém os detalhes do cliente e da conta associada.

        Returns:
            dict: Detalhes do cliente, incluindo nome, idade, e detalhes da
            conta bancária.
        """
        _data = {
            'Name': self.name,
            'Age': self.age,
            # 'Email': self.email,
            # 'Number': self.number
        }
        account_details = self.bank_account.account_details() \
            if self.bank_account else {}
        return {**_data, **account_details}


if __name__ == '__main__':

    pabloC = Customer('Pablo Alves', 23, CurrentAccount())
    for data, x in pabloC. fetch_account_info().items():
        print(f'{data}: {x}')

    pabloC.bank_account.deposit(50)
    pabloC.bank_account.withdraw(250)
    print('')

    pabloP = Customer('Pablo Alves', 23, SavingsAccount())
    for data, x in pabloP. fetch_account_info().items():
        print(f'{data}: {x}')
    pabloP.bank_account.deposit(50)
    pabloP.bank_account.withdraw(250)

    # Desativando o repr da conta corrente, no dataclass, o repr da Account
    # será executado
    print('')
    print(pabloC.bank_account)  # repr desativado
    print(pabloP.bank_account)  # repr da conta poupança
