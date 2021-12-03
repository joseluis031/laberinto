laberinto = [] #defino mi lista del laberinto
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) #defino las casillas de los muros

def creation_lab():
    for _ in range (5):
        laberinto.append(([' ']*5))
    for i in muro:
        laberinto[int(i[0])][int(i[1])] = 'X'
    return laberinto

lab = creation_lab()
for i in range (5):
        print (lab[i])  #Consigo crear el laberinto