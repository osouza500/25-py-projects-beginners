import random
import time


def printar_pausar(mensagem):
    time.sleep(.5)
    print(mensagem)


def continuar_sair():
    while True:
        printar_pausar("Jogar novamente? (S/n)")
        resposta = input().lower()
        if resposta == "s":
            adivinhe_numero(10)
        elif resposta == "n":
            printar_pausar("Até logo!")
            break
        else:
            printar_pausar("Input inválido.")


def adivinhe_numero(numero):
    numero_maquina = random.randint(1, numero)
    numero_usuario = 0
    printar_pausar("Bem-vind@ a...\n")
    printar_pausar("Adivinhe o Número!!!\n")
    while numero_usuario != numero_maquina:
        try:
            printar_pausar(f"Digite um número entre 1 e {numero}")
            numero_usuario = int(input())
            print("")
            if numero_usuario > numero_maquina:
                printar_pausar("Chutou alto. Tente novamente.\n")
            elif numero_usuario < numero_maquina:
                printar_pausar("Chutou baixo. Tente novamente.\n")
        except ValueError:
            printar_pausar("Input inválido.\n")        
    printar_pausar(f"Acertou! o número escolhido pela "
                   f"máquina foi {numero_maquina}.\n")
    continuar_sair()

adivinhe_numero(10)