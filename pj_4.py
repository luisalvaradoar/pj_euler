''' los for anidados sirven para generar todos los numeros resultado de multiplicar
dos numeros de tres cifras, 'Ns' es el numero 'N' como string, para luego en 'Np' 
se invierta el string asi poder compararlo con 'Ns' y determinar si es capicua.
Para determinar el mas grande, se asigna una variable 'a = 1', 
cuando se encuentre el primer palindromo, 'a = nuevo_palindromo', en el siguiente
palindromo hace la comparacion si 'nuevo_palindromo > a', 
en caso lo sea asigna ese nuevo palindromo a 'a' '''
a = 1
f1 = 0
f2 = 0
for x in range(100,1000):
	for y in range(100,1000):
		N = x * y
		Ns = str( N )
		Np = Ns[::-1]
		if Ns == Np:
			if a == 1:
				a = N
			elif N > a:
				a = N
				f1 = x
				f2 = y
print( a )
print(f1,f2)

# respuesta: 906609