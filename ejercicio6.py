def reemplazar_vocal(frase, vocal):
 

  # Convertimos la vocal a mayúscula.

  vocal_mayuscula = vocal.upper()

  # Creamos una nueva cadena vacía.

  frase_modificada = ""

  # Recorremos la frase original.

  for letra in frase:
    # Si la letra es la vocal introducida, la reemplazamos por su versión en mayúscula.
    if letra == vocal:
      letra = vocal_mayuscula

    # Añadimos la letra a la cadena modificada.
    frase_modificada += letra

  return frase_modificada


def main():
 

  # Pedimos la frase al usuario.

  frase = input("Ingresa una frase: ")

  # Pedimos la vocal al usuario.

  vocal = input("Introduce una vocal: ")

  # Reemplazamos la vocal en la frase.

  frase_modificada = reemplazar_vocal(frase, vocal)

  # Mostramos la frase modificada.

  print("La frase modificada es:", frase_modificada)


if __name__ == "__main__":
  main()