"""
Atividade do CodeWar
"""


def dna_strand(dna):
    """
    Função simples para manipular DNA
    """
    reference = {"A": "T",
                 "T": "A",
                 "C": "G",
                 "G": "C"
                 }
    return "".join([reference[x] for x in dna])


print(dna_strand('ATTGC'))
