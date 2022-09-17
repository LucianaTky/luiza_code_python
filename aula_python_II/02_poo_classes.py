class PokemonCards:
    
    def __init__(self, nome, tipo, evolucao):
        self.nome = nome
        self.tipo = tipo
        self.evolucao = evolucao
        
    def ponto_de_combate(self):
        return f'O pokémon: {self.nome}, possui 80 pontos de ataque'
    
    def vencedor(self):
        return f'Você venceu a partida'
    
chikorita = PokemonCards('Chikorita', 'Planta', 'Bayleef')

pontos = chikorita.ponto_de_combate()
print(pontos)