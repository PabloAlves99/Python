# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário

from pathlib import Path
import csv

CAMINHO = Path(__file__).parent / 'aula_csv.csv'

with open(CAMINHO, 'r', encoding='utf8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha['Nome'])
        print(linha['Sobrenome'])
        print(linha['Idade'])
