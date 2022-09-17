# Exercício 06 

from ex_05 import Quadrado

lado = float(input('Lado do quadrado:'))
q = Quadrado(lado)

area = q.area_quadrado()
perimetro = q.perimetro_quadrado()

print(f'A área do quadrado: {area}\nPerímetro: {perimetro} ')