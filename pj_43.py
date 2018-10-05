import itertools

permutaciones = list(itertools.permutations(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]))
#permutaciones = [("1", "4", "0", "6", "3", "5", "7", "2", "8", "9"),("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"),("2", "3", "1", "0", "5", "6", "7", "8", "9", "4")]


def unir_permutacion(per):
	return( int( per[0] + per[1] + per[2] + per[3] + per[4] + per[5] + per[6] + per[7] + per[8] + per[9] ) )


total = 0
for i in range(len(permutaciones)):
	n = int( permutaciones[i][1] + permutaciones[i][2] + permutaciones[i][3] )
	if n % 2 == 0:
		n = int( permutaciones[i][2] + permutaciones[i][3] + permutaciones[i][4] )
		if n % 3 == 0:
			n = int( permutaciones[i][3] + permutaciones[i][4] + permutaciones[i][5] )
			if n % 5 == 0:
				n = int( permutaciones[i][4] + permutaciones[i][5] + permutaciones[i][6] )
				if n % 7 == 0:
					n = int( permutaciones[i][5] + permutaciones[i][6] + permutaciones[i][7] )
					if n % 11 == 0:
						n = int( permutaciones[i][6] + permutaciones[i][7] + permutaciones[i][8] )
						if n % 13 == 0:
							n = int( permutaciones[i][7] + permutaciones[i][8] + permutaciones[i][9] )
							if n % 17 == 0:
								#print(unir_permutacion(permutaciones[i]))
								total += unir_permutacion(permutaciones[i])
							else:
								pass
						else:
							pass
					else:
						pass
				else:
					pass
			else: 
				pass
		else:
			pass
	else:
		pass

print(total)


 