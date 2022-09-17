from functools import reduce

lista = [100, 248.90, 88, 124.90]

def desconto(preco):
    return preco * (1 - 0.1)

# map()
lista_desconto = map(lambda x: desconto(x), lista)
print(list(lista_desconto))

# filter()
lista_maior_100 = filter(lambda x: x > 100, lista)
print(list(lista_maior_100))

# reduce()
lista_somatoria = reduce(lambda x, y:  x+y, lista)
print(lista_somatoria)