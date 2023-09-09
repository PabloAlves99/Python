import random

def verificarDigi(CPF, v):
    multi = v
    somaNoveD = []
    
    for digito in CPF:
        somaNoveD.append(int(digito) * multi)
        multi -= 1
        if multi == 1:
            somaNoveD = (sum(somaNoveD)) * 10
            break       
           
    resto = somaNoveD % 11
    
    nDigito = 0 if resto > 9 else resto
    return str(nDigito)

def gerarCPF():
    
    CPF = ''
    for i in range(9):
        CPF += str(random.randint(0, 9))
        
    v = 10
    CPF += verificarDigi(CPF, v)
    v += 1
    CPF += verificarDigi(CPF, v)
    
    print (CPF)
    

x = int(input('Quantos CPF você deseja que seja criado? '))
for i in range(x):
    gerarCPF()
