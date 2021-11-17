entrada = input()

dados = entrada.split()

a = float(dados[0])
b = float(dados[1])
c = float(dados[2])
pi = float(3.14159)

calc_triangulo = (a * c) / 2
calc_circulo = pi * c ** 2
calc_trapezio = ((a + b) * c) /2
calc_quadrado = b ** 2
calc_retangulo = a * b

print(f'TRIANGULO: {calc_triangulo:.3f}')
print(f'CIRCULO: {calc_circulo:.3f}')
print(f'TRAPEZIO: {calc_trapezio:.3f}')
print(f'QUADRADO: {calc_quadrado:.3f}')
print(f'RETANGULO: {calc_retangulo:.3f}')