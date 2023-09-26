import string
from random import choice

colors = {
    'fechar': '\033[m',
    'vermelho': '\033[1;31m',
    'amarelo': '\033[33m',
    'ciano': '\033[36m',
    'verde': '\033[32m',
    'cinza': '\033[1;37m'
}

def gerarSenha(end):   # Gerador de senha aleatória de letras e números
    letterAndNum = string.digits + string.ascii_letters
    passoword = ''
    for i in range(end):
        passoword += choice(letterAndNum)
        
    return passoword        

# Segundo a documentação, não é seguro criar uma senha usando o modulo random
if __name__ == '__main__':
    try:
        digits = int(input(f'{colors["cinza"]}Com quantos dígitos você deseja sua senha? {colors["fechar"]}'))       
        print(f'{colors["ciano"]}A sua senha aleatória é:\n {gerarSenha(digits)}{colors["fechar"]}')
        
    except ValueError:
        print(f'\n{colors["vermelho"]}*** O programa será finalizado, execute novamente usando apenas números inteiros ***{colors["fechar"]}\n')
        
    except:
        print(f'\n{colors["vermelho"]}*** ERRO NÃO RECONHECIDO, execute novamente usando apenas números inteiros ***{colors["fechar"]}\n')
    
    