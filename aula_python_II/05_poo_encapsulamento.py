class BatalhaPokemon:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        
    def escolher_pokemon(self):
        msg_pokemon = ','.join(self.pokemon)
        return msg_pokemon
    
    def ataque(self):
        return 'Ataque!'
    
    def comando_ataque(self, poder):
        if poder == 'Choque do trovão':
            return self.ataque()
        else:
            return "Seu ataque falhou!"
        
pokebolas = BatalhaPokemon(['Pikachu', 'Chikorita', 'Squartle', 'Charmander'])
batalha = pokebolas.comando_ataque('Chicote de cipó!')
print(batalha)

batalha = pokebolas.comando_ataque('Choque do trovão')
print(batalha)