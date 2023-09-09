def remove_repetidos(lista):
     # Converte a lista em um conjunto para remover elementos repetidos
    conjuntoRemovida = set(lista)
    
    # Converte o conjunto de volta para uma lista e a ordena
    listaRemOrd = sorted(list(conjuntoRemovida))
    
    return listaRemOrd
    
lista = [2, 4, 2, 2, 3, 3, 1]

listaSemRepeticao = remove_repetidos(lista)

print(listaSemRepeticao)
