bandas = [
    'Calcinha Preta',
    'Mel com Terra',
    'Noda de Caju',
    'A7'
]

banda_pes = input('Digite a banda preferida: ')

controle = 0
find = False

while controle < len(bandas):

    if bandas[controle].upper() == banda_pes.upper():
        find = True
        break

    controle += 1

if find:
    print('Achou')
else:
    print('Não achou')






    