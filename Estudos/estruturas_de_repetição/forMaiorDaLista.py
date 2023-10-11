# Universidade de São Paulo
def maior_elemento(lista):
    maior = lista[0]
    for l in lista:
        if l > maior:
            maior = l
    return(maior)


lista = [2, 5, 6, 35, 40, 7, 8, 9, 10]
print(maior_elemento(lista))