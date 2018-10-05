'''recibe un numero, si este tiene mas de diez digitos, toma el numero lo vuelve string
y devuelve los ultimos 10 elementos, luego lo devuelve en int. Si tiene menos
de 10, solo devuelve el numero '''
def acotador10(n):
	if len(str(n)) > 10:
		return(int(str(n)[-10:]))
	else:
		return(n)

'''recorre las potencias de 2, cuando esta exceda los 10 digitos corta hasta el 
decimo y sigue, ya que solo nos interesan las ultimas 10 '''

a = 1
for i in range(1,7830457 + 1):
	a *= 2
	a = acotador10(a)

# falta multiplicar las ultimas diez cifras de 2^7830457 por 28433 y sumarle 1
print(acotador10(28433 * a) + 1)