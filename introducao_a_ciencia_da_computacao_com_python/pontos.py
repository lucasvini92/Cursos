import math
x1 = int(input("Digite um número inteiro: "))
y1 = int(input("Digite um número inteiro: "))
x2 = int(input("Digite um número inteiro: "))
y2 = int(input("Digite um número inteiro: "))

distancia = math.sqrt((x1-x2)**2 + (y1-y2)**2)

if (distancia>=10):
    print("longe")
else:
    print("perto")