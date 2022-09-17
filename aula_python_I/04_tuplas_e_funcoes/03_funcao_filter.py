# utilizamos para filtrar elementos da lista

#retorne apenas os números pares
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = filter(lambda x: x%2 == 0, lista)
print(list(pares))