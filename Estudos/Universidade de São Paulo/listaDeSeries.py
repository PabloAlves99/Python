def adicionarSerie():
    series = []
    max_series = 20

    while True:
        serie = input(
            "\nDigite em ordem de preferencia as séries que você mais gosta (ou 'sair' para encerrar): ")

        if serie.lower() == "sair":  # lower() tornou tudo minusculo para verificar
            break

        if not serie:  # Quando não recebe nada, fica negativo automaticamente
            print("Por favor, digite o nome de uma série válida.")
            continue  # Volta no inicio do while

        # Se serie(em minusculo) em [ S.lower recebe a serie dentro do for em minusculo e o "s" recebe oque tem dentro da lista]
        if serie.lower() in [s.lower() for s in series]:
            # Se o serie antes do "in" for igual o s depois do "in"...
            print(
                "Essa série já foi adicionada. Digite outra série ou 'sair' para encerrar.")
        else:
            series.append(serie)  # Adicionar na lista
            if len(series) >= max_series:
                print(
                    f"Limite máximo de séries ({max_series}) atingido. Encerrando adição de séries.")
                break

        # Armazenamento permanente em arquivo
   # with open("series_preferidas.txt", "w") as arquivo:
       # for serie in series:
          #  arquivo.write(serie + "\n")

    return series


def exibirLista(series):

    if series:
        print("\nAs suas séries preferidas são: ")

        for indice, serie in enumerate(series):
            serie = serie.capitalize()  # Capitalize deixa a primeira letra maiúscula
            print(f"Em {indice + 1}º lugar: {serie}")
    else:
        print("\nNenhuma série foi adicionada")


def main():
    print("=== Bem vindo ao catálogo de séries! === ")

    listaSeries = adicionarSerie()
    exibirLista(listaSeries)

    print("\nObrigado! Fechando a lista")


if __name__ == "__main__":
    main()
