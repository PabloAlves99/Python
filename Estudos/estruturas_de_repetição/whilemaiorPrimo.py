#  Universidade de São Paulo
def maior_primo(n):
    for c in range(n, 1, -1):
        if primo(c):
            return c


def primo(m):
    i = 1
    cont = 0
    while i <= m:
        if m % i == 0:
            cont += 1
        i += 1
        if cont > 2:
            return False
    return True


num = int(input('Digite um número inteiro maior que "1": '))

print(f'O maior número primo menor ou igual a "{num}" é: {maior_primo(num)}')