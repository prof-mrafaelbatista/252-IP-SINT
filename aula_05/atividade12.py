ouro = input('Digite a quantidade de Ouro: ')
ferro = input('Digite a quantidade de Ferro: ')

ouro = float(ouro)
ferro = float(ferro)

proporcao_ferro = ferro / (ouro + ferro)

if proporcao_ferro >= 0.7:
    print(f'A proporção de Ferro na Liga é de: {proporcao_ferro}')
    print('Será possível criar a armadura de Pegasus')
else:
    print('Quantidade de ferro insuficiente')
    print(f'Proporção de Ferro é apenas: {proporcao_ferro}')