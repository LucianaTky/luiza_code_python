class Personalidade:
    def __init__(self):
        pass
    
    def personalidade_pokemon(self):
        return 'Indefinida'
    
class PersonalidadePikachu(Personalidade):
    def __init__(self, personalidade):
        self.personalidade = personalidade
        super().__init__()
        
    def caracteristica_personalidade(self):
        return f'A personalidade do Pikachu é: {self.personalidade}'
    
personalidade_pikachu = PersonalidadePikachu('calmo e alegre')
print(personalidade_pikachu.caracteristica_personalidade())