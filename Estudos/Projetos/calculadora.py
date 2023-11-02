import os

def clear_screen():
    """Limpa a tela do terminal de acordo com o sistema operacional."""
    sistema_operacional = os.name
    if sistema_operacional == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')
        
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError('Não é possível dividir por zero. Por favor, insira um divisor diferente de zero.')


def module(a, b):
    if b != 0:
        return a % b
    else:
        raise ValueError('Não é possível dividir por zero. Por favor, insira um divisor diferente de zero.')

    
def get_valid_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print('Por favor, digite um número válido para prosseguir com o cálculo.')


def calculate():
    """
    Realiza cálculos matemáticos com base na escolha do usuário.
    
    Retorna o resultado do cálculo.
    Pode levantar ValueError se a operação escolhida for inválida.
    """
    number_1 = get_valid_number('Digite o primeiro número: ')
    number_2 = get_valid_number("Digite o segundo número: ")  
            
    operation ={
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '%': module,
    }
    
    clear_screen()
    print('\033[1mDigite apenas oque estiver entre [] !!\n\tOperações disponiveis\033[0m')
    
    print('[+] Adição \n[-] Subtração \n[*] Multiplicação \n[/] Divisão \n[%] Resto da dívisão')    
    chosen_operation = input('\nEscolha a operação: ')
    
    if chosen_operation in operation:
        clear_screen()
        return operation[chosen_operation](number_1, number_2)
    else:
        clear_screen()
        raise ValueError('Operação inválida. Por favor, escolha uma operação válida listada entre os símbolos [+, -, *, /, %].')

def show_instructions():
    print('Bem-vindo! Este programa realiza operações matemáticas simples.')
    print('Operações disponíveis: ')
    print('[+] Adição \n[-] Subtração \n[*] Multiplicação \n[/] Divisão \n[%] Resto da divisão\n')

def main():
    while True:
        clear_screen()
        show_instructions()
        
        try:
            result = calculate()
            print(f"Resultado do cálculo: {result}")
        except ValueError as ve:
            print(f'Erro: {ve}')
            
        continuar = input("\nDeseja fazer outro cálculo? (s/n): ")
        if continuar.lower() != 's':
            break
        
if __name__ == '__main__':
    main()