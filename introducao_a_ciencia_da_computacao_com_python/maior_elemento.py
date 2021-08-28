def maior_elemento(lista):
    maior = 0
    for item in lista:
        if item > maior:
            maior = item
    return maior

lista = [2,3,4,5,6,2,4,5,1,2,4,5,6,1,2,4,7,3,2,2,2,2,3]

lista = maior_elemento(lista)
print (lista)             