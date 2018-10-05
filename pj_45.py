import math

# n-esimo numero triangular por la forma cerrada
def Tn(n):
	return((n * (n + 1)) // 2)

''' recibe un numero entero y comprueba si es un numero pentagonal, si es 
pentagonal retorna (True, n) donde n es el indice del n-esimo numero pentagonal,
sino es pentagonal retorna (False, 0)'''
def PnQ(n):
	disc = (1 + math.sqrt(1 + 24 * n)) / 6
	if disc - math.floor(disc) == 0:
		return(True, int(disc))
	else:
		return(False, 0)

''' recibe un numero entero y comprueba si es un numero hexagonal, si es 
hexagonal retorna (True, n) donde n es el indice del n-esimo numero hexagonal,
sino es pentagonal retorna (False, 0)'''
def HnQ(n):
	disc = (1 + math.sqrt(1 + 8 * n)) / 4
	if disc - math.floor(disc) == 0:
		return(True, int(disc))
	else:
		return(False, 0)

''' recorre los numeros triangulares desde T_2, cuando las PnQ y HnQ retornen
ambas True imprimira el numero y el indice T_i, P_j y H_k, respectivamente
y luego suma uno al contador, cuando se encuentren la cantidad de numeros
sale del ciclo'''
cont = 0
i = 2
while(True):
	x = Tn(i)
	if PnQ(x)[0] and HnQ(x)[0]:
		print(x)
		print(i)
		print(PnQ(x)[1])
		print(HnQ(x)[1])
		i += 1
		cont += 1
		if cont == 3:
			break
	else:
		i += 1