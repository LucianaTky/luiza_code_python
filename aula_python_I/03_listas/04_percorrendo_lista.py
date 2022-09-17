lista = [0, 5, 8, 10, 35, 15, 7, 4, 12, 22, 3, 2, 9, 1]
lista_numeros_maior_10 = []

for i in lista:
    if i > 10:
        lista_numeros_maior_10.append(i)        
print(f'Resultado da lista: {lista_numeros_maior_10}')

### Pode ser feito assim também 
lista_numeros_maior_10 = [i for i in lista if i > 10]
print(f'Resultado da lista: {lista_numeros_maior_10}')