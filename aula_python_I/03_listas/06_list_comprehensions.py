# melhor método
lista = [i for i in range(10) if i%2 == 0]
print(lista)

# método razoável
i = 0
lista = []
while i <= 10:
    if i% 2 == 0:
        lista.append(i)
i+=1       
print(lista)