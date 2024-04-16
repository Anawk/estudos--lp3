#TABUADA DE UM NÚMERO

def tabuada ():
    num = int(input("Digite um número para gerar a tabuada: "))

    print("TABUADA DO {}".format(num))

    for i in range(1,11):
        print(f"{num} X {i} = {num*i}")

tabuada()        