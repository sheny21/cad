# Pedir al usuario que introduzca una frase
frase = input("Introduce una frase: ")

# pedir al usuario que introduzca una vocal
vocal = input("introduce una vocal: ")

# validar que la entrada sea una vocal 
if len(vocal) ! = 1 or vocal.lower () not in "aeiou":
    print(" por favor, introduce una sola vocal (a, e, i, o, u,).")
else:
    emplazar la vocal en minusculas con la volcal en minusculas en la frase 
    frase_modificada = frase.remplace(vocal.lower(), vocal.upper())

# Mostrar por la frase modificada por pantalla
print("frase con la vocal en mayusculas:", frase_modificada)
