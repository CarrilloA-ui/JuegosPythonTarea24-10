#El juego del gato no supe como terminar de hacerlo correctamente
#El juego del colgado que hice si funciona
import random
tablero = [
    [" "," "," "], #fila 0: columnas 0, 1, 2
    [" "," "," "], #1: 0, 1, 2
    [" "," "," "] #2: 0, 1, 2
]
# a coordenadas 
combiGanadoras = [
    ((0,0), (0,1), (0,2)), #horizontal 0
    ((1,0), (1,1), (1,2)), #horizontal 1
    ((2,0), (2,1), (2,2)), #horizontal 2
    ((0,0), (1,0), (2,0)), #vertical 0
    ((0,1), (1,1), (2,1)), #vertical 1
    ((0,2), (1,2), (2,2)) #vertical 2
]
while True:
    print("--Bievenido al juego del 'gato'--")
    print("---------------------------------")
    print("1. jugar solo")
    print("2. jugar con alguien")
    print("3. Salir")
    modoJuego= input(f"Selecciona tu modo de juego: ")
    if modoJuego == "1":
        pass
    elif modoJuego == "2":
        pass
    elif modoJuego == "3":
        break
    else:
        break


#print("""
# 1 | 2 | 3 
# 4 | 5 | 6 
# 7 | 8 | 9 
#  """)

tablerostr = """
      |      |     
  {}  |  {}  |  {}  
______|______|______
      |      |     
  {}  |  {}  |  {}  
______|______|______
      |      |     
  {}  |  {}  |  {}  
      |      |     
    """.format(
        tablero[0][0], tablero[0][1], tablero[0][2],  # Fila 0
        tablero[1][0], tablero[1][1], tablero[1][2],  # Fila 1  
        tablero[2][0], tablero[2][1], tablero[2][2]   # Fila 2
    )
