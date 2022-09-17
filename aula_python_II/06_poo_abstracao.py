import time

class DuracaoBatalha:
    def __init__(self, ataque, pokemon):
        self.ataque = ataque
        self.pokemon = pokemon
        
    def cooldownAtaque(self):
        inicio = time.time()
        
        msg = f'{self.pokemon}! {self.ataque}!'
        msg += f'O cooldown é de {time.time()}'
        
        time.sleep(3)
        
        msg += f' Sua defesa irá expirar em {time.time()}'
        time.sleep(5)
        
        fim = time.time()
        calculo_tempo = fim - inicio
        return msg + f' O tempo de batalha foi:{calculo_tempo}'

charmander = DuracaoBatalha('Lança-Chamas', 'Charmander')
print(charmander.cooldownAtaque())