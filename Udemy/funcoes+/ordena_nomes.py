# Udemy com Luiz Otávio Miranda

lista = [
    {"Nome": "João", "Sobrenome": "Silva"},
    {"Nome": "Maria", "Sobrenome": "Santos"},
    {"Nome": "Pedro", "Sobrenome": "Oliveira"},
    {"Nome": "Ana", "Sobrenome": "Pereira"},
    {"Nome": "Lucas", "Sobrenome": "Costa"},
    {"Nome": "Isabela", "Sobrenome": "Ferreira"},
    {"Nome": "Rafael", "Sobrenome": "Ribeiro"},
    {"Nome": "Mariana", "Sobrenome": "Carvalho"},
    {"Nome": "Gustavo", "Sobrenome": "Martins"},
    {"Nome": "Julia", "Sobrenome": "Almeida"}
]


def exibirLista(lista):
    for item in lista:
        print(item)


l1 = sorted(lista, key=lambda item: item['Nome'])
l2 = sorted(lista, key=lambda item: item['Sobrenome'])

print('\033[1;31mListas ordenadas pelo NOME \033[m')
exibirLista(l1)

print('\n\033[1;31mListas ordenadas pelo SOBRENOME \033[m')
exibirLista(l2)
