# Execício 19

venda = float(input('Informe o valor da venda: '))

if venda < 1000.00:
    print('Você não ganhará comissão')
elif venda >= 1000.00 and venda < 5000.00:
    comissao = venda * (10/100)
    print(f'Você ganhará comissão de {comissao}')
elif venda >= 5000.00 and venda < 10000.00:
    comissao = venda * (20/100)
    print(f'Sua comissão será de {comissao}')
elif venda >= 10000.00 and venda < 50000.00:
    comissao = venda * (25/100)
    print(f'Sua comissão será de {comissao}')
else:
    comissao = venda * (30/100)
    print(f'Sua comissão será de {comissao}')