cotacao_viccoin = float(1.0)
valor_real = float(cotacao_viccoin * 2.50)

doacoes = [float()] 

while -1.0  not in doacoes :
    
    doadores = float(input())
    doacoes.append(doadores)
 
   
if -1.0 in doacoes:
    doacoes.remove(-1.0)
    print(f'VC$ {sum(doacoes):.2f}')
    print(f'R$ {sum(doacoes)*valor_real:.2f}')
    
