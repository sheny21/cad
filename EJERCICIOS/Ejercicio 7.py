# Pedir al usuario  su direccion de correo electronico
correo = input("introduce tu direccion de correo electronico: ")

# dividir la direcion de correo en nombre de usuario y dominio 
nombre-usuario, dominio = correo.split("@")

# crear la nueva direccion de correo con el mismo nombre de usuario pero con el dominio ceu.es
nuevo_correo = nombre_usuario + "@ceu.es"

# Mostrar la nueva direccion de correo por pantalla
print("Tu nuevo correo electrónico es: ", nuevo_correo)
