segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = int((segundos / 3600) // 24)
hora = (segundos // 3600) % 24
segsRestante = segundos % 3600
minutos = segsRestante // 60
segundos = segsRestante % 60

print(dias, "dias", hora, "horas", minutos, "minutos e", segundos, "segundos.")
