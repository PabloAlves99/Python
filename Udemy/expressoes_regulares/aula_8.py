# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $
# re.S -> Dotall \n

# re.A(ou re.ASCII): Faz com que certas sequências de escape ASCII sejam
# correspondidas de acordo com a tabela ASCII, mesmo em strings que utilizam
# um encoding diferente de ASCII. Isso garante que as classes de caracteres
# como \w, \W, \b, \B, \d, \D, \s, e \S correspondam apenas a caracteres ASCII.

# re.I(ou re.IGNORECASE): Faz com que a correspondência de padrões seja feita
# de forma insensível a maiúsculas e minúsculas. Por exemplo, ao usar essa
# flag, as letras "A" e "a" serão consideradas iguais durante a correspondência

# re.M(ou re.MULTILINE): Modifica o comportamento dos metacaracteres ^ e $
# para fazer correspondência com o início e o fim de cada linha dentro de uma
# string multilinha, em vez de apenas o início e o fim da string como um todo.
# Ou seja, ^ corresponderá ao início de uma linha e $ corresponderá ao fim de
# uma linha, independentemente de onde estejam na string.

# re.S(ou re.DOTALL): Faz com que o ponto(.) corresponda a qualquer caractere,
# incluindo o caractere de nova linha(\n). Por padrão, o ponto corresponde a
# qualquer caractere exceto \n, mas ao usar essa flag, ele também corresponderá
# a \n.

import re

texto = '''
131.768.460-53
055.123.060-50
955.123.060-90
'''

print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto, flags=re.M))

texto2 = '''O João gosta de folia
E adora ser amado'''
texto3 = '''xO João gosta de folia
E adora ser amado'''
print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))
print(re.findall(r'^o.*o$', texto3, flags=re.I | re.S))
