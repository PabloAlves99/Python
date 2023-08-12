a = int(input("Digite um número: "))
b = int(input("Digite mais um número: "))
c = int(input("Digite o último número: "))

if ( a < b) and (b < c):
    print("crescente")
else:
    print("não está em ordem crescente")