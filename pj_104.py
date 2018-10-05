import math

''' la funcion pandigitalQ recibe como parametro un numero, el cual vuelve
cadena y la ordena, luego la compara con la lista que contiene los digitos
del 1-9, si son iguales es porque el numero es pandigital, en ese caso
retorna 1, sino retorna 0'''
def pandigitalQ(n):
	comp = ['1','2','3','4','5','6','7','8','9']
	ns = sorted(str(n))
	if ns == comp:
		return(1)
	else:
		return(0)

'''recibe un numero, si este tiene mas de nueve digitos, toma el numero lo vuelve string
y devuelve los ultimos 9 elementos, luego lo devuelve en int. Si tiene menos
de 9, solo devuelve el numero '''
def acotador_u9(n):
	if len(str(n)) > 9:
		return(int(str(n)[-9:]))
	else:
		return(n)

'''recibe un numero, si este tiene mas de nueve digitos, toma el numero lo vuelve string
y devuelve los primeros 9 elementos, luego lo devuelve en int. Si tiene menos
de 9, solo devuelve el numero '''
def acotador_p9(n):
	if len(str(n)) > 9:
		return(int(str(n)[0:9]))
	else:
		return(n)

k = 3
fib1 = 1
fib2 = 2
temp = 0 
while(True):
	temp = fib2
	if pandigitalQ(acotador_u9(temp)) == 1:
		if pandigitalQ(acotador_p9(temp)) == 1:
			print(k)
			break
	temp = fib1 + fib2
	fib1 = fib2
	fib2 = temp
	k += 1
