entrada = int(input())

verifica_p_i = entrada % 2

num_anterior_impar = entrada - verifica_p_i -1

num_seguinte_par = num_anterior_impar + 3

print( num_anterior_impar , num_seguinte_par)
