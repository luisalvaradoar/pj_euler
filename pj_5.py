n = 1

''' se calcula el d = mcm(2, 3, ..., 19), luego recorro los naturales en modulo d
cuando algun numero N = 0 mod d lo imprime y sale del ciclo
'''
while(True):
	if n % ( ( 2 ** 4 ) * ( 3 ** 2 ) * 5 * 7 * 11 * 13 * 17 * 19 ) == 0:
		print(n)
		break
	else:
		n += 1