# Universidade de São Paulo
segundosStr = input("Digite a quantidade de segundos que deseja converter: ")
totalSegundos = int(segundosStr)

horas = totalSegundos // 3600

segundosRestantes = totalSegundos % 3600

minutos = segundosRestantes // 60

segFinal = segundosRestantes % 60

print(horas, "horas, ", minutos, "minutos e", segFinal, "segundos.")
