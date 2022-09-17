# decorator é um meto para envolver uma função, modificando o seu comportamento

# exemplo

def decorator(funcao):
    def wrapper():
        print ('Estou antes da execução da função passada como argumento')
        funcao()
        print ('Estou depois da execução passada como argumento')
        
    return wrapper

def outra_funcao():
    print ("Sou um belo argumento!")

funcao_decorada = decorator(outra_funcao)
funcao_decorada()