import os

print(" Tente completar a palavra oculta")
PALAVRA = 'CRUZEIRO'
palavraFormada = ['*'] * len(PALAVRA) 
vezes = 0
print('*' * len(PALAVRA))

while True:
    palavraCerta = ''   
    tentativa = input('\nDigite uma letra: ').upper()
    vezes += 1  
     
    if len(tentativa) > 1:
        print('Digite apenas uma letra!!!')
        continue
    
    if tentativa in palavraFormada:
        print('Você já digitou essa letra')
        continue
    
    if tentativa in PALAVRA:
        
        for indice, i in enumerate(PALAVRA):
                           
            if i == tentativa:
                palavraFormada[indice]= tentativa
        
        for l in palavraFormada:
            palavraCerta += l     
             
        print(f'{palavraCerta}')
        
    else:
        print(f'ERROU! Não tem a letra {tentativa} nessa palavra, tente outra')
        continue
    
    if '*' not in palavraFormada:
        os.system('cls')
        print(f'\nParabens, você acertou a palavra!! \n{PALAVRA} que tem {len(PALAVRA)} letras, você acertou com {vezes} tentativas.')
        break