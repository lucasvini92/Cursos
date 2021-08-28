largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
preencheLargura = ""
linhaCheia = 0

while largura > 0:
    preencheLargura = preencheLargura + "#"
    largura = largura - 1
while altura > 0:
    print(preencheLargura)    
    altura = altura - 1  