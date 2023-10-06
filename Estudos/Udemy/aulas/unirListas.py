"""
Exercício - Unir listas
Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas listas na ordem.
Use todos os valores da menor lista.
EX.:
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']
Resultado:
[('Salvador', 'BA), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
"""
from itertools import zip_longest

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

def zipper(l1, l2):
    end = min(len(l1), len(l2))   
    return [(l1[i], l2[i]) for i in range(end)]

print(zipper(cidades, estados))
print( list( zip(cidades, estados) ) )
print( list( zip_longest(cidades, estados) ) )