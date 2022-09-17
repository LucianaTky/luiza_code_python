# performam como listas de estrutura imutável
tupla = (('MG', 'Minas Gerais'), ('SP', 'São Paulo'))

tupla = (('MG', 'Minas Gerais'), ('SP', 'São Paulo'), [0, 1, 2, 3])

print(f'Remove o ultimo elemento da lista da tupla e retorna: {tupla[2].pop()}')
print(f'Resultado da tupla com o objeto lista modificado: {tupla}')