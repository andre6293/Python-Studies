# Jogo de NIM viciado
# Andre Pinto
# January 23, 2020
# Introdução à Ciência da Computação com Python Parte 1 @Coursera
import random as rd

numeros = {1: 'uma', 2: 'duas', 3: 'três'}
resta_restam = {1: "resta apenas", 2: 'restam', 3: 'restam'}
peca_pecas = {1: "peça", 2: 'peças', 3: 'peças'}


def computador_escolhe_jogada(n, m):
    # m = máximo de peças por jogada que podem ser removidas
    # n = número inicial de peças
    # SE
    # n = 3
    # m = 2
    print("Quantas peças?", str(n))
    print("Limite de peças por jogada?", str(m))
    if m + 1 < n:
        jogada_npc = m + 1
    else:
        jogada_npc = m
    return jogada_npc


def usuario_escolhe_jogada(n, m):
    print("Quantas peças?", str(n))
    print("Limite de peças por jogada?", str(m))
    jogada_pc = int(input("\nQuantas peças você vai tirar? "))
    return jogada_pc


def partida():
    n = 3
    m = 2
    while n != 0:
        if n % (m + 1):
            print("Voce começa!\n")
            j = usuario_escolhe_jogada(n, m)
            n -= j
            print("\nVocê tirou {} {}".format("uma", "peça"))
            print("Agora {} {} {} no tabuleiro.".format(resta_restam[n],
                                                        numeros[n],
                                                        peca_pecas[n]))
            j = computador_escolhe_jogada(n, m)
            n -= j
            print("\nO computador tirou {} {}.".format(numeros[j],
                                                       peca_pecas[j]))
        else:
            print("Computador começa!\n")
            j = computador_escolhe_jogada(n, m)
            n -= j
            print("\nO computador tirou {} {}".format(numeros[j],
                                                      peca_pecas[j]))
            print("Agora {} {} {} no tabuleiro.".format(resta_restam[n],
                                                        numeros[n],
                                                        peca_pecas[n]))
            j = usuario_escolhe_jogada(n, m)
            n -= j
            print("\nVocê tirou {} {}".format("uma", "peça"))
            print("Agora {} {} {} no tabuleiro.".format(resta_restam[n],
                                                        numeros[n],
                                                        peca_pecas[n]))
    print("O computador ganhou.")


def campeonato():
    # chamar partida() 3x
    print("**** Rodada 1 ****\n")
    partida()

    pass


def main():
    escolha = 0
    while escolha == 0:
        print("Bem-vindo ao jogo do NIM! Escolha: \n")
        escolha = int(input("1 - para jogar uma partida isolada" +
                            "\n" + "2 - para jogar um campeonato "))
        if escolha == 1:
            print("\nVocê escolheu uma partida isolada!\n")
            partida()
        elif escolha == 2:
            print("\nVocê escolheu um campeonato!\n")
            campeonato()
        else:
            escolha = 0

# if n % (m+1) == 0:
    # jogador começa
# else:
    # computador começa


main()
