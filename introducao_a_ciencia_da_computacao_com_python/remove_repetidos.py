def remove_repetidos(lista):
    novaLista = []
    for item in lista:
        if item not in novaLista:
            novaLista.append(item)
    novaLista.sort()
    return novaLista

lista = [2,3,4,5,6,2,4,5,1,2,4,5,6,1,2,4,5,3,2,2,2,2,1,3]

lista = remove_repetidos(lista)
print (lista)