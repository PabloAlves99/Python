class Multiplicar:
    # def __init__(self, multiplicador):
    #     self._multiplicador = multiplicador

    # def __call__(self, func):
    #     def interna(*args, **kwargs):
    #         resultado = func(*args, **kwargs)
    #         return resultado * self._multiplicador
    #     return interna
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, *kwargs)


# @Multiplicar(2)
@Multiplicar
def soma(x, y):
    return x + y


dois_mais_quatro = soma(2, 40)
print(dois_mais_quatro)
