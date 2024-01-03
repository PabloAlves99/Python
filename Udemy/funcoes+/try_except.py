# Udemy com Luiz Otávio Miranda

A = 18
B = 0

try:
    c = A / B

except ZeroDivisionError as e:  # Informar qual erro será tratado
    print(e.__class__.__name__)
    print(e)

except NameError:
    print('Variável b não foi definida.')

except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG: ', error)
    print('Nome: ', error.__class__.__name__)

except Exception:  # Exception trata QUALQUER erro
    print('Erro desconhecido.')

print('Continuar')

# try, except, else, finally

try:
    print('Open file.')
    8 / 0

except ZeroDivisionError:
    print('Divison by zero.')

else:
    print('No error.')

finally:  # sempre será executado independente das exceções
    print('Close file.')
