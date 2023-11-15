# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime, timedelta
import locale

FORMATO = '%d/%m/%Y'
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
VALOR_EMPRESTIMO = 1_000_000

data_emprestimo = datetime(2020, 12, 20)
data_final = data_emprestimo + timedelta(days=365*5)

for datas in range(60):
    parcela = locale.currency(VALOR_EMPRESTIMO / 60, grouping=True)
    datas_emprestimo = data_emprestimo + timedelta(days=31*datas)

    if datas_emprestimo.day < 20:
        diferenca = 20 - datas_emprestimo.day
        datas_emprestimo += timedelta(days=diferenca)
    else:
        diferenca = datas_emprestimo.day - 20
        datas_emprestimo -= timedelta(days=diferenca)

    print(f'{datas+1}x: {datas_emprestimo.strftime(FORMATO)} Valor a pagar: '
          f'{parcela}')
