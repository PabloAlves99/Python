# Udemy com Luiz Otávio Miranda

import json

# pessoa = {
#     'nome': 'Pablo',
#     'sobrenome': 'Alves',
#     'idade': 23,
#     'altura': 1.75,
#     'time': 'Cruzeiro',
# }

# with open('pessoas.json', 'w', encoding='utf8') as arquivo:
#     json.dump(pessoa, arquivo, indent=2)

with open('pessoas.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)

print(pessoa)
