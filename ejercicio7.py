def crear_correo_ceu(correo):


  # Obtenemos el nombre de usuario.

  nombre = correo.split("@")[0]

  # Creamos el nuevo correo electrónico.

  nuevo_correo = nombre + "@ceu.es"

  return nuevo_correo


def main():
 
  # Pedimos el correo electrónico al usuario.

  correo = input("Ingresa tu correo electrónico: ")

  # Creamos el nuevo correo electrónico.

  nuevo_correo = crear_correo_ceu(correo)

  # Mostramos el nuevo correo electrónico.

  print("Tu nuevo correo electrónico es:", nuevo_correo)


if __name__ == "__main__":
  main()