def computador_escolhe_jogada (n, m):
    global placarUsuario
    global computadorJogou
    pecasRestantes = n
    maxPecasParaRetirar = m
    global pecasRetiradas
    i = maxPecasParaRetirar
    passou = 0
    while i >= 0 and passou != 1: 
        if (pecasRestantes - i) % (maxPecasParaRetirar + 1) == 0:
            pecasRetiradas = i
            passou = 1
        else:
            i = i - 1
    if i == 0:
        pecasRetiradas = maxPecasParaRetirar
        
    computadorJogou = True
    if pecasRetiradas == 1:
        print("O computador tirou uma peça")
        print()
    else:
        print("O computador tirou",pecasRetiradas,"peças")
        print()    
    return pecasRetiradas

def usuario_escolhe_jogada (n , m):
    global placarComputador
    global usuarioJogou
    pecasRestantes = n
    maxPecasParaRetirar = m
    valido = 0
    while valido == 0:
        pecasRetiradas = int(input("Quantas peças você vai tirar?"))
        print()
        if (pecasRetiradas > maxPecasParaRetirar) or (pecasRetiradas < 1) or (pecasRetiradas > pecasRestantes):
            print ("Oops! Jogada inválida! Tente de novo.")
            continue
        else:
            print("Você tirou",pecasRetiradas,"peças")
            print()
            usuarioJogou = True
            valido = 1
            return pecasRetiradas
        
def partida():
    comecar = False
    global computadorJogou
    global usuarioJogou
    while comecar == False:
        try:
            n = int(input("Quantas peças?"))
            m = int(input("Limite de peças por jogada?"))
            comecar = True
        except:
            print ("Digite um número inteiro válido para N e para M")
            print()
            continue
        if n < m:
            print ("Computador começa!")
            print()
            pecasRetiradas = computador_escolhe_jogada(n, m)
        else:
            if n %(m+1) == 0:
                print ("Você começa!")
                print()
                pecasRetiradas = usuario_escolhe_jogada(n, m)
            else:
                if n == 1:
                    print ("Computador começa")
                    print()
                    pecasRetiradas = computador_escolhe_jogada(n, m)
                else:
                    if n == m:
                        print ("Computador começa!")
                        print()
                        pecasRetiradas = computador_escolhe_jogada(n, m)
                    else:
                        print ("Computador começa!")
                        print()
                        pecasRetiradas = computador_escolhe_jogada(n, m)
    jogadas(n, m, pecasRetiradas)

def jogadas(n, m, pecasRetiradas):
    global computadorJogou
    global usuarioJogou
    global placarComputador
    global placarUsuario
    n = n - pecasRetiradas    
    if n > 0:
        print("Agora restam",n,"peças no tabuleiro")
        print()
        if usuarioJogou == True:
            usuarioJogou = False
            pecasRetiradas = computador_escolhe_jogada(n, m)
        else:
            if computadorJogou == True:
                computadorJogou = False
                pecasRetiradas = usuario_escolhe_jogada(n, m)
    else:            
        if (n <= 0) and (usuarioJogou == True):
            print ("Fim do jogo! Você ganhou!")
            placarUsuario = placarUsuario + 1
            return
        else:
            if (n <= 0) and (computadorJogou == True):
                print ("Fim do jogo! O computador ganhou!")
                placarComputador = placarComputador + 1
                return
    return jogadas(n, m, pecasRetiradas)

       



def campeonato():
    vitoria = 1
    while vitoria <= 3:
        print ("**** Rodada",vitoria, "****")
        print()
        partida()
        vitoria = vitoria + 1
        if vitoria > 3:
            print("**** Final do campeonato! ****")
            print()
            print("Placar: Você ",placarUsuario,"X",placarComputador, "Computador")

def inicioJogo():
    entrarJogo = False
    while entrarJogo == False:
        opcaoJogo = int(input("Digite a opção escolhida: "))
        print()
        if opcaoJogo == 1:
            partida()
            entrarJogo = True
        else:
            if opcaoJogo == 2:
                campeonato()
                entrarJogo = True
            else:
                 continue
            

print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato 2")
print()
placarUsuario = 0
placarComputador= 0
computadorJogou = False
usuarioJogou = False
inicioJogo()
