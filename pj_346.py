def repunitQ(N):
    for b in range(2, N - 1):
        n = N
        while (n % b) != n:
            if (n % b) == 1:
                n = int(n/b)
            else:
                break

            if n == 1:
                return(True)
    return(False)

def recurrencia(n, f, p):
    a = n
    lista = []
    for i in range(10):
        lista.append(a)
        a = f * a + p

    return(lista)

'''al parecer '''
suma = 1
lista = []
for i in range(400):
    if repunitQ(i):
        lista.append(i)


print(lista)
print(recurrencia(13, 3, 1))
print(recurrencia(15, 2, 1))
print(recurrencia(57, 3, 1))