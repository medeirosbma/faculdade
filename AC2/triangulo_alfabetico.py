alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

tamanho_triangulo = int(input())

indice = 0

contador = 1

while contador <= tamanho_triangulo:
    print(f"{alfabeto[indice]*contador}")
    contador = contador + 1
    indice = indice + 1