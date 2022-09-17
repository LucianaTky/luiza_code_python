# Exercício 02

class Pessoa:
    def __init__(self, nome, sexo, idade):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
    
    def dados_pessoais(self):
        return f'Nome: {self.nome} \nSexo: {self.sexo} \nIdade: {self.idade} \nCPF: {self.cpf}'
    
class PessoaFisica:
    def __init__(self, nome, sexo, idade, cpf):
        self.cpf = cpf
        
        super().__init__()
        
    def score(self):
        if self.cpf == "Positivo":
            return f'Autorizado!'
        return f'Não Autorizado'

cliente = PessoaFisica('Anna Julia', 'Feminino', '32', 'Positivo')
cliente2 = PessoaFisica('Luciana', 'Feminino', '27', "Negativo")
print(cliente.score())
print(cliente2.score())