frase = 'O python é uma linguem de programação ' \
        'multiparadigma. ' \
        'Python foi criado por Guido Van Rossum.'

i = 0
maior = 0
letra = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    
    apareceu = frase.count(letra_atual)
    
    if maior < apareceu:
        maior = apareceu
        letra = letra_atual
    i += 1

print(f'A letra que apareceu mais vezes foi: -> {letra} <-. Que apareceu {maior}x')