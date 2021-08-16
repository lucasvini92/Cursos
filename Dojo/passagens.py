pos1 = False
pos2 = False
pos3 = False
pos4 = False
pos5 = False
pos6 = False
pos7 = False
pos8 = False
pos9 = False
pos10 = False
fullEconomyClass = False
fullFirstClass = False

def firstClass():
    global pos1
    global pos2
    global pos3
    global pos4
    global pos5
    global fullFirstClass
    preencheVaga = False
    while fullFirstClass == False:
        while preencheVaga == False:
            if pos1 == False:
                pos1 = True
                preencheVaga = True
                print("************Cartão de embarque ************")
                print("Você está na poltrona 1 da primeira classe")
                print("******************************************")
                print()
                main()
            else:
                if pos2 == False:
                    pos2 = True
                    preencheVaga = True
                    print("************Cartão de embarque ************")
                    print("Você está na poltrona 2 da primeira classe")
                    print("******************************************")
                    print()
                    main()
                else:
                    if pos3 == False:
                        pos3 = True
                        preencheVaga = True
                        print("************Cartão de embarque ************")
                        print("Você está na poltrona 3 da primeira classe")
                        print("******************************************")
                        print()
                        main()
                    else:
                        if pos4 == False:
                            pos4 = True
                            preencheVaga = True
                            print("************Cartão de embarque ************")
                            print("Você está na poltrona 4 da primeira classe")
                            print("******************************************")
                            print()
                            main()
                        else:
                            if pos5 == False:
                                pos5 = True
                                preencheVaga = True
                                print("************Cartão de embarque ************")
                                print("Você está na poltrona 5 da primeira classe")
                                print("******************************************")
                                print()
                                main()
                            else:
                                preencheVaga = True
                                fullFirstClass = True
              
    if fullFirstClass == True:
        print("A primeira classe está lotada!")
        mudarClasse = int(input("Deseja viajar na classe econômica? Digite 1 (Sim) ou Digite 2 (não)"))
        print()
        if mudarClasse == 1:
            economyClass()
        else:
            if mudarClasse == 2:
                print ("Next flight leaves in 3 hours")
                return
    
def economyClass():
    global pos6
    global pos7
    global pos8
    global pos9
    global pos10
    global fullEconomyClass
    preencheVaga = False
    while fullEconomyClass == False:
        while preencheVaga == False:
            if pos6 == False:
                pos6 = True
                preencheVaga = True
                print("************Cartão de embarque ************")
                print("Você está na poltrona 6 da classe econômica")
                print("******************************************")
                print()
                main()
            else:
                if pos7 == False:
                    pos7 = True
                    preencheVaga = True
                    print("************Cartão de embarque ************")
                    print("Você está na poltrona 7 da classe econômica")
                    print("******************************************")
                    print()
                    main()
                else:
                    if pos8 == False:
                        pos8 = True
                        preencheVaga = True
                        print("************Cartão de embarque ************")
                        print("Você está na poltrona 8 da classe econômica")
                        print("******************************************")
                        print()
                        main()
                    else:
                        if pos9 == False:
                            pos9 = True
                            preencheVaga = True
                            print("************Cartão de embarque ************")
                            print("Você está na poltrona 9 da classe econômica")
                            print("******************************************")
                            print()
                            main()
                        else:
                            if pos10 == False:
                                pos10 = True
                                preencheVaga = True
                                print("************Cartão de embarque ************")
                                print("Você está na poltrona 10 da classe econômica")
                                print("******************************************")
                                print()
                                main()
                            else:
                                preencheVaga = True
                                fullEconomyClass = True
              
    if fullEconomyClass == True:
        print("A primeira classe está lotada!")
        mudarClasse = int(input("Deseja viajar na primeira classe? Digite 1 (Sim) ou Digite 2 (não)"))
        print()
        if mudarClasse == 1:
            firstClass()
        else:
            if mudarClasse == 2:
                print ("Next flight leaves in 3 hours")
    
def main ():
    escolha = False
    while escolha == False:
        if (fullEconomyClass == True) and (fullFirstClass == True):
            return "Não existem mais voos disponíveis"
        print ("Please type 1 for First Class e Please type 2 for Economy.")
        print()
        option = int(input("Informe sua escolha  "))
        if option == 1:
            firstClass()
            escolha = True
        else:
            if option == 2:
                economyClass()
                escolha = True
            else:
                print()
                print("Favor inserir um valor válido")
                print()
                continue

main()
