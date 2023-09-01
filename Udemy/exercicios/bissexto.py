from datetime import date

ano = int(input('Digite o ano que deseja saber se é Bissexto (Coloque 0 para analisar o ano atual) '))
if ano == 0:
    ano = date.today().year
condicao = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

print('\033[1;31m-=\033[m' *20)
print(f'O ano {ano} é Bissexto' if condicao else f'O ano {ano} não é Bissexto')
print('\033[1;31m=-\033[m' *20)