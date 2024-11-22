import random


def obtener_palabra_secreta() -> str:
    palabras = [
        "python",
        "javascript",
        "java",
        "angular",
        "django",
        "tensorflow",
        "react",
        "typescript",
        "git",
        "flask",
    ]
    return random.choice(palabras)


def mostrat_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ""

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print("¡Bienvenidos al juego del ahorcado")
    print(f"Tenes{intentos} intentos para adivinar la palabra correcta")
    print(mostrat_progreso(palabra_secreta, letras_adivinadas),"La cantidad de letras de la palabra son: ", len(palabra_secreta))

    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor introduzca una letra válida (sólo escribir una letra)")
        elif adivinanza in letras_adivinadas:
            print("Ya has utilizado esa letra, prueba con otra")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(
                    f"¡Muy bien has acertado, la letra '{adivinanza}' esta en la palabra"
                )
            else:
                intentos -= 1
                print(f"Lo siento la letra '{adivinanza}' no esta en la palabra secreta")
                print(f"Te quedan {intentos} intentos")

        progreso_actual = mostrat_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)
        if "_" not in progreso_actual:
            juego_terminado = True
            palabra_secreta=palabra_secreta.capitalize()
            print(f"¡Felicitaciones has ganado! la palabra es: '{palabra_secreta}'")

    if intentos == 0:
        palabra_secreta=palabra_secreta.capitalize()
        print(f"Perdiste, La palabra secreta era '{palabra_secreta}'")


juego_ahorcado()
