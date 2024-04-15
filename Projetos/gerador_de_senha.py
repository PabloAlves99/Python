import string
from secrets import choice
import os


def limpar_tela():
    """
    Exemplo:
    >>>limpar_tela()

    Nota:
    - Para utilizar essa função em um script, certifique-se de ter o módulo
      'os' importado.
    """
    sistema_operacional = os.name
    if sistema_operacional == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')


def letter_password() -> str:
    """
    Solicita ao usuário o tipo de letra desejado para a senha e retorna um
    conjunto de caracteres correspondente.

    O usuário pode escolher entre três opções:
    1. Maiúsculas e minúsculas.
    2. Somente maiúsculas.
    3. Somente minúsculas.

    Parâmetros:
    Nenhum.

    Retorna:
    str: Conjunto de caracteres correspondente à escolha do usuário.

    Exemplo:
    >>>letter_password()
    Escolha o tipo de letras desejado:
    1- Maiúscula e minúscula
    2- Só maiúscula
    3- Só minúscula
    Digite o número da opção desejada: 1
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    Raises:
    ValueError: Se o usuário inserir uma opção inválida.
    """
    limpar_tela()
    letter_type = int(input('\tAs lestras podem ser:\n'
                            '1- Maiúscula e minúscula\n'
                            '2- Só maiúscula\n'
                            '3- Só minuscula '))
    if letter_type == 1:
        _unit = string.ascii_letters
    elif letter_type == 2:
        _unit = string.ascii_uppercase
    elif letter_type == 3:
        _unit = string.ascii_lowercase
    else:
        raise ValueError('*** Opção escolhida não é permitida ***')

    return _unit


def creat_password(digits: int, unit: str) -> str:
    """
    Gera e retorna uma senha aleatória com o número especificado de dígitos.

    Parâmetros:
    - digits (int): Número de dígitos desejados na senha.
    - unit (str): Conjunto de caracteres a partir do qual a senha será gerada.

    Retorna:
    str: Senha aleatória gerada.
    """
    return ''.join(choice(unit) for _ in range(digits))


def password_settings() -> str | None:
    """
    Solicita ao usuário as configurações desejadas para a geração de senha.

    Solicita o número desejado de dígitos e o tipo de caracteres para a senha,
    permitindo escolher entre opções que incluem apenas letras, apenas números,
    letras e números, ou letras, números e caracteres especiais.

    Parâmetros:
    Nenhum.

    Retorna:
    str: Senha gerada de acordo com as configurações escolhidas.

    Exemplo:
    >>>password_settings()
    Com quantos dígitos você deseja sua senha? 8
    Como você deseja sua senha?
    1- Apenas letras
    2- Apenas Números
    3- Letras e números
    4- Letras, números e caracteres especiais
    Digite o número da opção desejada: 3
    'aB3zR7qE'

    Raises:
    ValueError: Se o usuário inserir um número inválido ou se a quantidade de
    dígitos for menor ou igual a 0.
    """
    try:
        digits = int(input('Com quantos dígitos você deseja sua senha? '))
        if digits <= 0:
            print('\n*** Não existe senha com 0 ou menos digitos ***\n')
            return None

    except ValueError as ve:
        raise ValueError('***Digite apenas números inteiros***') from ve

    while True:
        password_types = int(
            input('Como você deseja sua senha?\n'
                  '1- Apenas letras\n'
                  '2- Apenas Números\n'
                  '3- Letras e números\n'
                  '4- Letras, números e caracteres especiais '))

        if (password_types < 1) or (password_types > 4):
            raise ValueError('\n*** Escolha apenas um numero das opções ***\n')
        elif password_types == 1:
            unit = letter_password()
            limpar_tela()
            return creat_password(digits, unit)
        elif password_types == 2:
            unit = string.digits
            limpar_tela()
            return creat_password(digits, unit)
        elif password_types == 3:
            unit = letter_password() + string.digits
            limpar_tela()
            return creat_password(digits, unit)
        elif password_types == 4:
            unit = letter_password() + string.digits + string.punctuation
            limpar_tela()
            return creat_password(digits, unit)


if __name__ == '__main__':
    print(f'Senha aleatória: {password_settings()}')
