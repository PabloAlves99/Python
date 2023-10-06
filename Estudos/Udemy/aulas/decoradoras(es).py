"""
Funções decoradoras e decoradores

Decorar = Adicionar / Remover / Restringir / Alterar

Funçoes decoradoras são funções que decoram outras funções

Decoradores são usados para fazer o python usar as funções decoradoras em outras funções

Decoradores são "Sintax Sugar" (Açucar sintático)
"""

def criar_funcao(func):
    
    def interna(*args, **kwargs):   # Essa função decora 
        for arg in args:
            isString(arg) # Aqui faz o teste para ver se é str     
        resultado = func(*args, **kwargs) # executa a função recebida na primeira função com os args passado depois
        
        return resultado # retorna o resultado depois de decorado e chamado novamente com o parametro para executar
    
    return interna # retorna a funcao que decorou
 
@criar_funcao # Syntax Sugar. Passa a função de baixo como parametro para essa função do @ 
def inverteString(string):
    return string[::-1]

def isString(p):
    if not isinstance(p, str):
        raise TypeError('\n\nParametro deve ser uma string!!!\n\n')
    
invertida = inverteString(123)
print(invertida) 