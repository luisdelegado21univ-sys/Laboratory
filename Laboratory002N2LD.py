secret = 8
intento = 3

while intento > 0:
    adivina = int(input("Adivina el numero secreto entre 1 y 100: "))
    intento -= 1
    if adivina == secret:
        print("¡Felicidades! Adivinaste el numero.")
        break
    elif adivina < secret:
        print("Demasiado bajo. Intenta otra vez.")
    else:
        print("Demasiado alto. Intenta otra vez.")

if intento == 0:
    print(f"Lo siento, no adivinaste el numero. Era {secret}.")