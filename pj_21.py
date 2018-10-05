def suma_divisores( n ):
	suma = 0
	for i in range( 1 , round( n / 2 ) + 1 ):
		if n % i == 0:
			suma += i
	return(suma)

def amigos( n ):
	a = suma_divisores( n )
	b = suma_divisores( a )
	if n != a and n == b:
		return( n , a )
	else:
		return(0)

total = 0
for i in range(10000):
	x = amigos(i)
	if x != 0:
		total += x[0] + x[1]

print(total // 2)