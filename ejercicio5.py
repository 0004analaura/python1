def invertir_frase(frase):

  # Creamos para ingresar la frase

  palabras = frase.split()

  # Invertimos la lista de palabras.

  palabras.reverse()

  # Convertimos la lista de palabras en una frase.

  frase_invertida = " ".join(palabras)

  return frase_invertida


def main():


  # Pedimos la frase al usuario.

  frase = input("Ingresa una frase: ")

  # Invertimos la frase.

  frase_invertida = invertir_frase(frase)

  # Mostramos la frase invertida.

  print("La frase invertida es:", frase_invertida)


if __name__ == "__main__":
  main()