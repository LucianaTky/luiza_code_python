# utiliza-se p/ realizar uma operação específica 
# nos itens da lista e transformá-los em outra coisa.

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_somada = map(lambda x: x+x, lista) # soma item com ele msm
print(list(lista_somada))
# saída -> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]