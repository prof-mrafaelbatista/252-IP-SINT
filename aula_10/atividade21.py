from random import randint

vetor_a = []

for i in range(10):
    vetor_a.append(randint(1, 1000))

print('-' * 30)
print('Vetor A')
print(vetor_a)
print('-' * 30)

x = int(input('Digite o valor de X: '))

vetor_m = []

for j in range(len(vetor_a)):
    result = vetor_a[j] * x
    vetor_m.append(result)

print('-' * 30)
print('Vetor M')
print(vetor_m)
print('-' * 30)