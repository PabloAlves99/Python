# Universidade de São Paulo
def remove_repetidos(lista):
     # Converte a lista em um conjunto para remover elementos repetidos
    conjunto_removido = set(lista)
    
    # Converte o conjunto de volta para uma lista e a ordena
    lista_removidos_ord = sorted(list(conjunto_removido))
    
    return lista_removidos_ord
    
lista = [2, 4, 2, 2, 3, 3, 1]

listaSemRepeticao = remove_repetidos(lista)

print(listaSemRepeticao)
