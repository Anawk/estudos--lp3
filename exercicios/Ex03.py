#CONTADOR DE VOGAIS E CONSOANTES

def contaVogal():
    frase = input("Escreva um frase qualquer:\n").strip().lower()
    vog = 0
    con = 0

    for letra in frase:
        if letra.isalpha():
          if letra in "aeiou":
            vog += 1
          else:  
            con += 1

    
    print("Tem {} vogais e {} consoantes na frase que você digitou".format(vog,con))

contaVogal()