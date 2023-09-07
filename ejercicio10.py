def mostrar_productos(productos):


  for producto in productos:
    print(producto)


def main():
 

  # Pedimos los productos al usuario.

  productos = input("Ingresa los productos de la cesta de la compra, separados por comas: ")

  # Convertimos los productos a una lista.

  productos = productos.split(",")

  # Mostramos los productos.

  mostrar_productos(productos)


if __name__ == "__main__":
  main()