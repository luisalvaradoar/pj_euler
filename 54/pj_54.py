def separador(mano):
	lista_valor = []
	lista_suit = []
	valor_carta = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, 'T':9, 'J':10, 'Q':11, 'K':12, 'A':13}

	for i in mano.split(' '):
		lista_valor.append(valor_carta.get(i[0]))
		lista_suit.append(i[1])


	return(sorted(lista_valor), lista_suit)

def Royal_Flush(mano):
	valores = separador(mano)
	if sorted(valores[0]) == [9,10,11,12,13]:
		for i in ('H','S','C','D'):
			if valores[1].count(i) == 5:
				return True
	else:
		return False

	return False

def Straight_Flush(mano):
	valores = separador(mano)
	for i in range(4):
		if (valores[0][i + 1] - valores[0][i]) != 1:
			return False
	for i in ('H','S','C','D'):
		if valores[1].count(i) == 5:
			return True

	return False

def Four_of_a_Kind(mano):
	valores = separador(mano)
	for i in range(14):
		if valores[0].count(i) == 4:
			return True

	return False

def Full_House(mano):
	valores = separador(mano)
	for i in range(14):
		if valores[0].count(i) == 3:
			for j in range(14):
				if valores[0].count(j) == 2:
					return(True, i)

	return(False, 0)

def Flush(mano):
	valores = separador(mano)
	for i in ('H','S','C','D'):
		if valores[1].count(i) == 5:
			return True

	return False

def Straight(mano):
	valores = separador(mano)
	for i in range(4):
		if (valores[0][i + 1] - valores[0][i]) != 1:
			return False

	return True

def Three_of_a_Kind(mano):
	valores = separador(mano)
	for i in range(14):
		if valores[0].count(i) == 3:
			return(True, i)

	return(False, 0)

def Two_Pairs(mano):
	valores = separador(mano)
	for i in range(14):
		if valores[0].count(i) == 2:
			(valores[0]).remove(i)
			for j in range(14):
				if valores[0].count(j) == 2:
					return True

	return False

def One_Pair(mano):
	valores = separador(mano)
	for i in range(14):
		if valores[0].count(i) == 2:
			return(True, i)

	return(False, 0)

def Crupier(mano):
	if Royal_Flush(mano):
		return(10, 0)
	elif Straight_Flush(mano):
		return(9, 0)
	elif Four_of_a_Kind(mano):
		return(8, 0)
	elif Full_House(mano)[0]:
		return(7, Full_House(mano)[1])
	elif Flush(mano):
		return(6, 0)
	elif Straight(mano):
		return(5, 0)
	elif Three_of_a_Kind(mano)[0]:
		return(4, Three_of_a_Kind(mano)[1])
	elif Two_Pairs(mano):
		return(3, 0)
	elif One_Pair(mano)[0]:
		return(2,One_Pair(mano)[1])
	else:#High Card
		valores = separador(mano)
		return(1, max(valores[0]))

def draw_One_Pair(mano1, mano2): #draw_High_Card, Straight y Flush
	valores1 = separador(mano1)[0]
	valores2 = separador(mano2)[0]
	while True:
		c1 = max(valores1)
		c2 = max(valores2)
		valores1.remove(c1)
		valores2.remove(c2)
		if c1 > c2:
			return(1)
		elif c1 == c2:
			pass
		else:
			return(2)

def draw_Full_House(c1, c2):
	if c1 > c2:
		return(1)
	else:
		return(2)

def mesa(m1, m2):
	mano1 = Crupier(m1)
	mano2 = Crupier(m2)

	if mano1[0] > mano2[0]:
		return(1)
	elif mano1[0] < mano2[0]:
		return(2)
	else:
		if mano1[0] in (1, 5, 6):
			return(draw_One_Pair(m1, m2))
		elif mano1[0] == 2:
			if mano1[1] > mano2[1]:
				return(1)
			elif mano1[1] < mano2[1]:
				return(2)
			else:
				return(draw_One_Pair(m1, m2))
		elif mano1[0] in (7, 4):
			if mano1[1] > mano2[1]:
				return(1)
			else:
				return(2)

def main():
	entrada = open('p054_poker.txt', 'r')
	#salida = open('output.txt', 'w')

	T = int(entrada.readline())
	
	total = 0
	for i in range(T):
		xy = entrada.readline()
		x = xy[0:14]
		y = xy[15:29]
		
		#salida.write("Caso #{}: Jugador {}\n".format(i+1, mesa(x, y)))
		if mesa(x, y) == 1:
			total += 1

	print(total)	
	
	entrada.close()
	#salida.close()

main()

#376
#[Finished in 0.2s]