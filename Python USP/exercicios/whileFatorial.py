def fatorial(n):
    multi = n
    while multi > 1:
        multi = multi - 1
        n = n * multi
        
    if n == 0:
        print("1")
    else:
        print(n)
    
n = float(input("Digite o valor de n "))

fatorial(n)
