## classe inicia por 'class' seguida do nome 
## iniciado por letra maiúscula

class Cachorro:
    # Podemos criar atributos de classe, esses atributos vão 
    # possuir o mesmo valor em toda instância que for criada
    # para a classe antes do construtor:
    raca = 'shih-tzu'
    
    # o método __init__() é o contrutor, ele define o
    # estado inicial do objeto, atribuindo valores
    # das propriedades do objeto. Ele que irá inicializar
    # cada nova instância da classe  
    def __init__(self, nome, idade):
        self.name = nome
        self.idade = idade
        
    def description(self):
        return f"{self.name} tem {self.idade} anos de idade"
    
    def emite_som(self, som):
        return f"A {self.name} faz {som}"
          
    # O 'self' deve vir primeiro, ele é usado para chamar 
    # atributos e métodos dentro da própria classe, 
    # representa a intância da classe.

cachorro1 = Cachorro('Roberval', 3).description()
cachorro2 = Cachorro('Luzinete', 1).emite_som('au au')
# Aqui criamos dois objetos e instanciamos a classe, assim temos
# dois cachorros shih-tzu com nome e idade diferentes.

print(cachorro1)
print(cachorro2)