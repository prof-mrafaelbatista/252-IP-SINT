try:
    print(50/2)
    lista_a = [1, 2]
    print(lista_a[3])

    # outros códigos

except ZeroDivisionError as error:
    print(f'Error: {error}')
    print('Tente novamente com outro número!')

except IndexError as error:
    print(f'Error: {error} | Este index não existe!')

except Exception as error:
    print(error)

print('Imprimir aqui!!')