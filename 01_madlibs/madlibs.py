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
    sentencas = [
        [f"{nome_proprio} acordou de madrugada e foi até "
         f"a cozinha. Abriu a geladeira e viu {substantivo}. "
         f"Pegou, comeu e {verbo_passado}."],
        [f"{nome_proprio} foi à guerra. Encontrou um baú "]
    
    ]

    print("Bem-vind@ a...\n")
    print(text2art("Mad Libs!"))
    print("Digite um nome próprio:\n")
    nome_proprio = input().lower()
    print("Agora, digite um substantivo:\n")
    substantivo = input().lower()
    print("Por fim, digite um verbo conjugado no passado:\n")
    verbo_passado = input().lower()
    print("...")


mad_libs()