def primo(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def n_primos(num):
    qnt = 0
    for x in range(2, num):
        if primo(x):
            qnt += 1
    if qnt == 2:
        qnt = 1
    return(qnt)

num = int(input("Digite um número igual ou maior que 2: "))

if num >= 2:
    n_primos(num)
else: 
    print("Execute novamente com um número válido")