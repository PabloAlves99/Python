# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

import locale
import string
from datetime import datetime
from pathlib import Path
from pytz import timezone

CAMINHO = Path(__file__).parent / 'msg_confirmacao.txt'

data = datetime.now(timezone('America/Sao_paulo')).strftime('%d/%m/%Y\n'
                                                            '%H:%M:%S')

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

compra = {
    'nome': 'Henrique Jr',
    'valor': locale.currency(935.99, grouping=True),
    'data': data,
    'servico': 'Automação',
    'numero': '+55 (31) 99423-4449'
}

with open(CAMINHO, 'r', encoding='UTF-8') as arquivo:
    _ = arquivo.read()
    texto = string.Template(_)
    print(texto.substitute(compra))
