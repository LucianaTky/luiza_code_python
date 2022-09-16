# Exercício 13

lista_idade = []
numero_pessoas = 3

i = 1
while i <= numero_pessoas:
    idade = int(input(f' Digite sua idade {i}: ')) 
    lista_idade.append(idade)
    i += 1

media = sum(lista_idade) / numero_pessoas
print(f'A média de idade será: {media}')