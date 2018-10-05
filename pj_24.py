import itertools

permutaciones = list(itertools.permutations(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]))


def unir_permutacion(per):
	return( int( per[0] + per[1] + per[2] + per[3] + per[4] + per[5] + per[6] + per[7] + per[8] + per[9] ) )

permutaciones_unidas = []
for i in range( len( permutaciones ) ):
	permutaciones_unidas.append( unir_permutacion( permutaciones[i] ) )


print(permutaciones_unidas[999999])