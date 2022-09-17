# Exercício 03

class Pessoa:
    def __init__(self):
        pass
    
    def situacao_cadastral(self):
        return 'Não rastreado'
    
class PessoaJuridica(Pessoa):
    def __init__(self, cnpj):
        self.cnpj = cnpj
        super().__init__()
        
    def retorno(self):
        return f'CNPJ: {self.cnpj}'
    
cliente = PessoaJuridica('XXX.XXX.XXX-XX')
print(cliente.retorno())