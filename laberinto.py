laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],   #definimos el laberinto siendo "X" los muros, los "espacios" por donde
    [' ', 'X', ' ', 'X', ' '],    #se puede recorrer el laberinto y "S" la salida del laberinto
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) #defino las casillas de los muros

for i in range (5):
        print (laberinto[i])  #Consigo crear el laberinto