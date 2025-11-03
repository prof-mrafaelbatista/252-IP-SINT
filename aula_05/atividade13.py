texto = 'Qual seu animal favorito (m) ou (r): '
animal = input(texto).lower()

if animal == 'm':
    print('Você gosta de doguinhos???')
elif animal == 'r':
    print('Seu bicinho é uma takaruga!!!')
else:
    print('Opção inválida!')