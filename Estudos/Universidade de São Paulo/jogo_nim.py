def computador_escolhe_jogada(n, m):
    jogada = 1
    while jogada <= m:
        if (n - jogada) % (m + 1) == 0:
            return jogada
        jogada += 1
    # Caso não seja possível deixar uma quantidade que mantenha a propriedade acima, o computador retira o máximo possível
    return m


def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada <= 0 or jogada > m or jogada > n:
        jogada = int(input("\nQuantas peças você vai tirar? "))
        if jogada <= 0 or jogada > m or jogada > n:
            print("\nOops! Jogada inválida! Tente de novo.")

    return jogada


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print("\nVoce começa!")
        vezUsuario = True
    else:
        print("\nComputador começa!")
        vezUsuario = False

    while n > 0:
        if vezUsuario:
            jogada = usuario_escolhe_jogada(n, m)
            vezUsuario = False
            if jogada == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou", jogada, "peças.")
        else:
            jogada = computador_escolhe_jogada(n, m)
            vezUsuario = True
            if jogada == 1:
                print("\nO computador tirou uma peça.")
            else:
                print("\nO computador tirou", jogada, "peças.")

        n -= jogada  # type: ignore
        if n > 0:
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam", n, "peças no tabuleiro.")

    if vezUsuario:
        print("Fim de jogo! O computador ganhou!")
        return False
    else:
        print("\nVocê ganhou!")
        return True


def campeonato():
    vitorias_usuario = 0
    vitorias_computador = 0

    for _ in range(3):
        print("\n**** Rodada", _ + 1, "****\n")
        if partida():
            vitorias_usuario += 1
        else:
            vitorias_computador += 1

    print("\n**** Final do campeonato! ****\n")
    print("Placar: Você", vitorias_usuario, "X",
          vitorias_computador, "Computador")


print("Bem-vindo ao jogo do NIM! Escolha:")
print("\n1 - para jogar uma partida isolada")
modo = int(input("2 - para jogar um campeonato "))

while modo != 1 and modo != 2:
    print("Opção inválida. Escolha novamente.")
    modo = int(input())

if modo == 1:
    print("\nVocê escolheu uma partida única!\n")
    partida()
else:
    print("\nVocê escolheu um campeonato!")
    campeonato()
