'''recibe como parametro un numero entero, realiza el aloritmo para 
convertir a binario, devuelve el binario como una cadena'''
def dec_din(n):
	binario = []
	while n != 0:
		if n % 2 == 0:
			binario.append(0)
			n = n // 2
		else:
			binario.append(1)
			n = n // 2
	return(binario[::-1])

'''recorre los enteros, primero convierte a string el numero luego lo convierte
a binario. Despues comprueba que sea palindromo en ambas bases, si es asi lo suma'''
suma = 0
for i in range(10 ** 6):
	ns = str(i)
	n2 = dec_din(i)
	if n2 == n2[::-1] and ns == ns[::-1]:
		suma += i

print(suma)