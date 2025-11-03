vetor_a = [1, 2, 3, 4, 5]
vetor_b = [6, 7, 8, 9, 10]
vetor_n = []

if len(vetor_a) == len(vetor_b):
    for i in range(len(vetor_a)):
        result = vetor_a[i] + vetor_b[i]
        vetor_n.append(result)
else:
    print('Tamanho de vetores incompatíveis')

print(vetor_n)