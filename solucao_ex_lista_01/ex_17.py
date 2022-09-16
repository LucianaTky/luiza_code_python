# Exercício 17

import math

a = float(input(f'Digite o valor de a:'))
b = float(input(f'Digite o valor de b:'))
c = float(input(f'Digite o valor de c:'))

delta = pow(b,2) - (4 * a * c)

if delta < 0:
    print("Não há raízes reais")
elif delta == 0:
    x = -b / (2*a)
    print(f'Temos duas raízes de mesmo valor: {x}')
else:
    x_1 = (-b + math.sqrt(delta)) / (2 * a)
    x_2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"""As raízes serão:
      x1: {x_1}
      x2': {x_2}""")


