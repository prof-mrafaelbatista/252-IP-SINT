from random import randint

matriz_10x10 = []

for a in range(10):
    lista_temp = []
    for b in range(10):
        lista_temp.append(randint(1, 10000))
    matriz_10x10.append(lista_temp)

print(matriz_10x10)


maior_valor = -1
posicao = ()

for i in range(len(matriz_10x10)):
    for j in range(len(matriz_10x10[i])):
        if maior_valor < matriz_10x10[i][j]:
            maior_valor = matriz_10x10[i][j]
            posicao = (i, j)

print(f'O maior valor é {maior_valor}')
print(f'A posição dele é {posicao}')