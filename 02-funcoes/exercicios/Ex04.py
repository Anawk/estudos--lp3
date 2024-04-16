#SIMULADOR DE ELEIÇÕES

def eleicao():
    votocand1 = 0
    votocand2 = 0
    votocand3 = 0

    while True:
        print("ELEIÇÕES")
        print("Candidatos:\n")
        print("0-Gabriel Monteiro")
        print("1-Nicolas Ferreira")
        print("2-Lula")
        print("3-Parar votação")
        print("OBS: digite o numero que está antes do nome do candidato\n")

        voto = int(input("Digite o numero do respectivo candidato que você quer votar: "))

        if voto == 3:
            resultado(votocand1,votocand2, votocand3)
            break
        elif voto == 0:
            votocand1 += 1
        elif voto == 1:
            votocand2 += 1
        elif voto == 2:
            votocand3 += 1
        else:
            print("Opção errada, digite de novo")


def resultado(votocand1, votocand2, votocand3):
    vencedor = max(votocand1, votocand2, votocand3)

    print("RESULTADO:\n")
    print("Gabriel Monteiro: {} votos".format(votocand1))
    print("Nicolas Ferreira: {} votos".format(votocand2))
    print("Lula: {} votos\n".format(votocand3))

    print("VENCEDOR DA ELEIÇÃO")
    if vencedor == votocand1:
        print("Gabriel Monteiro é o vencedor!")
    elif vencedor == votocand2:
        print("Nicolas Ferreira é o vencedor!")
    else:
        print("Lula é o vencedor!")


eleicao()