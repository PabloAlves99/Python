def solution(string, ending):
    return string.endswith(ending) #O endswith()método retorna True se a string terminar com o valor especificado, caso contrário, False.

x = 'fsasfawsfdsadsdsa'
y = 'sadsdsa'
print(solution(x, y))