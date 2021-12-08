laberinto = [] #defino mi lista del laberinto
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) #defino las casillas de los muros
for _ in range (5):
        laberinto.append(([' ']*5))
for i in muro:
        laberinto[int(i[0])][int(i[1])] = 'X'
laberinto [4] [4] = "Salida"
for i in range (5):
        print (laberinto[i])  #Consigo crear el laberinto
        
def recorrido():
    movimientos = []
    a = 0 #eje Y
    b = 0 #eje X
    c = 0 #'contrario' de a
    d = 0 #'contrario' de b
    while laberinto [a][b] != "Salida": #Genero un bucle que me va a recorrer el laberinto mientras no este en la casilla de salida, es decir, hasta que llegue a la salida, el bucle ira desarrollandose
        if d <= a and laberinto[a+1][b] != 'X': #Cuando esas condiciones den como resultado una casilla diferente de 'X', añado a los movimientos "Abajo"
            movimientos.append("Abajo")
            a += 1
        elif c <= b < 4 and laberinto[a][b+1] != 'X': #Cuando esas condiciones den como resultado una casilla diferente de 'X', añado a los movimientos "Derecha"
            movimientos.append("Derecha")
            b += 1
            c = b-1
            d = a
        elif b < c and laberinto[a][b-1] != 'X': #Cuando esas condiciones den como resultado una casilla diferente de 'X', añado a los movimientos "Izquierda"
            movimientos.append("Izquierda")
            b -= 1
        else:
            movimientos.append("Arriba") #Cuando no ocurra ninguna de las condiciones anteriores, añado a los movimientos "Arriba"
            a -= 1
            
            
    return movimientos

print("Los movimientos son:\n{}".format(recorrido()))   #Le doy formato a la funcion
         
