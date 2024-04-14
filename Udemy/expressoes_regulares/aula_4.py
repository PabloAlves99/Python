# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1

import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
'''

print(re.findall(r'<[pdiv]{1,3}>.+<\/[divp]{1,3}>', texto))
print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto))


# <[pdiv]{1, 3} > : Corresponde a uma tag HTML que começa com < , seguida por
# uma das letras p, d, i, ou v, repetindo de 1 a 3 vezes, e seguida por > .

# .+: Corresponde a qualquer caractere(exceto nova linha) repetido uma ou mais
# vezes.

# <\/ [divp]{1,3}>: Corresponde a uma tag de fechamento HTML que começa com </,
# seguida por uma das letras d, i, v, ou p, repetindo de 1 a 3 vezes, e seguida
# por >. O caractere de barra invertida \ é usado para escapar o caractere de
# barra /.

# r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>': A expressão regular aqui é quase a mesma
# que a anterior, mas adiciona um ? após o .+, tornando o quantificador +
# "preguiçoso" ao invés de "ganancioso". Isso significa que ele corresponderá
# ao mínimo possível de caracteres, em vez de ao máximo, tornando a
# correspondência não-gananciosa.
