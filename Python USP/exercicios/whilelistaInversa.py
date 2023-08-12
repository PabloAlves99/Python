def adcLista():
    lista = []
    while True:
        x = int(input("Digite um número: "))
        if x > 0:
            lista.append(x)
        else:
            break
    return lista

def mostrarInverso(lista):
    cont = len(lista)
    for cont in range(cont, 0 , -1):
        print(lista[cont - 1])
    

mostrarInverso(adcLista())

