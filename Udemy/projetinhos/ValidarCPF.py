import re
import os
# CPF = 287.307.536-86


def verificarDigi(CPF, v):
    multi = v
    somaNoveD = []

    for digito in CPF:
        somaNoveD.append(digito * multi)
        multi -= 1
        if multi == 1:
            somaNoveD = (sum(somaNoveD)) * 10
            break

    resto = somaNoveD % 11

    nDigito = 0 if resto > 9 else resto
    return nDigito


def verificar(CPF, cpf):
    v = 10
    CPF[9] = verificarDigi(CPF, v)
    v += 1
    CPF[10] = verificarDigi(CPF, v)
    CPF = ''.join(map(str, CPF))

    if CPF == cpf:
        os.system('cls')
        print('O CPF digitado é válido')
    else:
        os.system('cls')
        print('O CPF digitado não é válido')


def verificarNumeros(cpf):

    if cpf.isdigit() == False:
        cpf = re.sub(r'[^0-9]', '', cpf)
    CPF = []
    CPF.extend(int(digito) for digito in cpf)

    verificar(CPF, cpf)


def main():

    print(f'\t VAMOS VERIFICAR O SEU CPF\n')
    cpf = input('Digite o seu CPF: ')

    verificarNumeros(cpf)


if __name__ == '__main__':
    main()
