# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class


"""
super(): A função super() é usada para acessar métodos e atributos da classe pai (superclasse). 
No contexto do construtor da classe Fabricante, super() retorna um objeto especial que representa a classe pai Carro.

super()__init__(fabricante, motor): Isso chama o construtor __init__ da classe pai Carro e passa dois argumentos para ele: fabricante e motor.
"""

class Carro: # classe principal ou superclasse.
    def __init__(self):
        self._fabricante = None
        self._motor = None
        self._carro = None     
        
    def detalhes_carro(self):
        print(f'\nCarro: {self._carro} \nFabricante: {self._fabricante} \nMotor: {self._motor}')
  
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor
        return self._motor
        
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante
        return self._fabricante
        
    @property
    def carro(self):
        return self._carro
    
    @carro.setter
    def carro(self, carro):
        self._carro = carro
        return self._carro
        
        
class Fabricante(Carro):
    
    def criar_carro(self):
        
        print(f'\n\tCRIANDO UM CARRO')
        self.carro = input('Digite o nome do carro: ')
        self.fabricante = input('Digite o nome do fabricante: ')
        self.motor = input('Digite qual é o motor: ')
        
        return {'carro': self._carro, 'fabricante': self._fabricante, 'motor': self._motor}

carros = []
while True:
    _ = input('\nO que deseja fazer?\n\
          [C]riar carro\n\
          [S]air ')               
    
    if _.upper() == 'S':
        break
    elif _.upper() == 'C':
        carros.append(Fabricante().criar_carro())
        
print(*carros, sep='\n')

x3 = Carro()
x3.carro = 'x3'
x3.motor = 'Inline-3'
x3.fabricante = 'BMW'
x3.detalhes_carro()

# x4 = Fabricante()
# x4.criar_carro()

# x7 = Fabricante()
# x7.criar_carro()

# x7.detalhes_carro()
# x4.detalhes_carro()


# print(help(Carro))
