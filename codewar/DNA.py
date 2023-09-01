# def DNA_strand(dna):
#     dna = dna.upper()
#     x = ''
#     for i in dna:
#         if i == 'A':
#             x += 'T'
#         elif i == 'T':
#             x += 'A'
#         elif i == 'C':
#             x += 'G'
#         else:
#             x += 'C'
#     return x

# import string
# def DNA_strand(dna):
#     return dna.translate(string.maketrans("ATCG","TAGC"))

def DNA_strand(dna):
    reference = { "A":"T",
                  "T":"A",
                  "C":"G",
                  "G":"C"
                  }
    return "".join([reference[x] for x in dna])

print(DNA_strand('ATTGC'))

    
