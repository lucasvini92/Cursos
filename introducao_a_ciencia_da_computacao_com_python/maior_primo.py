def maior_primo(x):
    numPrimo = False
    while numPrimo == False:
        cont = 1
        primo = 0
        while x > cont:
            if x%cont ==0:
                primo = primo + 1
            cont = cont +1
        if primo <=2:
            numPrimo = True
            return x
        else:
            x=x-1