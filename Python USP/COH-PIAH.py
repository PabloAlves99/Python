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
    
    grauSimilar = sum([abs(as_a[i] - as_b[i]) for i in range(6)])
    grauSimilar /= 6            
    
    return grauSimilar
    
def calcula_assinatura(texto):
    
    sentencas = separa_sentencas(texto)
    
    frases = []  
    for sentenca in sentencas:
        frase = separa_frases(sentenca)
        frases.extend(frase)
    
    lista_palavras = []
    for frase in frases:
        palavras = separa_palavras(frase)
        lista_palavras.extend(palavras)
    
    palavras_unicas = n_palavras_unicas(lista_palavras)
    palavras_diferentes = n_palavras_diferentes(lista_palavras)

    
    #wal = tamanho_medio_palavra(lista_palavras)
    wal = sum(len(palavra) for palavra in lista_palavras) / len(lista_palavras)
    
    #ttr = relacao_type_token(lista_palavras)
    ttr = palavras_diferentes / len(lista_palavras)
    
    #hlr = razao_hapax_legomena(lista_palavras)
    hlr = palavras_unicas / len(lista_palavras)
    
    #sal = tamanho_medio_sentenca(sentenca)
    sal = sum(len(sentenca) for sentenca in sentencas) / len(sentencas)

    #sac = complexidade_media_sentenca(sentenca, frase)
    sac = len(frases) / len(sentencas)
    
    #pal = tamanho_medio_frase(frase)
    pal = sum(len(frase) for frase in frases) / len(frases)
    
    return [wal, ttr, hlr, sal, sac, pal]
    
def avalia_textos(textos, ass_cp):
    as_a = []
        
    for texto in textos:
        as_a.append(calcula_assinatura(texto)) 
  
    Sab = [compara_assinatura(as_a[i], ass_cp) for i in range(len(textos))]
    infectado = Sab.index(min(Sab))
    
    infectado += 1
    
    return infectado

    
def main():  
    ass_cp = le_assinatura()
    textos = le_textos()
    autor_infectado = avalia_textos(textos, ass_cp)
    
    
    print(f"O autor do texto {autor_infectado} está infectado com COH-PIAH")
       
       
if __name__ == '__main__':
    main()