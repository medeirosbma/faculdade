def numeros_primos ():
    inicio_primo= int(input())
    final_primo = int(input())
    contador_primos = 0
    
    while inicio_primo <= final_primo:
        if verifica_primo(inicio_primo) == True:
            print(inicio_primo)
            contador_primos += 1
        inicio_primo = inicio_primo + 1

    print (f'primos: {contador_primos}')
    
    
def verifica_primo(numero):
    contador = 1
    contar_divisor = 0
    
    while contador <= numero:
        if numero % contador == 0:
            contar_divisor +=1         
        contador = contador + 1
    
    if contar_divisor != 2:
        return False
    else:
        return True

      
numeros_primos()