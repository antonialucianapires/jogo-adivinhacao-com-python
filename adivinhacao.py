import random


def jogar():
    print("##################################")
    print("Bem vinde ao jogo de Adivinhação! 🚀")
    print("##################################")

    numero_secreto = round(random.randrange(1, 101))
    total_tentativas = 0
    pontos = 1000

    print("Níveis de dificuldade do jogo ")
    print("(1) Fácil")
    print("(2) Médio")
    print("(2) Difícil")

    nivel = int(input("Escolha um  nível:"))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa: {} de {}".format(rodada, total_tentativas))
        chute_string = input("digite o seu número: ")
        print("Você deve digitar um número entre 1 e 100")
        print("Você digitou ", chute_string)
        chute = int(chute_string)

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100")
            continue

        if acertou:
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if chute_maior:
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif chute_menor:
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("##################################")
    print("Fim de jogo... Até a próxima!")
    print("##################################")
