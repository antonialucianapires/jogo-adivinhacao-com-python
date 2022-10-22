print("##################################")
print("Bem vinde ao jogo de Adivinhação! 🚀")
print("##################################")

numero_secreto = 42

chute = input("digite o seu número: ")

print("Você digitou ", chute)

if numero_secreto == int(chute):
    print("Você acertou!")
else:
    print("Você errou! O número correto é ", numero_secreto)

print("##################################")
print("Fim de jogo... Até a próxima!")
print("##################################")