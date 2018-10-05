M = 1000
suma = 0

# suma todos los multiplos de 3 que no son divisibles por 5
for n in range( M // 3 + 1 ):
	m3 = 3 * n
	if m3 % 5 != 0:
		suma += m3
# suma todos los multiplos de 5.
for n in range( M // 5 ):
	m5 = 5 * n
	suma += m5
	
print(suma)