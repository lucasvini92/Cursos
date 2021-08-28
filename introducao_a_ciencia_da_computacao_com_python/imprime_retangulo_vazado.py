altura = int(input("digite a altura"))
largura = int(input("digite a largura"))
larguraAtual = 0
alturaAtual = 0
while larguraAtual < largura:
    larguraAtual = larguraAtual + 1
    while alturaAtual < altura:
        if larguraAtual == 1 or larguraAtual == largura or alturaAtual == 0 or alturaAtual == altura-1:
            print("#", end ="")
        else:
            print (end =" ")
        alturaAtual = alturaAtual + 1
    print()
    alturaAtual = 0
