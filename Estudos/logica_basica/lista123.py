# Universidade de São Paulo
lista1 = {"a", "b", "c",
          "d", "e"}

lista2 = {"a", "b", "c",
          "d", "e"}

lista3 = {"a", "d"}

print(lista1 is lista3)
print(lista3 is lista1)
print(lista1 is lista2)
print(lista1 == lista3)
print(lista3 == lista1)
print(lista1 == lista2)