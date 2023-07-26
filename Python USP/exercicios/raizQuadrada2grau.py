print("Vamos calcular a raiz quadrada de uma equação de 2º grau")
a = float(input("Digite um valor para *a* "))
b = float(input("Agora digite um valor para *b* "))
c = float(input(" Por último, digite um valor para *c* "))
#Se delta < 0 = não tem raiz real
#Se delta == 0 = tem uma raiz real (tal)
#Se delta > 0 = informar raizes 
import math
d = b ** 2 - 4 * a * c

if d < 0:
    print("esta equação não possui raízes reais")
elif d == 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    print("a raiz desta equação é", x1)
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    
    if x1 < x2:
        print("as raízes da equação são", x1, "e", x2)
    else:
        print("as raízes da equação são", x2, "e" ,x1)