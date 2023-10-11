# Universidade de São Paulo
num =input("Digite um número com varios dígitos, vamos somar cada número dele, entre eles: ")
x = len(num)
soma = 0

if float(num) <= 0:
    print("Por favor, digite um número maior que 0")
else:
    while x > 0:
        soma = soma + (float(num) % 10)
        num = float(num) // 10
        x = x - 1

if float(soma) > 0:
    print(int(soma))

    