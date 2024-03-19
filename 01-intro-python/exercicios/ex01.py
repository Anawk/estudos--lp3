
numero = input ('digite um número inteiro')
numero = int(numero)

ant = 0
sus = 0


def antecessor_num(numero):
    ant = numero -1
    print(ant)

def sucessor_num(numero):
    sus = numero +1
    print(sus)

antecessor_num(numero)
sucessor_num(numero)