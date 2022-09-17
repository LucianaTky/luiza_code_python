# Parâmetros são nomes dados aos atributos de uma função,
# eles definem argumentos aceitos por uma função, podendo 
# ter ou não um valor padrão

# ex função que recebe dois parâmetros

def calcula_salario(valor, horas=220):
    return valor * horas
print(calcula_salario(35))