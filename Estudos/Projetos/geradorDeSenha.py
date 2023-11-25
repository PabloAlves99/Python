import string
from random import choice
import os


def limpar_tela():
    """
    Limpa o terminal/console, detectando o sistema operacional atual.

    Utiliza o módulo os para identificar o sistema operacional e executa
    o comando apropriado para limpar a tela. Suporta Windows ('nt') e sistemas
    Unix/Linux/Mac.

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


def letter_password():
    """
    Solicita ao usuário o tipo de letras desejado para a senha e retorna um
    caracter correspondente.

    O usuário pode escolher entre três opções:
    1. Maiúsculas e minúsculas.
    2. Somente maiúsculas.
    3. Somente minúsculas.

    Parâmetros:
    Nenhum.

    Retorna:
    str: Caracter correspondente à escolha do usuário.

    Exemplo:
    >>>letter_password()
    Escolha o tipo de letras desejado:
    1- Maiúscula e minúscula
    2- Só maiúscula
    3- Só minúscula
    Digite o número da opção desejada: 2
    'P'

    Raises:
    ValueError: Se o usuário inserir uma opção inválida.
    """
    letter_type = int(input('\nAs lestras podem ser:\n'
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
        raise ValueError('Opção escolhida não é permitida')

    return _unit

def creat_password()
...
def password_settings():
    try:
        digits = int(input('Com quantos dígitos você deseja sua senha? '))

    except ValueError as ve:
        raise ValueError('Informe apenas números inteiros') from ve

    while True:
        password_types = int(
            input('Como você deseja sua senha?\n'
                  '1- Apenas letras\n'
                  '2- Apenas Números\n'
                  '3- Letras e números\n'
                  '4- Letras, números e caracteres especiais '))

        if (password_types < 1) or (password_types > 4):
            print('\n*** ESCOLHA UM NÚMERO DAS OPÇÕES ACIMA. ***\n')
        elif password_types == 1:
            unit = letter_password()
        elif password_types == 2:
            unit = string.digits
        elif password_types == 3:
            unit = string.ascii_letters + string.digits
        elif password_types == 4:
            unit = string.ascii_letters + string.digits + string.punctuation

    creat_password()
password_settings()


#     password = ''
#     for i in range(end):
#         password += choice(unit)
#     limpar_tela()
#     return password


# # Segundo a documentação, não é seguro criar uma senha usando o modulo random
# if __name__ == '__main__':
#     limpar_tela()

#     # except:
#     #     print(
#     #         f'\n{colors["vermelho"]}*** ERRO NÃO RECONHECIDO, execute \
#     #         novamente usando apenas números inteiros ***\
#     #         {colors["fechar"]}\n')
