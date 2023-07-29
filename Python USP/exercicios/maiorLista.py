def maior_elemento(lista):
    maior = 0
    for l in lista:
        if l > maior:
            maior = l
    return(maior)


lista = [2, 5, 6, 35, 7, 8, 9, 10]
print(maior_elemento(lista))