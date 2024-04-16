palavra = "castanha"
numTentativas = 10

def mpalavraOculta(palavra, advinhadas):
    result = ""
    for letra in palavra:
        if letra.lower() in advinhadas or letra == " ":
            result += letra
        else:
            result += "_"
    return result

def jogo(palavra, numTentativas):
    advinhadas = set()

    while numTentativas > 0:
        print("A palavra é: ", mpalavraOculta(palavra, advinhadas))
        print("Tente advinhar!")
        letra = input("Digite uma letra: ").lower()

        if letra in advinhadas:
            numTentativas -= 1
            print("Você já escolheu essa letra, escolha outra\n")
            print("Agora você tem {} tentativas\n".format(numTentativas))
        else:
            advinhadas.add(letra)
            if letra not in palavra:
                numTentativas -= 1
                print("Não tem essa letra na palavra\n")
                print("Agora você tem {} tentativas\n".format(numTentativas))
            else:
                print("Você acertou uma letra!\n")
                numTentativas -= 1
                print("Agora você tem {} tentativas\n".format(numTentativas))

        if mpalavraOculta(palavra, advinhadas).replace(" ", "") == palavra.replace(" ", ""):
            print("----Você acertou a palavra! Parabéns!----")
            print("A palavra era: {}".format(palavra))
            return palavra

    print("----Você perdeu, a palavra era: {} ----".format(palavra))

jogo(palavra, numTentativas)


