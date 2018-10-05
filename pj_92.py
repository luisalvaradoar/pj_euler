'''dado un numero entero, la funcion lo convierte a string luego recorre el
string elemento a elemento sumando el cuadrado de este a s, al final retorna
s '''
def sD(n):
	ns = str(n)
	s = 0
	for i in range(len(ns)):
		s += int(ns[i])**2
	return(s)

# forma recursiva de la cadena de digitos cuadrados
'''para mejorar el algoritmo en el caso que se analicen varios numeros
guardaremos la cadena de numeros que se forman y al final terminan en 89'''
# se debe definir cadena = []
def sDc(n):
	if n == 89:
		return(89)
	elif n == 1:
		return(1)
	else:
		return sDc(sD(n))




i = 1
cont = 0
while i < 10**7:
	cadena = []
	i += 1
	if sDc(i) == 89:
		cont += 1

print(cont)

# se tardo 234s D:
