# *args e *kwars é uma convenção. As palavras são utilizadas para passar
# uma lista de argumentos variável sem palavras chaves em forma de tupla
# a função não saberá quantos argumentos serão passados

## exemplo *args

def foo(*args):
    print(f'conteudo: {args}')
    for i in args:
        print(i)
        
    foo('Hello', 'Moças', 'LuizaCode')

# **kwargs = keyword arguments, ele permite passar um dicionário com inúmeras 
# chaves para a função

## exemplo **kwargs

def foo(**kwargs):
    print(f' O nome dele é: {kwargs.get("nome")} ')
    
foo(nome = 'Jhon',
    idade = '28',
    pais = 'Brasil')