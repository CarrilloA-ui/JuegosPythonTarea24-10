import random
tablero = [[" "," "," "],[" "," "," "],[" "," "," "]]
combiGanadoras = [
    ((0,0), (0,1), (0,2)), #horizontal 0
    ((1,0), (1,1), (1,2)), #horizontal 1
    ((2,0), (2,1), (2,2)), #horizontal 2
    ((0,0), (1,0), (2,0)), #vertical 0
    ((0,1), (1,1), (2,1)), #vertical 1
    ((0,2), (1,2), (2,2)) #vertical 2
]
#imprimir tablero
def printTablero(): #para imprimir el tablero
    print("""
 {} | {} | {} 
----+----+----
 {} | {} | {} 
----+----+----
 {} | {} | {} 
          """)
# Tomar imput del jugador

#ganar o perder

#
printTablero()