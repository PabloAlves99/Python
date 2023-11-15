from random import randint
import os


def clear_screen():
    sistema_operacional = os.name
    if sistema_operacional == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')


def get_user_attempt(__attempts):

    # Retorna um int de tentativa válida do usuario

    _attempt = input('Tente adivinhar o número: ')
    if _attempt.isdigit():
        _attempt = int(_attempt)
        __attempts.append(_attempt)
        return _attempt
    else:
        print('Só é permitido números inteiros neste programa...')
        return get_user_attempt(__attempts)


def verify_attempt(_attempt, __number_random):

    # Retorna um booleano true se a tentativa for correta,
    # False se for incorreto a tentativa.

    if _attempt == __number_random:
        return True
    elif _attempt < __number_random:
        print('O número é maior')
    else:
        print('O número é menor')
    return False


def random_number_game():

    #  Retorna uma tupla contendo a lista de tentativas e o número aleatório.

    attempts = []
    number_random = randint(1, 1000)
    escape = False

    while not escape:
        _attempt = get_user_attempt(attempts)
        clear_screen()
        escape = verify_attempt(_attempt, number_random)

    return attempts, number_random


def main():
    """
    Inicializa o jogo de adivinhação e mostra a mensagem de boas-vindas.
    Retorna a função finish para mostrar a mensagem de conclusão do jogo.
    """
    clear_screen()
    print('\tBem vindo ao jogo de adivinha')
    print('Neste jogo só é permitido números inteiros...')

    def finish(_attempt, _attempts):
        clear_screen()
        print(
            f'\t\tParabens, você acertou!!\n\nO número aleatório é: {_attempt}'
            f'.\nVocê acertou com {len(_attempts)} tentativas.')
        print('\nNúmeros tentados:')
        print(*_attempts, sep='\t')
    return finish


if __name__ == "__main__":
    call = main()
    tentativas, numeros_aleatorios = random_number_game()
    call(numeros_aleatorios, tentativas)
