#FUNÇÃO DE CONTAGEM DE PALAVRAS

def contaPalavras(frase):

    palavras = frase.split()

    cont = {}

    for palavra in palavras:
        if palavra in cont:
            cont[palavra] += 1
        else:
            cont[palavra] = 1

    return cont

while True:
    tex = input("Digite um texto, ou se quiser sair, digite 'sair':  ")
    if tex.lower() == 'sair':
        break
    resultado = contaPalavras(tex)
    print("Contagem das palavras:")
    for palavra, cont in resultado.items():
        print(f"{palavra}: {cont}")
