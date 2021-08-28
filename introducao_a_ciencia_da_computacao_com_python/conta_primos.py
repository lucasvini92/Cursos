def n_primos (n):
    while n < 2:
        if n < 2:
            print("Digite um número válido : ")
    cont = n
    primo = 0
    total = 0
    i = n
    while i > 1:
        while cont <= n and cont > 0:
            if i % cont == 0:
                primo = primo + 1
            print("primo=",primo,"i=",i,"cont=",cont)    
            if cont == 1 and primo == 2:
                total = total + 1
            cont = cont - 1    
        i = i - 1
        primo = 0
        cont = 0
    return total         
