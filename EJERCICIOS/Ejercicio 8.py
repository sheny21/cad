# Preguntar por el precio del producto
precio = float(input("Introduce el precio del producto en euros: "))

# Formatear el precio con dos decimales y el símbolo de euro
precio_formateado = "{:.2f} €".format(precio)
print("El precio formateado es:", precio_formateado)

# Convertir el precio a céntimos
centimos = int(precio * 100)

# Calcular el número de euros y céntimos
euros = centimos // 100 # División entera
centimos = centimos % 100 # Resto de la división

# Mostrar el resultado
print("El precio tiene", euros, "euros y", centimos, "céntimos")
