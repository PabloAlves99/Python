#Esse modelo precisa que o formulario tenha um step = "5" para que não dê erro em receber o valor

sacar = input("Qual valor você deseja sacar? ")


liberar = int(sacar)

nota100 = liberar // 100

resto100 = liberar % 100
nota50 = resto100 // 50

resto50 = resto100 % 50
nota10 = resto50 // 10

resto10 = resto50 % 10
nota5 = resto10 // 5

sobra = resto10 % 5

print ("O caixa eletrônico vai te entregar as seguintes notas:")
print(nota100, "notas de R$100")
print(nota50, "notas de R$50")
print(nota10, "notas de R$10")
print(nota5, "notas de R$5")
print(f'\nSobrou R${sobra:.2f}')