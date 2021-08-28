def soma_elementos(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma

lista = [2,3,4,5,6,2,4,5,1,2,4,5,6,1,2,4,5,3,2,2,2,2,3]

lista = soma_elementos(lista)
print (lista)        