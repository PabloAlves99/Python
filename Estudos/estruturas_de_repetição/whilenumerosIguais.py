# Universidade de São Paulo
ni = float(input("Digite um número: "))
resto = ni + 1

while ni % 10 != resto:
    resto = ni % 10
    ni = ni // 10

if ni == 0:
    print("Não existe números repetidos em sequência!")
else:
    ni = int(ni % 10)
    print("O número", ni, "repete em sequência")