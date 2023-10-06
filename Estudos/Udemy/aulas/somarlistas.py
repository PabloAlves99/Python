listaA = [1, 2, 3, 4, 5, 6, 7]
listaB = [1, 2, 3, 4]
listaSomada = [x + y for x, y in zip(listaA, listaB)]

# end = min(len(listaA), len(listaB))
# listaSomada = []
# for i in range(end):
#     listaSomada.append(listaA[i] + listaB[i])  
# print(listaSomada)


# listaSomada = []
# for i, _ in enumerate(listaB):
#     listaSomada.append(listaA[i] + listaB[i])
    
print(listaSomada)