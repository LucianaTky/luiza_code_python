lista = [0, 5, 8, 10, 35, 15, 7, 4, 12, 22, 3, 2, 9, 1]
lista_append = []

# adicionamos '1' a cada elemento da lista
for i in lista:
    lista_append.append(i+1) 
print(f'Append: {lista_append}')
# saída -> Append: [1, 6, 9, 11, 36, 16, 8, 5, 13, 23, 4, 3, 10, 2]


### aumenta lista
lista_append.extend([0, 0, 0, 0,])
print(f'Extend: {lista_append}')
#saída -> Extend: [1, 6, 9, 11, 36, 16, 8, 5, 13, 23, 4, 3, 10, 2, 0, 0, 0, 0]


### insere valor no index desejado
lista_append.insert(8, 'meio')
print(f'Insert: {lista_append}')
#saída -> Insert: [1, 6, 9, 11, 36, 16, 8, 5, 'meio', 13, 23, 4, 3, 10, 2, 0, 0, 0, 0]

lista_append.remove('meio')
print(f'Remove: {lista_append}')
#saída ->Remove: [1, 6, 9, 11, 36, 16, 8, 5, 13, 23, 4, 3, 10, 2, 0, 0, 0, 0]


### remove item index 4
lista_append.pop(4)
print(f'Remone: {lista_append}')
#saída -> Remone: [1, 6, 9, 11, 16, 8, 5, 13, 23, 4, 3, 10, 2, 0, 0, 0, 0]


### localiza index por valor
print(f'Index: {lista_append.index(11)}')
#saída -> Index: 3


### organiza em ordem crescente
lista_append.sort()
print(f'Sort: {lista_append}')
# Sort: [0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 16, 23]


### inverte ordem lista
lista_append.reverse()
print(f'Reverse: {lista_append}')
# Reverse: [23, 16, 13, 11, 10, 9, 8, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0]

### faz copia da lista para uma nova lista
lista_new = lista_append.copy()
print(f'Copy: {lista_new}')