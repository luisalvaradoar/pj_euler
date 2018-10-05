'''recibe como parametro un numero entero y un digito 'd', recorre el numero como 
string digito a digito, cuando un digito sea igual a 'd' se sumara 1 a cont
retorna la cantidad de veces que el digito 'd' esta en el numero '''
def contador(n, d):
	cont = 0
	ns = str(n)
	for i in range(len(ns)):
		if int(ns[i]) == d:
			cont += 1
	return(cont)

d = 9
cont = 0
suma = 0
for i in range(10 ** 10):
	cont += contador(i, d)
	if i == cont:
		print(i, cont)
		suma += i

print(suma)