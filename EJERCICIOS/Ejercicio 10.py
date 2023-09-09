def main():
    # Pedir al usuario que ingrese los productos separados por comas
    productos = input("Ingrese los productos de la cesta de compra, separados por comas: ")
    
    # Dividir los productos en una lista usando la coma como separador
    lista_productos = productos.split(',')
    
    # Mostrar cada producto en una línea distinta
    print("Productos en la cesta de compra:")
    for producto in lista_productos:
        print(producto.strip())  # strip() elimina espacios en blanco al inicio y final

if __name__ == "__main__":
    main()
