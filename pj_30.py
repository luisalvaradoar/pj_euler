'''recive como parametro un numero, recorre el numero digito a digito
elevando a la quinta potencia este y sumandolo a total, al terminar de 
recorrerlo si total = n devuelve n, sino 0 '''
def p5(n):
	total = 0
	ns = str(n)
	for i in range(len(ns)):
		total += int(ns[i]) ** 5
	if total == n:
		return(n)
	else:
		return(0)

''' recorre todos los numeros en la funcion p5, cuando devuelva un valor diferente
a 0 lo suma'''
suma = 0
for i in range(2,10 ** 6 ):
	if p5(i) != 0:
		print(i)
		suma += i

print(suma)