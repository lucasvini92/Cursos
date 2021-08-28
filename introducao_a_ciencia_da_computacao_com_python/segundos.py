valor = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = valor//86400
horas = (valor%86400)//3600
rest_horas = (valor%86400)%3600
minutos = rest_horas//60
segundos = rest_horas%60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
