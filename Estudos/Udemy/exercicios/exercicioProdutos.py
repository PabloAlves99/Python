produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#copia profunda
from copy import deepcopy
novos_produtos = deepcopy(produtos)

def aumentando10(novos_produtos):
    
    for i, preco in enumerate(novos_produtos):
        novos_produtos[i]['preco'] = round(novos_produtos[i]['preco'] * 1.1, 2)
        
    return novos_produtos

def nomeDecrescente(novos_produtos):
    
    crescente = sorted(novos_produtos, key= lambda item: item['nome'])
    decrescente = []
    while crescente:
        decrescente.append(crescente.pop(-1))
        
    return decrescente
   
def precoCrescente(novos_produtos):
    
    crescente = sorted(novos_produtos, key= lambda item: item['preco']) 
    
    return crescente


produtos_ordenados_por_nome = deepcopy(nomeDecrescente(novos_produtos))
produtos_ordenados_por_preco = deepcopy(precoCrescente(novos_produtos))

print(*aumentando10(novos_produtos), sep='\n')
print('\n', *produtos_ordenados_por_nome, sep='\n')
print('\n', *produtos_ordenados_por_preco, sep='\n')

