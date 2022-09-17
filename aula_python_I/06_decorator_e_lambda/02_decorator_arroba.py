# Podemos usar o @, que chamará a função da imagem anterior
# exemplo

import time

def calculo_tempo(funcao):
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()
        
        calculo = tempo_final - tempo_inicial
        
        print(f' A {funcao.__name__}, levou o total de {calculo} para ser executada')
        
        return wrapper
    
    @calculo_tempo
    def run():
        for n in range(1000):
            yield
        
    run()