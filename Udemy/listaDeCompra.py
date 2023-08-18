import os
print(f'\tEssa é a sua lista de compras\n')
lista = []

while True:
    
    acao = input('O que deseja fazer na sua lista de compras? \n\n [I]nserir itens \n [D]eletar item \n [V]isualizar lista:\n [F]inalizar: ').upper()
    
    if acao == 'F':
        break
    
    elif acao == 'V':
        os.system('cls')
        print('Sua lista até o momento:\n')
        for indice, item in enumerate(lista):
            print(indice, item)
        print('\n')
        continue
        
    elif acao == 'D':
        os.system('cls')
        d = int(input('Digite qual o indice do item que deseja apagar: '))
        if d < len(lista):
            del(lista[d])
            os.system('cls')
            continue
        else:
            os.system('cls')
            print('Indice incorreto, vamos tentar novamente')
            continue
    
    elif acao == 'I':
        os.system('cls')
        i = input('Digite o nome do item que deseja inserir na lista: ')
        lista.append(i)
        os.system('cls')
        continue
    
    else:
        os.system('cls')
        print('Você digitou algo de errado, vamos tentar novamente')

os.system('cls')
print('Segue abaixo sua lista de compras finalizada:\n')
for item in lista:
    print(item)