print("##################################")
print("Bem vinde ao jogo de Adivinhação! 🚀")
print("##################################")

numero_secreto = 42
total_tentativas = 3
rodada = 1

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
        rodada = 4
        print("Você acertou!")
        break
    else:
        if chute_maior:
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif chute_menor:
            print("Você errou! O seu chute foi menor do que o número secreto.")

print("##################################")
print("Fim de jogo... Até a próxima!")
print("##################################")
