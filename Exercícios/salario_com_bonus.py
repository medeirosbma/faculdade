nome_vendedor = str(input())

salario_fixo = float(input())

total_vendas = float(input())

comissao = float(0.15) 

salario_final = total_vendas * comissao + salario_fixo

print(f'TOTAL = R$ {salario_final:.2f}')