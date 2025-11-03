# Quantos valores pares existem entre 1 e 100
# que sejam divisíveis por 5.

valor_inicial = 1
contador_valores = 0
while valor_inicial <= 100:

    if(valor_inicial % 5) == 0 and (valor_inicial % 2) == 0:
        print(valor_inicial)
        contador_valores += 1
    valor_inicial += 1

print(f'Total: {contador_valores}')