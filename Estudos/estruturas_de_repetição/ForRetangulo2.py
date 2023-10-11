# Universidade de São Paulo
def retangulo(larg, alt):
    
    for a in range(alt):
        print("#", end="")
        for l in range(1):
            if (a == 0) or (a == alt - 1):
                print("#" * (larg - 2), end ="")
            else:
                print(" " * (larg - 2), end="")
            l += 1 
        a += 1     

        print("#")
        
        
larg = int(input("Digite a largura: "))
alt = int(input("Digite a altura: "))

retangulo(larg, alt)