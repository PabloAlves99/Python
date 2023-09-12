lista = [1, 2, 3, 'Alo', 0.5 , 'Alo2']

for _ in lista:
    if isinstance(_, int):
        print(_, isinstance(_, int))
    else:
        print(_, isinstance(_, int), 'para inteiro')
        
