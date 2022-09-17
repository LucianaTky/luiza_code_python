class Pokemon:
    
    def __init__(self, nome, tipo, codigopokedex, evolucao):
        self.nome = nome
        self.tipo = tipo
        self.codigopokedex = codigopokedex
        self.evolucao = evolucao
        
    def buscar_nome(self):
        return f'O nome do Pokémon é: {self.nome}'
    
    def buscar_tipo(self):
        return f'Ele é do tipo: {self.tipo}'
    
    def buscar_codigo(self):
        return f'O códogo na Pokedéx é: {self.codigopokedex}'
    
    def buscar_evolucao(self):
        return f'A evolução deste pokémon é: {self.evolucao}'
    
class Pikachu(Pokemon):
    def __init__(self, nome, tipo, codigopokedex, evolucao, dono):
        self.dono = dono
        
        super().__init__(nome, tipo, codigopokedex, evolucao)
        
    def possui_mestre(self):
        if self.dono == "S":
            return f'Este pokémon possui um mestre'
        if self.dono == "N":
            return f'Este pokémon mão possui mestre'
        
        return f'Não sabemos'

pikachu = Pikachu('Pikachu', 'planta', '172', 'Raichu', 'S')
print(pikachu.possui_mestre())