def tablero():
    print(' _' * 8)
    contador = 0
    while contador <= 7:
        print(('|' + '_') * 8 + '|')
        contador += 1
