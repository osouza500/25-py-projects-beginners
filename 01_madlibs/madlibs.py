from art import text2art
import random

def continuar_sair():
    while True:
        print("Jogar outra vez? (S/n)")
        resposta = input().lower()
        if resposta == "s":
            mad_libs()
        elif resposta == "n":
            print("Até logo!")
            quit()
        else:
            print("Input inválido.")

def mad_libs():
    print("Bem-vind@ a...\n")
    print(text2art("Mad Libs!"))
    print("Digite um nome próprio:")
    nome_proprio = input()
    print("")
    print("Agora, digite um substantivo no singular:")
    substantivo = input().lower()
    print("Gerando sentença...")
    sentencas = [
        f"{nome_proprio} comeu um(a) {substantivo} estragad@, "
         "passou mal e desmaiou.",
        f"{nome_proprio} foi à guerra e atirou um(a) {substantivo} "
         "em um soldado prussiano.",
        f"{nome_proprio} foi pres@ porque roubou um(a) {substantivo}.",
        f"{nome_proprio} atropelou um(a) {substantivo} e fugiu sem "
         "prestar socorro.",
        f"Desastrad@, {nome_proprio} tropeçou em um(a) {substantivo}, "
         "caiu e foi hospitalizad@.",
        f"Sem motivo para tal, {nome_proprio} amarrou um(a) {substantivo} "
         "em uma árvore e ficou ali observando.",
        f"O cachorro de {nome_proprio} comeu um {substantivo} e enlouqueceu."
        f"O gato de {nome_proprio} adora arranhar {substantivo}."
    ]
    print(random.choice(sentencas))
    continuar_sair()


mad_libs()