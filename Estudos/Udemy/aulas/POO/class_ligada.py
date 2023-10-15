# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um Fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e Fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor
        
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

class Motor:
    def __init__(self, nome):
        self.nome = nome
        
class Fabricante:
    def __init__(self, nome):
        self.nome = nome

i8 = Carro('i8')
bmw = Fabricante('BMW')
motor = Motor('eletrico')
i8.fabricante = bmw
i8.motor = motor

print(i8.nome, i8.fabricante.nome, i8.motor.nome)

x4 = Carro('x4')
motor = Motor('v8')
x4.fabricante = bmw
x4.motor = motor

print(x4.nome, x4.fabricante.nome, x4.motor.nome)

x3 = Carro('x3')
motor = Motor('v8')
x3.fabricante = bmw
x3.motor = motor

print(x3.nome, x3.fabricante.nome, x3.motor.nome)

twistter = Carro('twistter')
motor = Motor('6M')
honda = Fabricante('Honda')
twistter.fabricante = honda
twistter.motor = motor

print(twistter.nome, twistter.fabricante.nome, twistter.motor.nome)