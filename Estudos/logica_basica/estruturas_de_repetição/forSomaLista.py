# Universidade de São Paulo
def soma_elementos(lista):
    soma = 0
    for l in lista:
        soma += l      
    return(soma)


lista = [2, 5, 6, 7, 8, 9, 10]
print(soma_elementos(lista))