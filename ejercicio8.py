def mostrar_precio(precio):


  # Obtenemos el número de euros.

  euros = precio //1

  # Obtenemos el número de céntimos.

  centimos = precio % 10

  # Mostramos el precio.

  print("El precio es:", euros, "euros y", centimos, "céntimos.")


def main():
  

  # Pedimos el precio al usuario.

  precio = input("Ingresa el precio del producto: ")

  # Convertimos el precio a un número decimal.

  precio = float(precio)

  # Mostramos el precio.

  mostrar_precio(precio)


if __name__ == "__main__":
  main()