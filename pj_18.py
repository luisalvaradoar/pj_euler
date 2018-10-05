import itertools

'''genera toda las posibles combinaciones de movimientos en la piramide 
como cadenas de 'D' e 'I', el largo de la cadena se establece en repeat'''
movimientos = list(itertools.product('ID', repeat = 14))

#piramide = [[[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]] # ejemplo, repeat = 3

piramide = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65],\
[19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92],\
[41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29,],\
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,],\
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],\
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

'''recorre todas las combinaciones de movimientos, comienza en (0,0) que es la
cima de la piramide. Luego va leyendo la cadena de movimiento, para las I's
 suma uno a la primera coordenada (x + 1, y), para las D's suma uno a cada
 coordenada (x + 1, y + 1). Luego guarda la suma del camino, la cadena de 
 movimientos y el camino'''
SCmc = []
for i in range(len(movimientos)):
	mov = movimientos[i]
	x = 0
	y = 0
	camino = [75]
	for j in range(len(mov)):
		if mov[j] == 'I':
			x += 1
		elif mov[j] == 'D':
			x += 1
			y += 1

		camino.append(piramide[x][y])

	SCmc.append([sum(camino), mov, camino])

# la suma mas grande
print(max(SCmc))