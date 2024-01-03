# Universidade de São Paulo
import math
print("Vamos calcular a raiz quadrada de uma equação de 2º grau")
a = float(input("Digite um valor para *a* "))
b = float(input("Agora digite um valor para *b* "))
c = float(input(" Por último, digite um valor para *c* "))
# Se delta < 0 = não tem raiz real
# Se delta == 0 = tem uma raiz real (tal)
# Se delta > 0 = informar raizes
d = b ** 2 - 4 * a * c

if d < 0:
    print("Delta sendo menor que 0, não possui raiz.")
elif d == 0:
    delta = math.sqrt(d)
    x1 = (-b + delta) / (2 * a)
    print("Delta sendo igual a 0, ele possui apenas uma raíz, que é:", x1)
else:
    delta = math.sqrt(d)
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)

    print(x1)
    print(x2)
