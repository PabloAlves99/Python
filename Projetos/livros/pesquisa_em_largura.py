from collections import deque

amigos = {
    'pablo': ['alice', 'bob', 'claire'],
    'bob': ['naju', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jhonny'],
    'naju': [],
    'peggy': [],
    'thom': [],
    'jhonny': []
}


def pesquisar(nome):  # todos precisa conter uma lista no valor
    fila_pesquisa = deque()  # Essa função permite usar o popleft
    fila_pesquisa += nome  # recebeu os amigos de pablo
    verificado = []
    while fila_pesquisa:  # Vai recebendo amigos até achar o jhony

        pessoa = fila_pesquisa.popleft()  # retira o primeiro da lista
        if pessoa not in verificado:  # não verifica o mesmo
            if pessoa == 'jhonny':
                print('Achamos Jhonny')
                return True
            else:
                verificado.append(pessoa)  # pessoas que não são o jhonny
                # amigos dessa pessoa, para verificar se é o jhonny
                fila_pesquisa += amigos[pessoa]
                print(f'{pessoa} não é o Jhonny')
    return False  # Se ninguem for amigo de jhonny


print(pesquisar(amigos['pablo']))
