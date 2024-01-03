def teste(n):
    if n == 0:
        print("1")
    else:  
        return(n)
    
def fatorial(n):
    multi = n
    teste(n)
    while multi > 1:
        multi = multi - 1
        n = n * multi
    return(n)
        
def coeBinomial():
    res = (fatorial(c)) / (fatorial(b) * fatorial(c - b))
    print(res)
      
print("Vamos calcular coeficiente binomial ")
c = float(input("Digite o valor de cima: "))
b = float(input("Agora digite o numero de baixo: "))
coeBinomial()