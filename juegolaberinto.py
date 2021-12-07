laberinto = [
    ['Entrada:', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]


x = 0
y = 0


print("Comienzas en la posición (0,0)")
print((laberinto[y])[x])

def recorrido():
    movimientos = []