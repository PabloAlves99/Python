# pylint: disable= missing-docstring
# type: ignore

grafo: dict = {}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}

# Dicionario para os custos
infinito = float("inf")
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

# Dicionario para os pais
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []


def ache_custo_mais_baixo(_custos):
    custo_mais_baixo = float('inf')
    nodo_custo_mais_baixo = None

    # Pegar um por um dos vertices
    for _nodo in _custos:
        _custo = _custos[_nodo]

        # Se for o vertice de menor custo até o momento
        # e ainda nao tiver sido processado...
        if _custo < custo_mais_baixo and _nodo not in processados:

            # Atribui como novo vertice de menor custo
            custo_mais_baixo = _custo
            nodo_custo_mais_baixo = _nodo
    return nodo_custo_mais_baixo


# Custo mais baixo que não foi processado
NODO = ache_custo_mais_baixo(custos)

# Enquanto houver NODO para processar faça...
while NODO is not None:

    custo = custos[NODO]
    vizinhos = grafo[NODO]

    # Percorre todos os vizinhos da vertice
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]

        # Verificar se o novo custo é menor
        if custos[n] > novo_custo:

            # se for menor, atualiza o valor
            custos[n] = novo_custo

            # esse vertice se torna o novo pai
            pais[n] = NODO

    # Marca como processado
    processados.append(NODO)
    # Encontra o novo vertice e reinicia
    NODO = ache_custo_mais_baixo(custos)

# Resultados finais
print("Custos finais:", custos)
print("Pais finais:", pais)
