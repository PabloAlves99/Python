# Udemy com Luiz Otávio Miranda

from copy import deepcopy
from dados import produtos

cores = {
    'fechar': '\033[m',
    'vermelho': '\033[31m',
    'amarelo': '\033[33m',
    'ciano': '\033[36m',
    'verde': '\033[32m',
    'cinza': '\033[37m'
}

# def aumentando10(novos_produtos):
    
#     for i, preco in enumerate(novos_produtos):
#         novos_produtos[i]['preco'] = round(novos_produtos[i]['preco'] * 1.1, 2)
        
#     return novos_produtos

# def nomeDecrescente(novos_produtos):
#     crescente = sorted(novos_produtos, key= lambda item: item['nome'])
#     decrescente = []
#     while crescente:
#         decrescente.append(crescente.pop(-1))
    
#     return decrescente
   
# def precoCrescente(novos_produtos):
    
#     crescente = sorted(novos_produtos, key= lambda item: item['preco']) 

#     return crescente


novos_produtos = [ {**i, 'preco': round(i['preco'] * 1.1, 2)} for i in produtos ]

produtos_ordenados_por_nome = sorted(produtos, key=lambda i: i['nome'], reverse=True)

produtos_ordenados_por_preco = sorted(produtos, key=lambda i: i['preco'])

if __name__ == "__main__":

    print(f'{cores["ciano"]}Essa é a lista dos produtos original:', *produtos, sep='\n')
    
    print(f'{cores["fechar"]}', f'{cores["verde"]}Essa é a nova lista dos produtos com um acrescimo de 10%:',*novos_produtos, sep='\n')
    
    print(f'{cores["fechar"]}',f'{cores["vermelho"]}Essa é a lista ordenada pelo nome:',*produtos_ordenados_por_nome, sep='\n')
    
    print(f'{cores["fechar"]}',f'{cores["amarelo"]}Essa é a lista ordenada pelo preço:', *produtos_ordenados_por_preco, sep='\n')
    
    print('\n', f'{cores["ciano"]}Essa é a lista dos produtos original novamente:', *produtos, sep='\n')

