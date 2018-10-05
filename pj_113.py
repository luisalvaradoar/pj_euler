# 0 = numero creciente
# 1 = numero decreciente
# 2 = numero bouncy

'''la funcion bouncy recibe como parametro un numero entero, convierte el numero
a string asi poder recorrer el numero digito a digito, primero compara digitos
adyacentes con la relacion <=, cuando dos digitos cumplan suma 1 a iN
cuando no termina el ciclo, luego compara iN, cuando iN sea igual al numero de 
parejas de digitos adyacentes de n, es porque el numero es creciente. Analogamente
para determinar si es decreciente. Cuando ni un if devuelva algo, significa que es bouncy '''

def bouncy(n):
	ns = str(n)
	iN = 0
	dN = 0
	for i in range(len(ns) - 1):
		if ns[i] <= ns[i + 1]:
			iN += 1
		else:
			break

	if iN == (len(ns) - 1):
		return(0)

	for i in range(len(ns) - 1):
		if ns[i] >= ns[i + 1]:
			dN += 1
		else:
			break

	if dN == (len(ns) - 1):
		return(1)

	return(2)

total = 0
for i in range(1,10 ** 10 ):
	if bouncy(i) != 2:
		total += 1

print(total)