nota_trabalhos = float(input())
nota_prova = float(input())

media = (nota_trabalhos + nota_prova) / 2

if (media >=6):
    print('aprovado')
else:
    prova_sub = int(10)
    media_sub = (nota_trabalhos + prova_sub) / 2
    if (media_sub >= 6):
        print('talvez com a sub')
    else:
        print('reprovado')