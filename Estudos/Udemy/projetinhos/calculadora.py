while True:
    try:
        n1 = float(input("\nDigite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
    except:
        print("Digite apenas números, qualquer outro tipo não funcionará...")
        continue

    opera = input("Digite a operação que deseja fazer (apenas +, -, / e *) ")
    if opera not in '+-*/':
        print('Digite apenas os operadores mencionados, essa é uma calculadora simples! \n')
        continue
    if len(opera) > 1:
        print("Digite apenas um operador para fazer o calcular!")
        continue

    if opera == '+':
        resultado = n1 + n2
        print(f'\nResultado:\n{n1} {opera} {n2} = {resultado}')
    elif opera == '-':
        resultado = n1 - n2
        print(f'\nResultado:\n{n1} {opera} {n2} = {resultado}')
    elif opera == '/':
        resultado = n1 / n2
        print(f'\nResultado:\n{n1} {opera} {n2} = {resultado}')
    elif opera == '*':
        resultado = n1 * n2
        print(f'\nResultado:\n{n1} {opera} {n2} = {resultado}')
    else:
        print('Não deveria chegar aqui \n')

    condicao = input('\nDeseja fazer outro calculo? (sim ou não) ')

    abreviacao = (condicao.lower() == 'n') or (condicao == 'N')
    qualquerTamanho = (condicao.lower() == 'não') or (
        condicao.lower() == 'nao')

    if qualquerTamanho or abreviacao:
        break

print(f'\nFim do calculo')
