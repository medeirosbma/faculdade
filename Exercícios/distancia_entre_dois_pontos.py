linha1 = input()
dados1 = linha1.split()

linha2 = input()
dados2 = linha2.split()

x1 = float(dados1[0])
x2 = float(dados2[0])

y1 = float(dados1[1])
y2 = float(dados2[1])

distancia = ((x2 - x1)**2) + ((y2 - y1)**2)

print(x1,x2,y1,y2)