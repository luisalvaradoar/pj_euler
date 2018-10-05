fib1 = 1
fib2 = 2
temp = 0 
suma_pares = 0

'''crea la sucesion de Fibonacci, cuando F_n = 0 mod 2 lo suma a 'suma_pares'.
se detiene hasta que F_n sea mas grande que 4000000'''
while temp < 4000000:
	temp = fib2
	if temp % 2 ==0:
		suma_pares += temp
	temp = fib1 + fib2
	fib1 = fib2
	fib2 = temp

print(suma_pares)