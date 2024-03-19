valor = float(input ('digite o valor da compra'))
desconto = 0
valfinal = 0
valdesconto = 0

def desconto(valor):
    if valor < 10:
        desconto = 0
        valdesconto = valor * desconto
        valfinal = valor - valdesconto
        print(valfinal)  
       

    elif 10 <= valor < 100:
        desconto = 0.05
        valdesconto = valor * desconto
        valfinal = valor - valdesconto
        print(valfinal)  
       
    elif 100<= valor <500:
        desconto = 0.10
        valdesconto = valor * desconto
        valfinal = valor - valdesconto  
        print(valfinal)  
         

    else: 
        desconto = 0.15    
        valdesconto = valor * desconto
        valfinal = valor - valdesconto 
        print(valfinal)  
       

    return valfinal

desconto(valor)
