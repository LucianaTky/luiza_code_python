# Exercício 01

class Pessoa:
  def __init__(self, cpf, nome, idade, fumante):
    self.cpf = cpf
    self.nome = nome
    self.idade = idade
    self.fumante = fumante
 
  def tabagista(self):
      if self.fumante == "F":
        return (f"Fumante")   
      return (f"Não fumante")
  
  def saida(self):
    formato = f'CPF: {self.cpf} \nNome: {self.nome}'
    return formato
  
pessoa = Pessoa("XXX.XXX.XXX-XX", "Ana Maria", "78", "F")
fuma = pessoa.tabagista()

print(pessoa.saida())
print(f'É Fumante?: {fuma}')
