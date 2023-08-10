import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

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
    GSab = 0
    for dadosa, dadosb in zip(as_a, as_b):
        GSab += abs(dadosa - dadosb)
        
    similaridade = GSab / len(as_a)
    return similaridade
    
def calcula_assinatura(texto):
    sentenca = separa_sentencas(texto)
    frase = separa_frases(sentenca)
    lista_palavras = separa_palavras(frase)
    palavras_unicas = n_palavras_unicas(lista_palavras)
    palavras_diferentes = n_palavras_diferentes(lista_palavras)
    
    wal = 0
    ttr = 0
    hlr = 0
    sal = 0
    sac = 0
    pal = 0
    
    #wal = tamanho_medio_palavra(lista_palavras)
    for palavra in lista_palavras:
        wal += len(palavra)
    wal = wal / len(lista_palavras)
    #ttr = relacao_type_token(lista_palavras)
    ttr = palavras_diferentes / len(lista_palavras)
    #hlr = razao_hapax_legomena(lista_palavras)
    hlr = palavras_unicas / len(lista_palavras)
    #sal = tamanho_medio_sentenca(sentenca)
    sal = sum(len(lista_palavras) for palavra in lista_palavras) / len(sentenca)
    #sac = complexidade_media_sentenca(sentenca, frase)
    sac = len(frase) / len(sentenca)
    #pal = tamanho_medio_frase(frase)
    for palavra in frase:
        pal += len(palavra)
    pal = pal / len(frase)
    
    return [wal, ttr, hlr, sal, sac, pal]
    
def avalia_textos(textos, ass_cp):
    as_a = []
    as_b = ass_cp
    Sab = []
        
    for texto in textos:
        as_a.append(calcula_assinatura(texto)) 
        similaridade = compara_assinatura(as_a, as_b)
        Sab.append(similaridade)

    escritor = Sab.index(min(Sab))
    print(f"O autor do texto {escritor} está infectado com COH-PIAH")
    
def main():  
    ass_cp = le_assinatura()
    textos = le_textos()
    avalia_textos(textos, ass_cp)
       
if __name__ == '__main__':
    main()