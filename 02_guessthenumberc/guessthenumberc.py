import random
import time


def printar_pausar(mensagem):
    time.sleep(1)
    print(mensagem)

def continuar_sair():
    while True:
        printar_pausar("Jogar novamente? (S/n)")
        resposta = input().lower()
        if resposta == "s":
            adivinhe_numero()
        elif resposta == "n":
            printar_pausar("Até logo!")
            break
        else:
            printar_pausar("Input inválido.")