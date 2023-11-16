from pathlib import Path

CAMINHO = Path()

# .
print(CAMINHO)

# C:\Users\pablo\Documents\pablo_TI\pablo_programacao\Python
print(CAMINHO.absolute())

# C:\Users\pablo
print(CAMINHO.home())

# c:\Users\pablo\Documents\pablo_TI\pablo_programacao\Python\Estudos\Udemy\modulos\aula_pathlib.py
print(Path(__file__))


novo_caminho = CAMINHO.absolute() / 'TESTE' / 'TESTE.TXT'
# C:\Users\pablo\Documents\pablo_TI\pablo_programacao\Python\TESTE\TESTE.TXT
print(novo_caminho)

# C:\Users\pablo\Documents\pablo_TI\pablo_programacao\Python\TESTE
print(novo_caminho.parent)

criar_arquivo = Path(__file__).parent / 'aula_pathlib.txt'
print(criar_arquivo)

criar_arquivo.touch(exist_ok=True)  # CRIA
# criar_arquivo.write_text('Olá mundo\n')  # ESCREVE
# criar_arquivo.unlink()  # APAGA

# criar_pasta = criar_arquivo  # APENAS PARA TER UM CAMINHO
# criar_pasta.mkdir(exist_ok=True)  # CRIA PASTA

with criar_arquivo.open('a+') as arquivo:
    arquivo.write('Escrever novamente\n')
