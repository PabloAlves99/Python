segundosStr = input("Por favor, entre com o número de segundos que deseja converter: ")

segundos = int(segundosStr)

dias = segundos // 86400
restoSegundos = segundos % 86400
horas = restoSegundos // 3600
restosegundos = segundos % 3600
minutos = restosegundos // 60
seg = restosegundos % 60

print(dias, "dias,", horas,"horas,", minutos, "minutos e", seg,"segundos.")