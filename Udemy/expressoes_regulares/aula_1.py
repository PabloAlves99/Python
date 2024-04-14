# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto
import re

# Funções
# findall search sub
# compile

string = 'Este é um teste de expressões teste regulares.'
print(re.search(r'teste', string))
print()
print(re.findall(r'teste', string))
print()
print(re.sub(r'teste', 'ABCD', string))
print()
print()
regexp = re.compile(r'teste')
print(regexp.search(string))
print()
print(regexp.findall(string))
print()
print(regexp.sub('DEF', string))
