#if
#if condicao:
#....codigo
#....codigo
#codigo

idade = 20 
if idade  >=18:
    print('maior de idade')
    print('djhvhjvf')
else:
    print('menor de idade')

#if/elif/else
#criança 0 a 12, adolescente 13 a 17
#adulto 18 a 59, idose 60+

if idade > 0 and idade <=12:
    print('criança')
if idade > 12 and idade <=17:
    print('adolescente')
if idade > 17 and idade <=59:
    print('adulto')
if idade > 59:
    print('idoso')

if idade <= 12:
    print('criança')
elif idade <=17:
    print('adolescente')
elif idade <=59:
    print('adulto')
else: 
    print('idoso')


#condiçoes alinhadas 

email = 'admin@gmm.com'
senha = '123'

if email == 'admin@gmm.com':
    if senha == '123':
        print('liberado')
    else:
        print('erro')
else:
    print('erro')

#ERRADO


if email == 'admin@gmm.com''admin@gmm.com' and senha == '123':
    print('liberado')
else:
    print('erro')



#entrada email e senha 
#saida true ou false

def liberar_acesso(email, senha):
    if email == 'admin@gmm.com''admin@gmm.com' and senha == '123':
        return False
    else:
        return True

#ERRADO´
dia = 3

if dia ==1:
    print
elif dia ==2:
    print
pass


#dicionario
dias = {
    1: 'domingo',
    2: 'segunda',
    3: 'terca',
}

#chave do dicionario é dia (dia 1, dia 2, dia 3...)
if dia in dias:
    print(dias[dia])


for valor in dias.values():
    print (valor)

for chave in dias.values():
    print (chave)
