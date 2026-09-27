import math


def sumar(a, b):
  return a + b


def restar(a, b):
  return a - b


def multiplicar(a, b):
  return a * b


def dividir(a, b):
  if b == 0:
    return 'Error: División por cero.'
  return a / b


def potencia(a, b):
  return a**b


def raiz_cuadrada(a):
  if a < 0:
    return 'Error: No se puede calcular raíz de un número negativo.'
  return math.sqrt(a)


def seno(a):
  return math.sin(math.radians(a))


def coseno(a):
  return math.cos(math.radians(a))


def menu():
  print('\n--- Calculadora  ---')
  print('1. Suma')
  print('2. Resta')
  print('3. Multiplicación')
  print('4. División')
  print('5. Potencia')
  print('6. Raíz cuadrada')
  print('7. Seno (grados)')
  print('8. Coseno (grados)')
  print('9. Salir')


while True:
  menu()
  opcion = input('Elige una opción (1-9): ')

  if opcion == '9':
    print('Saliendo de la calculadora...')
    break

  if opcion in ['1', '2', '3', '4', '5']:
    try:
      number1 = int(input('Ingresa el primer número: '))
      number2 = int(input('Ingresa el segundo número: '))
    except ValueError:
      print('Error: Ingresa un valor numérico válido.')
      continue

    if opcion == '1':
      print(f'Resultado: {sumar(number1, number2)}')
    elif opcion == '2':
      print(f'Resultado: {restar(number1, number2)}')
    elif opcion == '3':
      print(f'Resultado: {multiplicar(number1, number2)}')
    elif opcion == '4':
      print(f'Resultado: {dividir(number1, number2)}')
    elif opcion == '5':
      print(f'Resultado: {potencia(number1, number2)}')

  elif opcion in ['6', '7', '8']:
    try:
      number1 = int(input('Ingresa el número o ángulo: '))
    except ValueError:
      print('Error: Ingresa un valor numérico válido.')
      continue

    if opcion == '6':
      print(f'Resultado: {raiz_cuadrada(number1)}')
    elif opcion == '7':
      print(f'Resultado: {seno(number1)}')
    elif opcion == '8':
      print(f'Resultado: {coseno(number1)}')
  else:
    print('Opción no válida. Intenta de nuevo.')