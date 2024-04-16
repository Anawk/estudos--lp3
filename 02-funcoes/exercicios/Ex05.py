#VERIFICADOR DE PALÍNDROMOS

palavra = input("Escreva uma palavra ou frase: ").lower().strip()


def verificaPalavra(palavra):
    invertida = palavra[::-1]

    if palavra == invertida:
        print("O que você digitou é um PALÍNDROMO")
    else:
        print("O que você digitou não é um PALÍNDROMO")


verificaPalavra(palavra)