import itertools

archivo = open("p081_matrix.txt")

a = archivo.readlines()

archivo.close()

matriz = [None] * 80
for i in range(80):
    matriz[i] = [None] * 80

for i in range(len(a)):
	b = a[i].split(',')
	for j in range(len(b)):
		matriz[i][j] = int(b[j])

# lo anterior es solo para crear la matriz del problema :D
print(matriz[78])
print(matriz[79])