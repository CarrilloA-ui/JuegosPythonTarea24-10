from os import system
from random import choice
palabrasList = ["casa", "cocodrilo", "computadora", "papeleria", "boligrafo", "corchea", "audifonos", "automobil", "escaleras", "arbol", "rompecabezas"]
vidas = 5  #puse vidas fuera de while para hacer más dificil el juego, sin embargo basta con agregar vidas dentro del primer while para hacer que se restauren cada nueva ronda
puntaje = 0
# en palabrasList se pueden agregar palabras nuevas
while True:
    palabraSecreta = choice(palabrasList)
    palabraReemplazada = ["_"] * len(palabraSecreta)
    #print(palabraReemplazada)
    letrasInsertadas = set()
    #vidas = 5  #para hacer más facil el juego, quitale el primer 'gato' de esta linea
    system("cls")
    print("--¡Bienvenid@ al juego del ahorcado!--")
    print(f"Tienes {vidas} vidas.")
    print()
    print(f"¡Adivina la palabra que estoy pensando!")
    #
    while vidas > 0 and "_" in palabraReemplazada:
        print("\nPalabra: " + " ".join(palabraReemplazada))
        print(f"Vidas restantes: {vidas}")
        intento = input("Ingresa una letra o la palabra completa: ").lower()
        #a minusculas
        #
        if len(intento) ==1:
            if intento in letrasInsertadas:
                print("¡Ya intentaste esa letra!")
                continue
            letrasInsertadas.add(intento)
            if intento in palabraSecreta:
                for i, letra in enumerate(palabraSecreta):
                    if letra == intento:
                        palabraReemplazada[i] = intento
                print(f"¡exacto! '{intento}' si está en la palabra.")
            else:
                vidas -= 1
                print(f"La letra '{intento}' no esta en la palabra.")
                print(f"Vidas restantes: {vidas}.")
        #
        else: 
            if intento == palabraSecreta:
                palabraReemplazada = list(palabraSecreta)
                break
            else:
                vidas -= 1
                print(f"'{intento}' no es la palabra que estaba pensando.")
                print(f"Vidas restantes: {vidas}.")
    #verifica el resultado final
    system("cls")
    if "_" not in palabraReemplazada:
        print(f"\n¡Felicidades! adivinaste la palabra: {palabraSecreta}")
        puntaje += 100
    else:
        print(f"\n¡Ups! te quedaste sin vidas. La palabra era: {palabraSecreta}")
    continuar = input("\n¿Quieres seguir jugando? (s/n)")
    #
    if continuar.lower() != "s":
        break
#
print("\nPuntuación total: ", puntaje)
print("¡Adiós!")