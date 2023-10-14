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

class Carro(): # classe principal ou superclasse.
    def __init__(self, carro, fabricante, motor):
        self.fabricante = fabricante
        self.motor = motor
        self.carro = carro
        
        
class Fabricante(Carro): # herda as propriedades e métodos da classe Carro.
    def __init__(self, carro, fabricante, motor):
        super().__init__(carro, fabricante, motor)
    
x3 = Fabricante('x3', 'BMW', 'inline-8')

print(f'Carro: {x3.carro} \nFabricante: {x3.fabricante} \nMotor: {x3.motor}')
# print(help(Carro))

"""
super(): A função super() é usada para acessar métodos e atributos da classe pai (superclasse). No contexto do construtor da classe Fabricante, super() retorna um objeto especial que representa a classe pai Carro.

__init__(fabricante, motor): Isso chama o construtor __init__ da classe pai Carro e passa dois argumentos para ele: fabricante e motor.
"""