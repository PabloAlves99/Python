"""
Sets - Conjuntos em Python (tipo set)
Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.html
Representatdos graficamente pelo diagrama de Venn
Sets em python são mutáveis, porém aceitatm apenas
tipos imutáveis como valor interno.
"""
s1 = set() # vazio
s2 = {'Lucas', 1, 2, 3}
print(s1, type(s1))
print(s2, type(s2))

"""
Sets são eficientes para remover valores duplicados de iteráveis.
- não tem indexes;
- não garantem ordem;
são iteráveis (for, in, not in)
"""
l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
print(l2)

for numero in s1:
    print(numero)

"""
Métodos úteis:
add, update, clear, discard
"""

s1 = set()
s1.add('Lucas')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Olá mundo')
print(s1)

"""
Operadores úteis:
união | união (union) - une
intersecção & (intersection) - itens presentes em ambos
diferença - itens presentes apenas no set da esquerda
diferença simétrica ^ - itens que não estão em ambos
"""

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s1 ^ s2
print(s3, s4, s5, s6)

# Exemplo de uso dos sets

letras = set()

while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Parabéns!')
        break

    print(letras)
