#CONVERSOR DE NOTAS ESCOLARES

pontuacao = int(input("Digite a pontuação do aluno de 0 a 100: "))

def conversorNota(pontuacao):
   if pontuacao>= 90:
      return 'A'
   elif pontuacao >= 80:
      return 'B'
   elif pontuacao >= 70:
      return 'C'
   elif pontuacao >= 60:
      return 'D'
   else:
      return 'F'

def verificaNota(pontuacao):
   if 0 <= pontuacao <= 100:
      nota = conversorNota(pontuacao)
      print("A pontuação {} convertida para nota é igual a: {}".format(pontuacao, nota))
   else:
      print("Digite uma pontuação que esteja entre 0 e 100.")


conversorNota(pontuacao)
verificaNota(pontuacao)
     