import math

'''los for anidados crean todas las permutaciones de (a,b) enteros
luego se calcula c por el teorema de pitagoras, y pf es la parte irracional de c
si pf es 0 es porque (a^2 + b^2) son un cuadrado perfecto. El if tiene 
las condiciones necesarias para la terna (a,b,c)'''
for a in range(1,1000):
	for b in range(1,1000):
		c = math.sqrt( a ** 2 + b ** 2 )
		pf = c - math.floor( c )
		if pf == 0 and a + b + c == 1000:
			print( int(a * b * c ))
			break