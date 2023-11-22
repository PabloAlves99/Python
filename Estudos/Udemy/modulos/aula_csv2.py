# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
# csv.writer e csv.DictWriter para escrever em CSV

# 'r': Abrir um arquivo para leitura. Se o arquivo existir, o ponteiro é
# posicionado no início do arquivo, permitindo que você leia seu conteúdo.

# 'w': Abrir um arquivo para escrita. Se o arquivo não existir, um novo a
# rquivo vazio é criado. Se o arquivo existir, o conteúdo anterior é apagado.
# Você pode escrever no arquivo após abri-lo.

# 'r+': Abrir um arquivo para leitura e escrita. O ponteiro é posicionado no
# início do arquivo. Permite ler e escrever no arquivo.

# 'a': Abrir um arquivo para anexar. Se o arquivo existir, o ponteiro é
# posicionado no final do arquivo. Se o arquivo não existir, um novo arquivo é
# criado. Você pode adicionar conteúdo ao final do arquivo.

from pathlib import Path
import csv

# CAMINHO = Path(__file__).parent / 'aula_csv.csv'

# with open(CAMINHO, 'r', encoding='utf8') as arquivo:
#     leitor = csv.DictReader(arquivo)

#     for linha in leitor:
#         print(linha['Nome'])
#         print(linha['Sobrenome'])
#         print(linha['Idade'])

CAMINHO = Path(__file__).parent / 'criar_csv.csv'

lista_clientes = [
    {'nome': 'Pablo', 'idade': 23},
    {'nome': 'Henrique', 'idade': 22},
    {'nome': 'Alves', 'idade': 21}
]

with open(CAMINHO, 'w+', encoding='utf8', newline='') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    # csv.writer(arquivo).writerow(nome_colunas)

    escritor = csv.DictWriter(arquivo, fieldnames=nome_colunas)
    escritor.writeheader()

    for dados in lista_clientes:
        escritor.writerow(dados)
