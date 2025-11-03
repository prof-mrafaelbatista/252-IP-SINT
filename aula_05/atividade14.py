moeda1 = int(input('Digite a qtd de R$ 1,00 '))
moeda2 = int(input('Digite a qtd de R$ 0,50 '))
moeda3 = int(input('Digite a qtd de R$ 0,25 '))

valor1 = moeda1 * 1
valor2 = moeda2 * 0.50
valor3 = moeda3 * 0.25

valor_total = valor1 + valor2 + valor3

print(f'O total em reais é de R$ {valor_total}')