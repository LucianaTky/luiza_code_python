lista = []

i = 0
while i < 10:
    numero = int(input("Digite um numero: "))
    lista.append(numero)
    lista.sort()
    i += 1
print(f'Sua lista: {lista}')

def numero_ocorrencias():
    print("o numero de repetições para cada elemento será:")
    for n in set(lista):
        ocorrencias = lista.count(n)
        print(f'{n}:{ocorrencias}')
       
def eh_par(n):
        if n%2 == 0:
            return 'par, '
        else:
            return 'ímpar,'
    
def eh_primo():
    for b in set(lista): 
        variavel = eh_par(b)   
        if b > 1:
            for n in range(2, b):
              if b % n == 0:
                print(b, variavel, 'não é primo.')
                break
            else:
                print(b, variavel, 'é primo.')
                
        elif b == 0:
            print('é zero.')
        elif b == 1:
            print(b, variavel,'é primo.')
            
numero_ocorrencias()            
eh_primo()

