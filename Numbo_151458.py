# Numbo
# Heidy Michelle Esquivel Perez
# Programación orientada a objetos

## Declaracion de variables

tablero = [[0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0]]

jugador2 = ""
jugador1 = ""
jugador_actual = 1
numero_actual = 1
ultima_posicion = (None, None)

# Funciones del juego   

def mostrar_instrucciones():
    print(
        """
    Bienvenid@ a NUMBO
        Las instrucciones de juego son las siguientes:
        Es un juego para dos jugadores con turnos intercalados
        En cada turno, cada jugador coloca en una posición vacía del tablero de 6*6 un numero consecutivo del 1 al 36.
    REGLA:
        Cada nuevo número debe colocarse a una distancia ininterrumpida como el movimiento de la torre en ajedrez en base al turno anterior. 
        "Ininterrumpido" significa que no interviene ningún número en el movimiento horizontal o vertical.
    FIN DEL JUEGO:
        El juego termina cuando algun jugador se quede sin movimientos legales.
        El jugador que se queda sin movimientos pierde y el otro gana.
         
          """
    )
    
def mostrar_tablero(tablero):
    print("Este es el tablero actual: ")
    tablero_ordenado = ""
    for fila in tablero:
        for celda in fila:
            tablero_ordenado = tablero_ordenado + str(celda)
            tablero_ordenado = tablero_ordenado + " "
        tablero_ordenado = tablero_ordenado + "\n"
    print(tablero_ordenado)
    return

def movimiento_legal(tablero, fila, columna, ultima_fila, ultima_columna):
    if tablero[fila][columna] != 0:
        return False
    
    if ultima_fila is None and ultima_columna is None:
        return True
    
    if fila == ultima_fila or columna == ultima_columna:
        if fila == ultima_fila:
            start, end = min(columna, ultima_columna), max(columna, ultima_columna)
            return all(tablero[fila][i] == 0 for i in range(start + 1, end))
        elif columna == ultima_columna:
            start, end = min(fila, ultima_fila), max(fila, ultima_fila)
            return all(tablero[i][columna] == 0 for i in range(start + 1, end))
    
    return False

def fin_juego(tablero):
    
    if numero_actual > 36:
        return True
        
    for fila in range(6):
        for columna in range(6):
            if movimiento_legal(tablero, fila, columna, *ultima_posicion):
                return False
    return True


## Ejecucion del juego

mostrar_instrucciones()
    
jugador1 = input("Jugador 1, ingrese su nombre: ")
jugador2 = input("Jugador 2, ingrese su nombre: ")

while not fin_juego(tablero):
    
    mostrar_tablero(tablero)
    print("El numero que se colocara es: "+ str(numero_actual))
    print(f"Turno del Jugador {jugador_actual}({jugador1 if jugador_actual == 1 else jugador2}):")
    
    while True:
        try:
            fila = int(input("Ingrese su fila del 1 al 6: ")) - 1  # 1
            columna = int(input("Ingrese su columna del 1 al 6: ")) - 1  # 2
            
            if 0 <= fila < 6 and 0 <= columna < 6:

                if movimiento_legal(tablero, fila, columna, *ultima_posicion):
                    break
                else:
                    print("Jugada ilegal, intente nuevamente")        
           
            else:
                print("Ingreso una columna o fila incorrecta")
                
        except:
            print("Algo salió mal, intente nuevamente")
    
    tablero[fila][columna] = numero_actual
    ultima_posicion = (fila, columna)
    numero_actual += 1
    jugador_actual = 3 - jugador_actual

if fin_juego(tablero):
    mostrar_tablero(tablero)
    print(f"El Jugador {jugador_actual} ({jugador1 if jugador_actual == 1 else jugador2}) no tiene movimientos válidos. ¡El Jugador {3 - jugador_actual}({jugador1 if jugador_actual == 2 else jugador2}) gana!")

mostrar_tablero(tablero)
print("El juego ha terminado en empate.")

