''' funcion collatz que recibe como parametro un numero entero, 
luego realiza el algoritmo que describe la conjetura de Collatz. Esta funcion 
hace uso de un contador "cont", se establece en el ciclo.'''
cont = 0
def collatz(n):
    global cont
    if n == 1:
        return(cont)
    elif n % 2 ==0:
        cont += 1
        return(collatz(n // 2))
    else:
        cont += 1
        return(collatz(3 * n + 1))


''' se declaran las variables M y num donde se guardaran el largo y el numero
que produce la cadena mas larga de collatz, respectivamente el ciclo valua los numeros 
de 1 a 1000000 en la funcion collatz(), al final se imprime el numero y el largo de la cadena'''

M = 0
num = 0
for i in range(1,1000000):
    cont = 1
    a = collatz(i)
    if a > M:
        M = a
        num = i

print(num)