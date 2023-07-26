numero = input("Digite um número inteiro: ")

num = int(numero)

primeiro = num % 10
segundo = int((num - primeiro) / 10)
dezena = int(segundo % 10)

print("O dígito das dezenas é", dezena)