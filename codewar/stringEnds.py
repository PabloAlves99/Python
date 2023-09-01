# def solution(text, ending):
#     x = text[::-1]
#     y = ending[::-1]
#     n = len(ending)
    
#     if x < y:
#         return False
    
#     for xi, yi in zip(x, y):
#         ret = False
#         if xi == yi:
#             ret = True
#         else:
#             return False
#         n += -1
#         if n == 0:
#             break
#     return ret

def solution(string, ending):
    return string.endswith(ending) #O endswith()método retorna True se a string terminar com o valor especificado, caso contrário, False.

x = 'fsasfawsfdsadsdsa'
y = 'sadsdsa'
print(solution(x, y))