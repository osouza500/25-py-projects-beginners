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

def adivinhe_numero():
    printar_pausar("Digite um número de 1 a 10; "
                   "o computador tentará adivinhá-lo.")
    resposta = int(input())
    return resposta


def ai_computador(numero):
    