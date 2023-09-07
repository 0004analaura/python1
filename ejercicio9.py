def validar_fecha(fecha):


  # Convertimos la fecha a una lista.

  fecha = fecha.split("/")

  # Validamos el día.

  if len(fecha[0]) == 1:
    dia = int(fecha[0])
    if dia < 1 or dia > 31:
      return False
  else:
    dia = int(fecha[0])
    if dia < 1 or dia > 99:
      return False

  # Validamos el mes.

  if len(fecha[1]) == 1:
    mes = int(fecha[1])
    if mes < 1 or mes > 12:
      return False
  else:
    mes = int(fecha[1])
    if mes < 1 or mes > 99:
      return False

  # Validamos el año.

  anio = int(fecha[2])
  if anio < 1900 or anio > 2100:
    return False

  return True


def mostrar_fecha(fecha):


  # Convertimos la fecha a una lista.

  fecha = fecha.split("/")

  # Mostramos la fecha.

  print("Día:", fecha[0], "Mes:", fecha[1], "Año:", fecha[2])


def main():
  
  # Pedimos la fecha al usuario.

  fecha = input("Ingresa tu fecha de nacimiento: ")

  # Validamos la fecha.

  if not validar_fecha(fecha):
    print("La fecha introducida no es válida.")
    return

  # Mostramos la fecha.

  mostrar_fecha(fecha)


if __name__ == "__main__":
  main()