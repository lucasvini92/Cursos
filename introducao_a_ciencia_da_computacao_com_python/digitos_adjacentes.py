num = int(input("Digite um número inteiro: "))
resp = 0
while num >= 1:
    num1 = num%10
    aux = num//10
    num2 = aux%10
    num = num//10
    if num1 == num2:
        resp = 1
if resp == 1:
    print("sim")
else:
    print("não")