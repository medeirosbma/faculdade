valor_divida = int(input())

pgto_por_mes = int(input())

contador = 1

while valor_divida > 0:
       
    print(f'pagamento: {contador}')
    print(f'antes = {valor_divida}')
    
    valor_divida = valor_divida - pgto_por_mes 
    
    if valor_divida < 0:
        valor_divida = 0 
        
    print(f'depois = {valor_divida}')
    print('-----')
    contador = contador + 1
    
    


    
