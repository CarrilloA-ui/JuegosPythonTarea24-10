from os import system
from random import choice
#
palabrasList = ["casa", "cocodrilo", "computadora", "papeleria", "boligrafo", "corchea", "audifonos", "automobil", "escaleras", "arbol", "rompecabezas"]
#en palabrasList se pueden agregar palabras nuevas
puntaje = 0
#
#para obtener palabras:
def obtenerPalabra (palabrasList):
    return choice (palabrasList)
#Mostrar el estado del juego en vidas
def vidasEstado(palabraSecreta, vidas):
    print("\nPalabra:" + " ".join(palabraSecreta))
    print(f"Vidas restantes: {vidas}")
#inicia las variables
def variableReemplaza(palabraSecreta):
    return ["_"] * len(palabraSecreta), set()
#funcion de procesar intento
def prosesarIntento(palabraSecreta, palabraReemplazada, vidas, intento, letrasInsertadas):
    if len(intento) ==1:
        if intento in letrasInsertadas:
                print("¡Ya intentaste esa letra!")
                return vidas, False
        letrasInsertadas.add(intento)
        if intento in palabraSecreta:
            for i, letra in enumerate(palabraSecreta):
                if letra == intento:
                    palabraReemplazada[i] = intento
                print(f"¡exacto! '{intento}' si está en la palabra.")
            else:
                vidas -= 1
                print(f"La letra '{intento}' no esta en la palabra.")
                return vidas, False
        #
    else: 
        if intento == palabraSecreta:
            for i, letra in enumerate(palabraSecreta):
                palabraReemplazada[i]=letra
            return vidas, True    
        else:
            vidas -= 1
            print(f"'{intento}' no es la palabra que estaba pensando.")
            return vidas, True
#para mostrar un resultado:
#def mostrarResultado(palabraReemplazada):
while True:
    palabraSecreta = obtenerPalabra(palabrasList)
    vidas = 5
    #print(palabraSecreta)
    #break
    system("cls")
    print("--¡Bienvenid@ al juego del ahorcado!--")
    print(f"Tienes {vidas} vidas.")
    print()
    print(f"¡Adivina la palabra que estoy pensando!")
    #
    palabraReemplazada, letrasInsertadas = variableReemplaza(palabraSecreta)
    while vidas > 0 and "_" in palabraReemplazada:
        vidasEstado(palabraReemplazada, vidas)
        intento = input("Ingresa una letra o la palabra completa: ").lower()
        prosesarIntento(palabraSecreta, palabraReemplazada, vidas, intento, letrasInsertadas)
    #
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
print("\nPuntuación total: ", puntaje)
print("¡Adiós!")