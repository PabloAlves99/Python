NOME = input("Digite o seu nome: ")

contador = 0
nome = ''
while contador < len(NOME):
    nome += f'*{NOME[contador]}'
    contador += 1

print(nome)
