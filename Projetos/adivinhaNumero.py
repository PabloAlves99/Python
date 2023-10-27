from random import randint
from time import sleep
import os

# Criar opção de mais de uma pessoa tentar acertar

def limpar_tela():
    sistema_operacional = os.name
    if sistema_operacional == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')


def random_game():
    attempts = []
    number_random = randint(1, 1000)   
    attempt = int(input('Tente adivinhar o número: '))
    
    if attempt == number_random:
        print('DE PRIMEIRAAA!!!')
    attempts.append(attempt)  
    while attempt != number_random:
        limpar_tela()
        if attempt < number_random:
            print('O número é maior')
        else:
            print('O número é menor')   
        
        attempt = int(input('Tente adivinhar novamente: '))
        attempts.append(attempt)
    
    limpar_tela()
    print(f'\t\tParabens, você acertou!!\n\nO número aleatório é: {attempt}.\nVocê acertou com {len(attempts)} tentativas.')
    print('\nNúmeros tentados:')
    print(*attempts, sep='\t')
        
        
random_game()
# print(number_random)