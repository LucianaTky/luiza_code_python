# Exercício 18

nota = int(input("Digite a nota: "))

if nota < 0 or nota > 100:
    print('Nota inválida')  
elif nota > 60:
    print('Aprovado!')
else:
    print('Reprovado!')
    