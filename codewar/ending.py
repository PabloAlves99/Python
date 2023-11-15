def solution(string, ending):
    # O endswith()método retorna True se a string terminar com o valor
    # especificado, caso contrário, False.
    return string.endswith(ending)


x = 'fsasfawsfdsadsdsa'
y = 'sadsdsa'
print(solution(x, y))
