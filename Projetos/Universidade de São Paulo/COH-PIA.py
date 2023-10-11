import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    x = 0
    for a, b in zip(as_a, as_b):
        x += abs(a) - abs(b) 
    return x / 6

def calcula_assinatura(texto):
    
    sentencas = separa_sentencas(texto) # lista de sentencas
 
    frases = []
    for sentenca in sentencas:
        frases.extend(separa_frases(sentenca))
        
    palavras = []
    for frase in frases:
        palavras.extend(separa_palavras(frase))

    palavras_unicas = n_palavras_unicas(palavras)
    palavras_diferentes = n_palavras_diferentes(palavras)
    
    x = 0
    for palavra in palavras:
        x += len(palavra)        
    tamanho_medio_palavra = x / len(palavras)
    
    type_token = palavras_diferentes / len(palavras)
    hapax_legomana = palavras_unicas / len(palavras)
    
    x = 0
    for sentenca in sentencas:
        x += len(sentenca)
    tamanho_medio_sentenca = x / len(sentencas)
    
    complexidade_sentenca = len(frases) / len(sentencas)
    
    x = 0
    for frase in frases:
        x += len(frase)
    tamanho_medio_frase = x / len(frases)
    
    return [tamanho_medio_palavra, type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = []
    for texto in textos:
        assinatura = calcula_assinatura(texto)
        assinaturas.append(compara_assinatura(assinatura, ass_cp))
    
    contaminado = assinaturas[0]
    texto_contaminado = 0
    for i, assinatura in enumerate(assinaturas):
        if assinatura < contaminado:
            contaminado = assinatura
            texto_contaminado = i
    
    return texto_contaminado + 1   
    
def digitar_textos():
    textos = []
    while True:
        texto = input(f'Digite o texto {len(textos) + 1}: ').strip()
        
        if len(texto) == 0:
            return textos

        else:
            textos.append(texto)       

if __name__ == '__main__':
    assinatura_contaminada = le_assinatura()
    textos = le_textos()
    provavel_contaminacao = avalia_textos(textos, assinatura_contaminada)
    
    print(f'O texto contaminado por COH-PIAH é o texto {provavel_contaminacao}.')