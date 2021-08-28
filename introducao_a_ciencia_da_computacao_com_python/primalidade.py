num = int(input("Digite um número inteiro: "))
div = 1
cont = 0

while num>=div:
    if num % div == 0:
        cont = cont + 1
    div = div + 1 
if cont <=2:
    print("primo")
else:
    print("não primo")