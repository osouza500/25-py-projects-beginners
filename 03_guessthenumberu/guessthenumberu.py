import time
import random

def printar_pausar(mensagem):
    time.sleep(.5)
    print(mensagem)


def continuar_sair():
    while True:
        printar_pausar("Jogar novamente? (S/n).")
        resposta = input().lower()
        if resposta == "s":
            adivinhe_numero()
        elif resposta == "n":
            printar_pausar("Até logo!")
            break
        else:
            printar_pausar("Input inválido.")

def input_usuario():
    while True:
        printar_pausar("Escolha um número de 1 a 10. "
                    "O computador tentará adivinhá-lo.")
        resposta = int(input())
        if resposta <= 0 or resposta > 10:
            printar_pausar("Input inválido.")
        ai_computador(resposta)


def ai_computador(numero):
    tentativas = []
    while True:
        jogada_computador = random.randint(1, 10)
        tentativas.append(jogada_computador)       
        printar_pausar(f"O número é {jogada_computador}?")
        if jogada_computador < numero:
            printar_pausar( "Acho que chutei baixo... "
                            "Vou tentar mais uma vez.")
        elif jogada_computador > numero:
            printar_pausar("Acho que chutei alto... "
                            "Vou tentar mais uma vez.")
        else:
            printar_pausar(f"Acertei! O número que você escolheu é {numero}!")
            continuar_sair()

input_usuario()