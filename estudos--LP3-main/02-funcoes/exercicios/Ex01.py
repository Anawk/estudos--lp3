#JOGO DE ADIVINHAÇÃO

import random

numAleatorio = random.randint(1,100)
print("Advinhe um numero de 1 a 100")

def verificaNum(numAleatorio):

    while True: 
        escolha = int(input("Qual numero você escolhe?\n"))

        if escolha < numAleatorio:
             print("Palpite baixo, tente novamente\n")
        elif escolha > numAleatorio:
            print("Palpite alto, tente novamente\n")    
        else:
            print("Você escolheu o numero certo!\n")    
            break

verificaNum(numAleatorio)