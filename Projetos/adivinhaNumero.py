from random import randint
import os

"""
Manipulação de Exceções: Adicionar tratamento de exceções para lidar com entradas não numéricas.

Limite de Tentativas: Adicionar um limite de tentativas para evitar que o jogo continue indefinidamente.

Validação de Entrada: Garantir que a entrada do usuário esteja dentro do intervalo válido.

Melhorar a Interface do Usuário: Adicionar mensagens mais descritivas e claras para orientar o jogador.

Organização do Código: Separar a lógica do jogo em funções para melhorar a legibilidade e reutilização.
"""
def clear_screen():
    sistema_operacional = os.name
    if sistema_operacional == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')


def random_number_game():
    attempts = []
    number_random = randint(1, 1000)   
    
    attempt = int(input('Tente adivinhar o número: '))
    if attempt == number_random:
        print('\tDE PRIMEIRAAA!!!')
        return
        
    attempts.append(attempt)  
    while attempt != number_random:
        clear_screen()
        if attempt < number_random:
            print('O número é maior')
        else:
            print('O número é menor')   
        
        attempt = int(input('Tente adivinhar novamente: '))
        attempts.append(attempt)
    
    clear_screen()
    print(f'\t\tParabens, você acertou!!\n\nO número aleatório é: {attempt}.\nVocê acertou com {len(attempts)} tentativas.')
    print('\nNúmeros tentados:')
    print(*attempts, sep='\t')
        
        
random_number_game()
