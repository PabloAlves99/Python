# Universidade de São Paulo
def maximo(a, b, c):
    if (a == b) and (b == c):
        return(a)
    elif (a > b) and (a > c):
        return(a)
    elif (b > a) and (b > c):
        return(b)
    else:
        return(c)

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o ultimo valor: "))
maximo(a, b, c)