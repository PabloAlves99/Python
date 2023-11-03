from abc import ABC, abstractmethod

class ContaCorrente():
    pass

class ContaPoupanca():
    pass

class Conta(ABC, ContaCorrente, ContaPoupanca):
    pass
