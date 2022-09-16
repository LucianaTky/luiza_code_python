# Exercício 21

prefixo = int(input("Informe o prefixo desejado: "))
primeiro_sufixo = int(input("Informe o primeiro sufixo: "))
ultimo_sufixo = int(input("Informe o último sufixo: "))

while primeiro_sufixo <= ultimo_sufixo:
        print (f'{prefixo} - ' + str({primeiro_sufixo}).zfill(4))
        primeiro_sufixo = primeiro_sufixo + 1