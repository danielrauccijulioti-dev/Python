lista = [7, 9, 10, 3, 4, 5, 2, 6, 1, 8]

for i in range(len(lista)):
    for a in range(len(lista) - 1):
        if lista[a] > lista[a + 1]:
            lista[a], lista[a + 1] = lista[a + 1], lista[a]

print(lista)
