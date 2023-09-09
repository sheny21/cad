nombre = input("ingresa tu nombre:")
try:
numero = int(input("ingrese un numero entero: "))
except valueError:
 print(¨El valor ingresado no es un numero entero valido.¨)
 exit()

 for i in range(numero):
  print(nombre)
  
