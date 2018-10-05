def es_bis(anio):
	if anio%4 == 0 and (anio%400 == 0 or not anio%100 == 0):
		return True
	else:
		return False

def d01M(anio, dia1):
	if es_bis(anio):
		lista = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]
		dia1anio2 = (dia1 + 2)%7
	else:
		lista = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
		dia1anio2 = (dia1 + 1)%7

	dias = []
	for i in lista:
		dia = (i + dia1 - 1) % 7
		dias.append(dia)

	return(dias, dia1anio2)

inicio = 2
total = 0
for i in range(1901, 2000+1):
	M = d01M(i, inicio)
	inicio = M[1]
	total += M[0].count(0)

print(total)

#171
#[Finished in 0.1s]
#http://www.cuandoenelmundo.com/calendario/guatemala/1900
