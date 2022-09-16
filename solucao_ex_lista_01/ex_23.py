import operator

diario_classe= {}

for i in range (4):
    nome = input("Digite o NOME do aluno: ")
    nota = int(input(f'NOTA do {nome} : '))
    
    diario_classe[nome] = nota
    
print(diario_classe)

nota_maxima = max(diario_classe.items(), key=operator.itemgetter(1))[0]
print(f'A maior nota foi do aluno(a) {nota_maxima}')

