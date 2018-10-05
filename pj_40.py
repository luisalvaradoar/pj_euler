#  crearemos donde se guardara la concatenacion de numeros
N = ""

'''iniciando en el 1 recorremos los naturales sumando a 'cont' el largo del numero que se 
concatena a 'N' hasta que cont sea mayor a un millon
'''
i = 1
cont = 0
while(True):
	if cont < 1000000:
		N += str(i)
		cont += len(str(i))
		i += 1
	else:
		break

# esto hace la suma de los digitos 1,10,100,1000,10000,100000,1000000, como 10^i con -1 0 <= i <= 6
total = 1
for i in range(7):
	total *= int(N[ 10 ** i -1 ])

print(total)