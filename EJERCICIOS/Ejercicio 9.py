import datetime
fecha = input('Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ')
dia, mes, año = list(map(int, fecha.split("/")))
fecha_nacimiento = datetime.date(año, mes, dia)
print(f"El día es {fecha_nacimiento.day}")
print(f"El mes es {fecha_nacimiento.month}")
print(f"El año es {fecha_nacimiento.year}")
