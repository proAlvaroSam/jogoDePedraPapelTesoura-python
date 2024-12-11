import random

def pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    print("Escolha entre Pedra, Papel ou Tesoura para jogar.")

    while True:
        jogador = input("Digite sua escolha (pedra, papel, tesoura) ou 'sair' para encerrar: ").lower()

        if jogador == 'sair':
            print("Jogo encerrado. Obrigado por jogar!")
            break

        if jogador not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue

        computador = random.choice(opcoes)
        print(f"Você escolheu {jogador}, e o computador escolheu {computador}.")

        if jogador == computador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
             (jogador == "papel" and computador == "pedra") or \
             (jogador == "tesoura" and computador == "papel"):
            print("Você venceu!")
        else:
            print("Computador venceu!")

# Inicia o jogo
pedra_papel_tesoura()
