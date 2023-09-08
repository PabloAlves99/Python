import os
from time import sleep
cores = {
    'fechar': '\033[m',
    'vermelho': '\033[1;31m',
    'amarelo': '\033[1;33m',
    'ciano': '\033[1;36m',
    'verde': '\033[1;32m',
    'cinza': '\033[1;37m'
}

# Função para limpar a tela com base no sistema operacional
def limpar_tela():
    sistema_operacional = os.name
    if sistema_operacional == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')
        
def quiz(questions):
    acerto = 0
    
    for question in questions:       
        limpar_tela()
        for chave, valor in question.items():
            print(f'{cores["amarelo"]}{chave}: {valor} ')
            print('\nOpções: ')
            
            for i, opç in enumerate(question['Opções']):
                print(f'{i}) {opç}')
                
            x = input('Resposta: {}{}'.format(cores['fechar'], cores['cinza']))
            
            if x.isdigit(): 
                xint = int(x)
                if (xint >= 0) and (xint < 4):
                    if x == question['resposta']:     
                        print('\n{}{}VOCÊ ACERTOU!!{}'.format(cores['fechar'], cores['verde'], cores['fechar']))
                        acerto += 1
                        sleep(2)
                        break   
                    else:             
                        print('\n{}VOCÊ ERROU!!{}'.format(cores['vermelho'], cores['fechar']))
                        sleep(2)
                        break
                else:
                    print(f'\n{cores["vermelho"]}VOCê ERROU!! Digite apenas os números das opções{cores["fechar"]}')
                sleep(3)
                break
                    
            else:
                print(f'\n{cores["vermelho"]}Digite apenas os números das opções, você errou essa pergunta!{cores["fechar"]}')
                sleep(3)
                break
    return acerto

def createQuestions():
    questions = [
        {
            'Pergunta': 'Existe quantas reliquias da morte na saga de Harry Potter?',
            'Opções': [3, 5, 2, 7],
            'resposta': '0',
        },
        {
            'Pergunta': 'Existe quantas maldições imperdoaveis na saga de Harry Potter?',
            'Opções': [2, 5, 3, 7],
            'resposta': '2',
        },
        {
            'Pergunta': 'O que o apanhador precisa capturar para vencer o jogo?',
            'Opções': ['pomo de ouro', 'bola de ouro', 'elmo de ouro', 'arco de ouro'],
            'resposta': '0',
        }
    ]
    return questions

def main():
  
    questions = createQuestions()
    right = quiz(questions)
    limpar_tela()
    if right > 0:
        mensagem = f'Você acertou {right} de {len(questions)} perguntas'
        print(f'{cores["verde"]}-='*20 , f'\n{mensagem.center(40)}\n' , '=-'*20 , f'{cores["fechar"]}')
    else:
        mensagem = 'Infelizmente você não conhece nada de Harry Potter!'
        print(f'{cores["ciano"]}-='*30 , f'\n{mensagem.center(60)}\n' , '=-'*30 , f'{cores["fechar"]}')
        
if __name__ == '__main__':
    main()