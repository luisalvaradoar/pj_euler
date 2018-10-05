import math
# archivo con los datos
archivo = open("p099_base_exp.txt")

'''lee el archivo linea por linea, separando el string en la coma 
luego guarda cada dato como una tupla en lista como int'''
lista = []
for line in archivo:
	a = line.split(',')
	lista.append((int(a[0]), int(a[1])))

archivo.close()

'''como debemos comparar numeros de la forma a^b > x^y esto es analogo a 
compararlos b*log(a) > y*log(x), asi no gastar tanta memoria en potencias
grandes. Recorremos la lista calculando b*log(a), cuando esto sea mas grande
que el xam se guarda ese valor nuevo en xam y xam_a y xam_b como a y b de ese xam
respectivamente '''
xam = 0
xam_a = 0
xam_b = 0
for i in range(len(lista)):
	a = lista[i][0]
	b = lista[i][1]
	temp = b * math.log10(a)
	if temp > xam:
		xam = temp
		xam_a = a
		xam_b = b

'''se imprime la posicion de los maximos '''
print(lista.index((xam_a,xam_b)) + 1)