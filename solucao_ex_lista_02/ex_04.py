# Exercício 04

class Professor:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        
    def identificacao(self):
        funcionario = f'{self.nome} \n {self.idade}'
        return funcionario
    
    def __salario_priv(self):
        salario = f'Remuneração: {self.salario}'
        return salario
    
    def acesso_salario(self, nome):
        if self.nome == "Juriscleide":
            return self.__salario_priv()
        return 'Acesso Negado'
    
professor_matematica = Professor('Jonielson', '58', '6300')
acesso_1 = professor_matematica.acesso_salario(professor_matematica)
print(acesso_1)

professor_literatura = Professor('Juriscleide', '32', '5600')
acesso_2 = professor_literatura.acesso_salario(professor_literatura)
print(acesso_2)            