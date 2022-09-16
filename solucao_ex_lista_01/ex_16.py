# Exercício 16

valor_emprestimo = float(input("Digite o valor desejado de empréstimo:"))
taxa = float(input("Digite o valor da taxa de juros ao mês:" ))
tempo = float(input("Digite o numero de meses que irei pagar o empréstimo: "))

taxa_porcento = taxa/100
valor_final = valor_emprestimo + (valor_emprestimo * taxa_porcento * tempo)

print(f'O valor final será de R${valor_final}')