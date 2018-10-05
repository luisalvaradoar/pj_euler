import math

# criba de eratostenes para probar si un numero 'n' es primo. Prueba a n mod k para k < sqrt(n)
def eratostenes( n ):
    if n == 1:
        return( 0 )
    else:
        for i in range( 2 , int( math.floor( math.sqrt( n ) ) ) + 1 ):
            if n % i == 0:
                return( 0 )
        return( n )

lista_primos = []

for n in range(10 ** 4):
    if eratostenes(n) != 0:
        lista_primos.append(n)


lista = []
for i in range(len(lista_primos)):
    suma_primos = lista_primos[i]
    for j in range(i + 1, len(lista_primos)):
        suma_primos += lista_primos[j]

        if suma_primos > 10 ** 6:
            break

        if eratostenes(suma_primos) != 0:
            lista.append((j - i + 1, i + 1, j + 1, suma_primos))

print(max(lista))

# 100,000   (543, 4, 546, 997651)

# (1587, 4, 1590, 9964597)