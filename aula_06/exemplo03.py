import time
for i in range(3, 30, 3):
    print(f'O número agora é o {i}')
    time.sleep(2)

lista_b = ['Luiz H.',
          'Duda',
          'Mr. Fontanive',
          'Thimenguista',
          'Patrícia (Monitora)',
          'Aluna da minha esposa, Gabrielê'
          ]

for aluno in lista_b:
    print(f'Você é arretado(a) {aluno}.')
    time.sleep(2)