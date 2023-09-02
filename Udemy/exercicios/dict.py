import os

# Função para limpar a tela com base no sistema operacional
def limpar_tela():
    sistema_operacional = os.name
    if sistema_operacional == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

def adicionar():
    login = input('Digite o seu usuario: ')
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    telefone = input('Digite o seu telefone: ')
    
    usuario = {
        login: {
            'nome': nome,
            'email': email,
            'telefone': telefone
        }
    }
    return usuario

usuarios = {}    

while True:
    usuario = adicionar()
    usuarios.update(usuario)
    x = input('Deseja continuar adicionando? [SIM / NAO] ').upper()
    limpar_tela()
    if x == 'NAO':
        break

limpar_tela()

# Para acessar os dados de um usuário específico:
buscar = input('Deseja buscar algum usuario? ').upper()
while True:
    if buscar == 'SIM':
        buscarLogin = input('Digite o login do usuário que deseja buscar: ')
        if buscarLogin in usuarios:
            limpar_tela()
            print(f'\033[1;31m{usuarios[buscarLogin]}\033[m')
        else:
            limpar_tela()
            print('Usuário não encontrado.')
    else:
        break
    buscar = input('Deseja buscar novamente algum usuario? ').upper()
