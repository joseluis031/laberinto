laberinto = [] #defino mi lista del laberinto
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) #defino las casillas de los muros

def creation_lab():
    for _ in range (5):
        laberinto.append(([' ']*5))
    for i in muro:
        laberinto[int(i[0])][int(i[1])] = 'X'
    laberinto [4] [4] = "Salida"
    return laberinto

lab = creation_lab()
for i in range (5):
        print (lab[i])  #Consigo crear el laberinto
        
def recorrido():
    movimientos = []
    a = 0 #eje Y
    b = 0 #eje X
    c = 0 #'contrario' de a
    d = 0 #'contrario' de b
    while laberinto [a][b] != "Salida" #Genero un bucle que me va a recorrer el laberinto mientras no este en la casilla de salida, es decir, hasta que llegue a la salida, el bucle ira desarrollandose
        if d <= a < 4 and laberinto[a+1][b] != 'X':
            movimientos.append("Abajo")
            a += 1
            d = a - 1 
            d = c
        elif c <= b < 4 and laberinto[a][b+1] != 'X':
            movimientos.append("Derecha")
            b += 1
            c = b - 1
            a = d
        elif 0 < b < c and laberinto[m][n-1] != 'X':
            movimientos.append("Izquierda")
            b -= 1
            c = b + 1
            d = b
        else:
            movimientos.append("Arriba")
            a -= 1
            d = a + 1
            c = b
    return movimientos

print("Ls movimientos son:\n{}".format(recorrido()))  
         
