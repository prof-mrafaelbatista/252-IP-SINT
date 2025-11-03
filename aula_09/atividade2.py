from random import randint

vetor20 = []

for i in range(20):
    num = randint(1, 100)
    vetor20.append(num)

vl_max = 0
vl_min = 101

for i in range(20):

    if vetor20[i] < vl_min:
        vl_min = vetor20[i]

    if vetor20[i] > vl_max:
        vl_max = vetor20[i]

print(f'O valor max é {vl_max}')
print(f'O valor min é {vl_min}')