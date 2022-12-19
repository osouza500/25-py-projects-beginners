from art import text2art

def continuar_sair():
    while True:
        print("Jogar outra vez? (S/n)\n")
        resposta = input().lower()
        if resposta == "s":
            mad_libs()
        elif resposta == "n":
            print("Até logo!")
            quit()
        else:
            print("Input inválido.")

def mad_libs():
    print(text2art("Mad Libs!"))
