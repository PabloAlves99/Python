# Udemy com Luiz Otávio Miranda
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y

# def criarFuncao(funcao, *args):
#     if len(args) == 1:
#         print('Precisamos de 2 valores,\nAutomaticamente consideramos o
#               segundo como "0"')
#         y = 0
#         return funcao(*args, y)
#     else:
#         return funcao(*args)


def criarFuncao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


somaComCinco = criarFuncao(soma, 5)
multiplicaPorDez = criarFuncao(multiplica, 10)

print(somaComCinco(5))
print(multiplicaPorDez(21))
