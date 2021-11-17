ano_inicio = int(input())
ano_final = int(input())

contador = 0

for ano in range(ano_inicio, ano_final + 1):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(ano)
        contador = contador + 1
              
print(f"bissextos: {contador}")