def limpiar_telefono(telefono):
  """
  Limpiamos el numero eliminando el prefijo 

  """

  # Eliminamos el prefijo.

  telefono = telefono[4:]

  # Eliminamos la extensión.

  if telefono.endswith("-"):
    telefono = telefono[:-1]

  return telefono


def main():
  

  # Pedimos el número de teléfono.

  telefono = input("Ingresa un número de teléfono: ")

  # Limpiamos el número de teléfono.

  telefono_limpio = limpiar_telefono(telefono)

  # Mostramos el número de teléfono limpio.

  print("El número de teléfono limpio es:", telefono_limpio)


if __name__ == "__main__":
  main()