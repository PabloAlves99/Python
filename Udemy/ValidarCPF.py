import re
#CPF = 287.307.536-86
def primeiroDigi(CPF):
    multi = 10
    somaNoveD = []
    # Posso usar também o cpf[:9] para pegar os 9 primeiros digitos
    for digito in CPF:
        somaNoveD.append(digito * multi)
        multi -= 1
        if multi == 1:
            somaNoveD = (sum(somaNoveD)) * 10
            break       
           
    resto = somaNoveD % 11
    
    primeiroDigito = 0 if resto > 9 else resto
    return primeiroDigito

def verificar(CPF):
    
    print(primeiroDigi(CPF))
   
def converteNumeros(cpf):
    
    if cpf.isdigit() == False:
        cpf = re.sub(r'[^\w|s]','', cpf)
    CPF = [int(digito) for digito in cpf]
    
    verificar(CPF)

def main ():
    
    print(f'\t VAMOS VERIFICAR O SEU CPF\n')
    cpf = input('Digite o seu CPF: ')
    
    converteNumeros(cpf)
      
if __name__ == '__main__':
    main()