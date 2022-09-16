#Exercício 05

### a.Calcule a área do quadrado
lado = 2
area_quadrado = lado * lado

print(f'A área do quadrado será {area_quadrado}')

### b. Preço da mala
preco_mala = 120.00
desconto = 5/100
valor_final = preco_mala - (preco_mala*desconto)

print(f'O valor com desconto será R${valor_final}')

### c. Horas de viagem
velocidade_em_km = 100
distancia_km_hora = 200
horas_de_viagem = distancia_km_hora/velocidade_em_km

print(f'A viagem irá demorar {horas_de_viagem} horas')

### d. Total de pirulitos
pirulitos_joao = 2
pirulitos_maria = 3
pirulitos_sofia = 1
total_pirulitos = pirulitos_joao + pirulitos_maria + pirulitos_sofia
media_pirulitos = total_pirulitos/3

print(f'O total de pirulitos será : {total_pirulitos}')
print(f'a média de pirulitos será: {media_pirulitos}')

### e.Verificação da Idade
davi = 13
irma_davi = 7
eh_mais_velho = davi > irma_davi
print(eh_mais_velho)
