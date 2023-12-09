# Udemy com Luiz Otávio Miranda

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