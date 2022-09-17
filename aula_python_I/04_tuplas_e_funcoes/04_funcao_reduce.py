# aplica uma operação em todos elementos da lista,
# reduzindo a apenas um elemento

from functools import reduce

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = reduce(lambda x, y: x+y, lista, 0)
print(soma)

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# depois.. lista = [3, 3, 4, 5, 6, 7, 8, 9]
# depois.. lista = [6, 4, 5, 6, 7, 8, 9]
# depois.. lista = [10, 5, 6, 7, 8, 9]
# depois.. lista = [15, 6, 7, 8, 9]
# depois.. lista = [21, 7, 8, 9 ]
# depois.. lista = [28, 8, 9]
# depois.. lista = [36, 9]
# depois.. lista = [45]