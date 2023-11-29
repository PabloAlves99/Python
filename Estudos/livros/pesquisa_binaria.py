def pesquisaBinaria(lista, item):

    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:

        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None


def mostrar(lista, posicoes):

    while True:

        num = int(input(
            "\nDigite um número da lista para receber a posição dele: (digite 0 para sair) "))
        posi = pesquisaBinaria(lista, num)

        if num == 0:
            break

        elif posi == None:
            print(
                f"*** DIGITE UM NUMERO QUE EXISTE NA LISTA ***\n Vou enviar novamente a lista \n\n {lista}")

        else:
            print(f"O numero {num} está na posição {posi}")
            posicoes.append(posi)

    return posicoes


def main():
    lista = [42, 15, 87, 95, 60, 31, 11, 28, 5, 93, 97, 85, 91, 37,
             98, 33, 85, 6, 4, 14, 10, 64, 31, 63, 18, 88, 94, 40, 83, 80]

    lista.sort()
    posicoes = []

    print(f"\n{lista}\n \n- Lembrando que a lista começa com o primeiro item na posição 0, o segundo na posição 1 e assim por diante...")
    mostrar(lista, posicoes)

    print(
        f"\nTodas as posições recebidas: {posicoes}\nFinalizando o programa!\n")


if __name__ == "__main__":
    main()
