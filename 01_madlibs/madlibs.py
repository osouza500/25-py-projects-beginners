from art import text2art
import random
import time


def printar_pausar(mensagem):
    time.sleep(1)
    print(mensagem)


def continuar_sair():
    while True:
        printar_pausar("Jogar outra vez? (S/n)")
        resposta = input().lower()
        print("")
        if resposta == "s":
            mad_libs()
        elif resposta == "n":
            printar_pausar("Até logo!")
            quit()
        else:
            printar_pausar("Input inválido.")


def sentenca_aleatoria(nome, subst):
    sentenca = random.choice([
        f"{nome} comeu um(a) {subst} estragad@ e passou mal.",
        f"{nome} atirou um(a) {subst} em um prussiano.",
        f"{nome} foi pres@ ao roubar um(a) {subst}.",
        f"{nome} atropelou um(a) {subst}.",
        f"{nome} tropeçou em um(a) {subst}.",
        f"{nome} foi ao pomar colher um(a) {subst}.",
        f"{nome} deu um(a) {subst} a um padre.",
        f"{nome} temperou o frango com {subst}.",
        f"{nome} escreveu um código usando um(a) {subst}.",
        f"{nome} trocou seu computador por um(a) {subst}.",
        f"{nome} assaltou um banco usando um(a) {subst}."
    ])
    return sentenca


def mad_libs():
    print("Bem-vind@ a...\n")
    printar_pausar(text2art("Mad Libs!"))
    printar_pausar("Digite um nome próprio:")
    nome_proprio = input().capitalize()
    print("")
    printar_pausar("Pronto. Agora, digite um substantivo no singular:")
    substantivo = input().lower()
    print("")
    printar_pausar("Gerando sentença...")
    print("")
    printar_pausar(sentenca_aleatoria(nome_proprio, substantivo))
    print("")
    continuar_sair()


if __name__ == "__main__":
    mad_libs()
