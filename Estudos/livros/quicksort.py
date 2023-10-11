import random

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menor = [i for i in array[1:] if i <= pivo]
        bigger = [i for i in array[1:] if i > pivo]
    return quicksort(menor) + [pivo] + quicksort(bigger)

lista = random.sample(range(1,1001), 100)

print(quicksort(lista))

# Usando o sorted(lista), o tempo de execução nesse caso é igual