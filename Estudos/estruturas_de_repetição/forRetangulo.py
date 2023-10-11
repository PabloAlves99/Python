# Universidade de São Paulo
def retangulo(larg, alt):
    
    for a in range(alt):
        for l in range(larg):
            print("#", end="")
            l += 1  
            if l == larg:
                print("") 
        a += 1

larg = int(input("Digite a largura: "))
alt = int(input("Digite a altura: "))

retangulo(larg, alt)