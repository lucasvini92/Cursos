num = -1
lista = []

while num != 0:
    num = int(input("Digite um número: "))
    if num != 0:
        lista.append(num)
while lista != []:
    i = len(lista) -1
    print (lista[i])
    del lista[i]