# Meta caracteres: ^ $
# ()     \1
# () ()  \1 \2
# (())()   \1 \2 \3
import re
from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
'''

cpf = 'a 147.852.963-12 a'
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# (?: [0-9]{3}\.){2}: Esta parte corresponde a dois grupos de três dígitos
# seguidos por um ponto.
# O(?: ...) é uma sintaxe especial em expressões regulares que cria um grupo de
# não captura, ou seja, os parênteses servem apenas para agrupar a expressão,
# mas não capturam o resultado. Isso significa que o conteúdo do grupo não será
# retornado separadamente pelo findall().

# [0-9]{3}: Corresponde a três dígitos.

# \- Corresponde a um traço.

# [0-9]{2}: Corresponde a dois dígitos.

tags = re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', texto)

# <([dpiv]{1, 3}) > : Corresponde a uma tag de abertura HTML que começa com < ,
# seguida por um grupo de captura contendo uma ou mais letras d, p, i, ou v,
# repetindo de 1 a 3 vezes, e seguida por > .

# (.+?): Corresponde a qualquer caractere(exceto nova linha) repetido uma ou
# mais vezes, mas o ? torna a correspondência "preguiçosa", ou seja,
# corresponde ao mínimo possível de caracteres.

# <\/\1 >: Corresponde a uma tag de fechamento HTML que começa com < /,
# seguida pelo mesmo texto capturado pelo primeiro grupo de captura
# (usando \1), e seguida por > .


tagss = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>', texto)
# nome do grupo de captura é definido como tag, indicado pelo ?P<tag> .

# O ?P < tag > é uma parte especial de uma expressão regular chamada
# "grupo nomeado". Ele é usado para nomear um grupo de captura na expressão
# regular.
# Por exemplo, você pode acessar o texto capturado usando match.group('tag')
# em vez de match.group(1)


pprint(tags)
pprint(tagss)

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS \3 COISAS \4', texto))

# for tag in tags:
#     um, dois, tres = tag
#     print(tres)
