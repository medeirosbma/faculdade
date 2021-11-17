dia_compra = input()
prazo = int(input())

entrega = 'sera entregue'

indice =  int(0) 
contador = int(0)

dias_semana = ['domingo' , 'segunda' , 'terca' , 'quarta' , 'quinta', 'sexta', 'sabado']

if dia_compra in dias_semana:
    indice = dias_semana.index(dia_compra)

if prazo != 0:
    while contador < prazo:
        contador = contador + 1
        indice = indice + 1
        
        if (indice > 6):
            indice = 0
            
    print(entrega,dias_semana[indice])                         
                           
else:   print('chega hoje!')