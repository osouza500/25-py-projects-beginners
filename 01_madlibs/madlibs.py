from art import text2art
import random

def continuar_sair():
    while True:
        print("Jogar outra vez? (S/n)")
        resposta = input().lower()
        print("")
        if resposta == "s":
            mad_libs()
        elif resposta == "n":
            print("Até logo!")
            quit()
        else:
            print("Input inválido.")

def sentenca_aleatoria(nome, subst):
    sentenca = random.choice([
        f"{nome} comeu um(a) {subst} estragad@ e passou mal.",
        f"{nome} foi à guerra e atirou um(a) {subst} em um prussiano.",
        f"{nome} foi pres@ porque roubou um(a) {subst}.",
        f"{nome} atropelou um(a) {subst} e fugiu sem prestar socorro."
        f"{nome} tropeçou em um(a) {subst}, caiu e foi hospitalizad@.",
        f"{nome} foi ao pomar e colheu um(a) {subst}.",
        f"{nome} deu um(a) {subst} a um padre.",
        f"{nome} temperou o frango com {subst}.",
        f"{nome} escreveu um código usando um(a) {subst}.",
        f"{nome} trocou seu computador por um(a) {subst}.",
        f"{nome} assaltou um banco usando um(a) {subst}."
    ])
    return sentenca

def mad_libs():
    print("Bem-vind@ a...\n")
    print(text2art("Mad Libs!"))
    print("Digite um nome próprio:")
    nome_proprio = input().capitalize()
    print("")
    print("Agora, digite um substantivo no singular:")
    substantivo = input().lower()
    print("Gerando sentença...")
    print(sentenca_aleatoria(nome_proprio, substantivo))
    continuar_sair()

mad_libs()