import adivinhacao
import forca


def escolha_jogo():
    print("##################################")
    print("###### Escolha seu jogo! 🚀######")
    print("##################################")

    print("(1) Jogo de adivinhação")
    print("(2) Jogo da forca")

    jogo_escolhido = int(input("Qual você quer jogar? "))

    if jogo_escolhido == 1:
        adivinhacao.jogar()
    elif jogo_escolhido == 2:
        forca.jogar()
    else:
        print("A opção selecionada não condiz com os jogos da lista. Tente novamente.")


if __name__ == "__main__":
    escolha_jogo()
