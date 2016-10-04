'''Arquivo de entrada contem quatro linhas, sendo que as 3 primeiras são as coordenadas x,y,z do cubo
e a ultima é um numero o qual a soma das coordenadas não pode ser igual.
Imprima na tela a lista de coordenadas possiveis tal que sua soma não seja igual ao número da última linha
do arquivo de entrada.'''

entrada = [int(input()) for x in range(4)]
lista_coordenadas = []
x, y, z = entrada[0:3]
for x in range(entrada[0]+1):
    for y in range(entrada[1]+1):
        for z in range(entrada[2]+1):
            lista_coordenadas.append([x, y, z])
lista_coordenadas_final = [coordenadas for coordenadas in lista_coordenadas if sum(coordenadas) != entrada[-1]]
print(lista_coordenadas_final)
