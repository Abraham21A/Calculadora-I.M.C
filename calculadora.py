### Calculadora I.M.C ###

while True:
  # Este ciclo se ejecuta hasta que el usuario ingrese un nombre
  while True:
    name = input("Ingresa tu Nombre: ")
    # Si el nombre está vacío, se pide al usuario que ingrese un valor válido
    if name == "" :
      print("Ingresa un valor")
    # Si el nombre tiene algún valor, se sale del ciclo
    else:
      break
  
   # Este ciclo se ejecuta hasta que el usuario ingrese un peso válido
  while True:
    try:
      # Se intenta convertir el peso a float
      weigth = float(input("Ingresa tu peso: "))
      # Si el peso es menor o igual a 0 o está vacío, se pide al usuario que ingrese un valor válido
      if weigth <= 0 or weigth == "":
        print("Valor Incorrecto o Ingrese valor")
      else:
        break
    # Si el peso no puede ser convertido a float, se informa al usuario
    except ValueError:
      print("Valor Incorrecto, debe ser un numero en kilogramos")

  # Este ciclo se ejecuta hasta que el usuario ingrese una estatura válida
  while True:
    height = input("Ingresa tu estatura: ")
     # Si el valor ingresado contiene un punto, se intenta convertirlo a float
    if "." in height:
      try:
        height = float(height)
        # Si la estatura es igual a 0.0, se pide al usuario que ingrese un valor válido
        if height == 0.0:
          print("Valor Incorrecto, ingrese un valor mas alto")
        else:
          break
       # Si la estatura no puede ser convertida a float, se informa al usuario
      except ValueError:
        print("Valor Incorrecto")
    # Si el valor ingresado no contiene un punto, se informa al usuario
    else:
      print("Valor Incorrecto, debe ser un numero en centimetros")
  
  # Cálculo del índice de masa corporal (IMC)
  result = weigth / height ** 2

  # Evaluación y Imprimir el resultado del IMC
  if result < 18.5:
    print(f"{name} tu I.M.C es {result:.2f} - bajo peso")
  elif result >= 18.5 and result <= 24.9:
    print(f"{name} tu I.M.C es {result:.2f} - peso normal")
  elif result >= 25 and result <= 29.9:
    print(f"{name} tu I.M.C es {result:.2f} - sobrepeso")
  elif result  >= 30 and result <= 34.9:
    print(f"{name} tu I.M.C es {result:.2f} - obesidad")
  else:
    print(f"{name} tu I.M.C es {result:.2f} - obesidad morbida")
  
  # Preguntar si desea el usuario repetir el programa
  repeat = input("desea repetir el programa?, escriba(si/no): ")
  if repeat.lower() != "si":
    break

