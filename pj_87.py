import math
# criba de eratostenes para probar si un numero 'n' es primo. Prueba a n mod k para k < sqrt(n)
def eratostenes(n):
	if n == 1:
		return(0)
	else:
		for i in range(2 , int(math.floor(math.sqrt(n))) + 1):
			if n % i == 0:
				return(0)
		return(n)

i = 0
primos = []
while i < 7080:
	i += 1
	if eratostenes(i) != 0:
		primos.append(i)

# primosP = []
# for i in primos:
# 	primosP.append(i**4)

cont = 0
for i in primos:
	for j in primos:
		for k in primos:
			if (i**2 + j**3 + k**4) < (5 * (10**7)):
				cont += 1
			else:
				pass

