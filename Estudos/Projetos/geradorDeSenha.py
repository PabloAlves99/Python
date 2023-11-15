import string
from random import choice


def limpar_tela():
    import os
    sistema_operacional = os.name
    if sistema_operacional == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')


colors = {
    'fechar': '\033[m',
    'vermelho': '\033[1;31m',
}


def createPassword(end):
    passwordTypes = int(input('Como você deseja sua senha?\n'
                              '1- Apenas letras\n'
                              '2- Apenas Números\n'
                              '3- Letras e números\n'
                              '4- Letras, números e caracteres especiais '))

    if (passwordTypes < 1) or (passwordTypes > 4):
        print(
            f'\n{colors["vermelho"]}*** APENAS É ACEITO OS NÚMEROS DAS OPÇÕES ACIMA. O programa será finalizado ***{colors["fechar"]}\n')
        return

    if passwordTypes == 1:
        # Pode ser gerado um if passowordTypes != 2, inves do que está rodando, e dar essa opçáo para cada opção que contem letras.
        letterType = int(input('\nAs lestras podem ser:\n'
                               '1- Maiúscula e minúscula\n'
                               '2- Só maiúscula\n'
                               '3- Só minuscula '))
        if letterType == 1:
            unit = string.ascii_letters
        elif letterType == 2:
            unit = string.ascii_uppercase
        elif letterType == 3:
            unit = string.ascii_lowercase
        else:
            print(
                f'\n{colors["vermelho"]}*** APENAS É ACEITO OS NÚMEROS DAS OPÇÕES ACIMA. O programa será finalizado ***{colors["fechar"]}\n')
            return

    elif passwordTypes == 2:
        unit = string.digits

    elif passwordTypes == 3:
        unit = string.ascii_letters + string.digits

    elif passwordTypes == 4:
        unit = string.ascii_letters + string.digits + string.punctuation

    password = ''
    for i in range(end):
        password += choice(unit)
    limpar_tela()
    return password


# Segundo a documentação, não é seguro criar uma senha usando o modulo random
if __name__ == '__main__':
    limpar_tela()
    try:
        digits = int(input(f'Com quantos dígitos você deseja sua senha? '))
        PASSWORD = createPassword(digits)
        if PASSWORD != None:
            print(f'A sua senha aleatória é:\n\n {PASSWORD}\n')

    except ValueError:
        print(f'\n{colors["vermelho"]}*** O programa será finalizado, execute novamente usando apenas números inteiros ***{colors["fechar"]}\n')

    except:
        print(
            f'\n{colors["vermelho"]}*** ERRO NÃO RECONHECIDO, execute novamente usando apenas números inteiros ***{colors["fechar"]}\n')
