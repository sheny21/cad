# pedir al usuario un numero de telefono con el formate +34-xxxxxxxxx-xx
telefono = input("ingresa un numero de telefono con formate +34-xxxxxxxxx-xx ")

# Dividir el numero de telefono en partes: prefijo, numero y extencion
partes = telefono.split("-")

# verificar si el numero de telefono tiene el formato correcto
if len(partes) !=3 or partes [0] != "+34" or len(partes[1]) !=9 or len(partes[2]) !=2:
print("el numero de telefono no tiene el formato correcto. ")
else:
    numero = partes[1] # obtener la parte del numero sin el prefijo ni la extencion
    print("numero de telefono sin prefijo ni extencion" , numero)
    
