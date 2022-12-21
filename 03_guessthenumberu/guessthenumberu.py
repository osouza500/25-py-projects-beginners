import time
import random


def printar_pausar(mensagem):
    time.sleep(1)
    print(mensagem)


def continuar_sair():
    while True:
        printar_pausar("Jogar novamente? (S/n).")
        resposta = input().lower()
        print("")
        if resposta == "s":
            input_usuario()
        elif resposta == "n":
            printar_pausar("Até logo!")
            quit()
        else:
            printar_pausar("Input inválido.\n")


def input_usuario():
    printar_pausar("Bem-vind@ a Adivinhe o Número!!!")
    while True:
            printar_pausar("Escolha um número de 1 a 10. "
                           "O computador tentará adivinhá-lo.")
            try: 
                resposta = int(input())
                print("")
                if resposta <= 0 or resposta > 10:
                    printar_pausar("Input inválido.\n")
                ai_computador(resposta)
            except ValueError:
                printar_pausar("Input inválido.\n")
        


def ai_computador(numero):
    tentativas = []
    while True:
        jogada_computador = random.randint(1, 10)
        if jogada_computador not in tentativas:
            printar_pausar(f"O número é {jogada_computador}?")
            if jogada_computador != numero:
                printar_pausar("Acho que não... Vou tentar "
                               "mais uma vez.\n")
            else:
                printar_pausar("Acertei! O número que você "
                              f"escolheu é {numero}!\n")
                continuar_sair()
            tentativas.append(jogada_computador)
        else:
            continue


if __name__ == "__main__":
    input_usuario()
