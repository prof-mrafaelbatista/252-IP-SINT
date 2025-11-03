msg = ''

while msg != 'seu nome':
    msg = input('Digite seu nome: ')
    with open('arquivo.txt', 'a', encoding='utf-8') as file:
        file.write(msg + '\n')