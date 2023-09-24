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
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

unidas = []

fim = len(cidades) if len(cidades) > len(estados) else len(estados)

for c, e in zip(cidades, estados):
    if fim == 0:
        break
    unidas.append([c, e])

print (unidas)