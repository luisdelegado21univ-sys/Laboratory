menu = (input("ingresar el menu de dia:"))
print(menu)

while menu != 4:
    print("n\ Menu de opciones")
    print("1. hambureguesa")
    print("2. pizza")
    print("3. pollo de kfc")
    print("4. sopa")
    print("5. muchas gracias por su visita, vuelve pronto!")
    
    menu = int(input("elige una opcion del (1-5): "))
    
    match menu:
        case 1:
            print("Has elegido hambureguesa.")
        case 2:
            print("Has elegido pizza.")
        case 3:
            print("Has elegido pollo de kfc.")
        case 4:
            print("Has elegido sopa.")
        case 5:
            print(" muchas gracias por su visita, vuelve pronto!")
        case _:
            print("Opción no válida. Por favor, ingrese una opción válida.")