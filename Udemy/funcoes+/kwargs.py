# Udemy com Luiz Otávio Miranda

pessoa = {
    'nome': 'Pablo',
    'sobrenome': 'Alves',
}

dados = {
    'idade': 19,
    'time': 'cruzeiro',
}

pessoaEDados = {**pessoa, **dados}
# print(pessoaEDados)


def mostrarNomeados(*args, **kwargs):
    print(f'Não nomeados {args}\n')
    # print(f'Nomeados {kwargs}\n')

    for chave, valor in kwargs.items():
        print(chave, valor)

# mostrarNomeados(1, 2, 3, 'qualquer', nome='Henrique', pais='Brasil',
# time='Real Madrid')


mostrarNomeados(**pessoaEDados)
