'''recibe dos parametros como entrada, hay dos posibles salidad. La primera
 (False, 0, 0), cuando algun numero tiene cero, cuando se han eliminado todos
 los digitos de un numero, y cuando no tienen digitos en comun. La segunda 
 posible salida es (True, int(xs), int(ys)). Para hacer la eliminacion de 
 digitos, se recorre un numero como string elemento a elemento y se compara
 con el otro string, si el elemento esta en el otro string se procede a 
 elimnarlo'''
def eliminador(x, y):
	xs = str(x)
	ys = str(y)
	i = 0
	if '0' in xs:
		return(False, 0, 0)
	while(True):
		if i == 2:
			return(False, 0, 0)
		if xs[i] in ys:
			ys = ys.replace(xs[i], '')
			xs = xs.replace(xs[i], '')
			break
		else:
			i += 1
	if (len(xs) * len(ys)) == 0:
		return(False, 0, 0)

	return(True, int(xs), int(ys))

'''recorre los enteros, cuando la salida 1 de eliminador(i,j) sea True y las 
fracciones sin eliminar digitos sea igual a cuando se elimnan y ademas 
la fraccion sea menor a 1, se imprime '''
for i in range(11, 100):
	for j in range(12, 100):
		if i != j:
			E = eliminador(i, j)
			x = E[1]
			y = E[2]
			if E[0] and x * y != 0:
				if (i / j) == (x / y) and (x / y) < 1:
					print(i, j)
