valores = [int(input()) for x in range(4)]
lista = []
x,i,k = valores[0:3]
for x in range(valores[0]+1):
    for i in range(valores[0]+1):
        for k in range(valores[0]+1):
            lista.append([x,i,k])
lista = [l for l in lista if sum(l) != valores[-1]]
print(lista)