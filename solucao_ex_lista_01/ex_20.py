# Exercício 20

valor_inicial = float(input("Digite o valor da primeira parcela: "))
percentual = int(input("Digite o valor percentual de cada parcela: ")) / 100
quantidade_parcelas = int(input("Digite o numero de parcelas: "))


count = 1
while count < quantidade_parcelas:
    if count == 1 :
        valor_parcela = valor_inicial + (valor_inicial * percentual)
        print(f'Parcela {count}: {valor_parcela}')
    
    valor_parcela = valor_parcela + (valor_parcela * percentual)
    valor_parcela = valor_parcela
    count = count + 1
    print(f'Parcela {count}: {valor_parcela}')
 
