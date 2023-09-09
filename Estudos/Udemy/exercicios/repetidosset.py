# lista_de_listas = [
#     [1, 2, 2, 3, 4, 4, 5, 5, 6, 7],
#     [2, 3, 3, 4, 5, 5, 6, 6, 7, 8],
#     [3, 4, 4, 5, 6, 6, 7, 7, 8, 9],
#     [4, 5, 5, 6, 7, 7, 8, 8, 9, 10],
#     [5, 6, 6, 7, 8, 8, 9, 9, 10, 1],
#     [6, 7, 7, 8, 9, 9, 10, 10, 1, 2],
#     [7, 8, 8, 9, 10, 10, 1, 1, 2, 3],
#     [8, 9, 9, 10, 1, 1, 2, 2, 3, 4],
#     [9, 10, 10, 1, 2, 2, 3, 3, 4, 5],
#     [10, 1, 1, 2, 3, 3, 4, 4, 5, 6],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
# ]


# for ind, lista in enumerate(lista_de_listas):
#     stop = 0
    
#     for i, item in enumerate(lista):
#         lista.pop(i)
#         x = lista
        
#         if item in x:
#             repetido = item
#             stop += 1
            
#             if stop == 3:
#                 print(f'Lista {ind + 1}: {repetido}')
#     if stop < 3:
#         print(f'Listas {ind + 1}: Não tem mais de dois numeros repetidos')
        
def primeiroduplicado(listas):
    
    for i, lista in enumerate(listas):
        valor = -1
        verificados = set()
        
        for item in lista:
            
            if item in verificados:
                valor = item
                break
            else:
               verificados.add(item)
                
        print(f'Lista {i + 1}: {valor}')

def criarLista():
    from random import randint
    lista_de_listas = []        
            
    for _ in range(10):
        lista = []
        
        for _ in range(10):
            num = randint(1, 20)
            lista.append(num)
        print(lista)
        lista_de_listas.append(lista)
    print('')
    return lista_de_listas

lista_de_listas = criarLista()
primeiroduplicado(lista_de_listas)