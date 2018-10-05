def mitad(lista):
    largo_medio = len(lista)//2
    m1 = lista[0:largo_medio]
    m2 = lista[largo_medio:largo_medio*2]
    return(m1, m2)

def riffle_shuffle(lista):
    lista_m = mitad(lista)
    lista1 = lista_m[0]
    lista2 = lista_m[1]
    lista_nueva = []
    for i in range(len(lista1)):
            lista_nueva.append(lista1[i])
            lista_nueva.append(lista2[i])
    
    return(lista_nueva)

def lista_largo_n(n):
    lista = []
    for i in range(n):
        lista.append(i)

    return(lista)

def S(lista):
    lista_nueva = lista
    cont = 0
    while(True):
        lista_nueva = riffle_shuffle(lista_nueva)
        cont += 1
        if lista_nueva == lista:
            break

    return(cont)


Sn = 60
suma = 0
for i in range(1983, 5000):
    n = 2*i
    lista = lista_largo_n(n)
    Si = S(lista)
    if Si == Sn:
        suma += n
        print(n, suma)

# 1964 36692
# 2926 35920
# 3966 45652
# 5776 72828