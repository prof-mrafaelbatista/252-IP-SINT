matriz = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [9, 10, 11]
    ]

for i in range(len(matriz)):
    for j in range(0, len(matriz[i]), 1):
        print(f'i={i} e j={j}')
        print(f'O valor de item da matriz é {matriz[i][j]}')