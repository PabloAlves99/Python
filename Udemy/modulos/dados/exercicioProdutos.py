# Udemy com Luiz Otávio Miranda

from produtos_modulo import produtos

cores = {
    'fechar': '\033[m',
    'vermelho': '\033[31m',
    'amarelo': '\033[33m',
    'ciano': '\033[36m',
    'verde': '\033[32m',
    'cinza': '\033[37m'
}

novos_produtos = [{**i, 'preco': round(i['preco'] * 1.1, 2)} for i in produtos]

produtos_ordenados_por_nome = sorted(
    produtos, key=lambda i: i['nome'], reverse=True)

produtos_ordenados_por_preco = sorted(produtos, key=lambda i: i['preco'])

if __name__ == "__main__":

    print(f'{cores["ciano"]}Essa é a lista dos produtos original:',
          *produtos, sep='\n')

    print(f'{cores["fechar"]}', f'{cores["verde"]}Essa é a nova lista dos '
          'produtos com um acrescimo de 10%:',
          *novos_produtos, sep='\n')

    print(f'{cores["fechar"]}', f'{cores["vermelho"]}Essa é a lista ordenada '
          'pelo nome:',
          *produtos_ordenados_por_nome, sep='\n')

    print(f'{cores["fechar"]}', f'{cores["amarelo"]}Essa é a lista ordenada '
          'pelo preço:',
          *produtos_ordenados_por_preco, sep='\n')

    print(
        f'\n{cores["ciano"]}Essa é a lista dos produtos original novamente:',
        *produtos, cores["fechar"], sep='\n')
