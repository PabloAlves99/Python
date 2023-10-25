def adc_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self.__dict__})'
    cls.__repr__ = meu_repr
    return cls

@adc_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adc_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)