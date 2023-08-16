import os

print(" Tente completar a palavra oculta")
PALAVRA = 'CRUZEIRO'
completando = ''
vezes = 0
print('*' * len(PALAVRA))

while True:
    palavraCerta = ''
    tentativa = input('\nDigite uma letra: ').upper()
    vezes += 1
    
    if len(tentativa) > 1:
        print('Digite apenas uma letra')
        continue
    
    if tentativa in completando:
        print('Você já digitou essa letra')
        continue
    
    if tentativa in PALAVRA:
        completando += tentativa
        
        for letraSecreta in PALAVRA:
            if letraSecreta in completando:
                palavraCerta += letraSecreta
            else:
                palavraCerta += '*'
        print(palavraCerta)
    
    else:
        print(f'ERROU! Não tem a letra {tentativa} nessa palavra, tente outra')
        continue
    
    if PALAVRA == palavraCerta:
        os.system('cls')
        print(f'\nParabens, você acertou a palavra!! \n{PALAVRA} que tem {len(PALAVRA)} letras, você acertou com {vezes} tentativas.')
        break