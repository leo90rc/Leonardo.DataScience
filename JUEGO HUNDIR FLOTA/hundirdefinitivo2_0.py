import numpy as np
from random import randint, choice
from os import system
from copy import deepcopy as dc
from math import sqrt

if __name__ == '__main__':

    size = 10

    def isint(value):
      try:
        int(value)
        return True
      except ValueError:
        return False

    level = input('El juego puede ser fácil o difícil. ¿Qué reto quieres? \n Escribe 1 para fácil o 2 para difícil: ')

    while int(level) not in range(0, 3):
        level = input('¡Vaya! No es correcto. Introduce solo 1 para fácil o 2 para difícil: ')
    level = int(level) - 1

    def visualizar_tablero_agua():   # MUESTRA el tablero creado con los índices y columnas
        print('   1 2 3 4 5 6 7 8 9 10')
        for i in range(len(tablero_agua)):
            if i < 9:
                print(str(i+1)+ '  ' + ' '.join(tablero_agua[i]))
            elif i == 9:
                print(str(i+1)+ ' ' + ' '.join(tablero_agua[i]))

    def print_board(board):
        print('   1 2 3 4 5 6 7 8 9 10')
        i = 1
        for row in board:
            if i >= 10:
                print(str(i) + ' ' + ' '.join(row))
            else:
                print(str(i) + '  ' + ' '.join(row))
            i += 1


    def func_posicion_fila():   # Pregunta por la fila donde se coloca la cabecera del barco
        global posicion_fila
        posicion_fila = input('Ingrese la fila donde quiere colocar su barco: (1 - 10)')
        if int(posicion_fila) < 1 or int(posicion_fila) > 10:
            print('Esa fila no se encuentra en el tablero. Ingresa una fila entre 1 y 10')
            func_posicion_fila()
        else:
            return posicion_fila


    def func_posicion_columna():   # Pregunta por la columna donde se coloca la cabecera del barco
        global posicion_columna
        posicion_columna = input('Ingrese la columna donde quiere colocar su barco: (1 - 10)')
        if int(posicion_columna) < 1 or int(posicion_columna) > 10:
            print('Esa columna no se encuentra en el tablero. Ingresa una columna entre 1 y 10')
            func_posicion_columna()
        else:
            return posicion_columna


    def func_orientacion():   # Pregunta por la posición en la que se coloca el barco (horizontal o vertical)
        global orientacion
        orientacion = input('Ingrese la orientación de su barco: ("h" para horizontal - "v" para vertical)')
        if orientacion == 'h' or orientacion == 'v':
            return orientacion
        else:        
            print('Ingrese una orientación válida ("h" para horizontal - "v" para vertical)')
            func_orientacion()

    def ubicar_barcos():    # Pregunta qué barco quiero colocar, lo coloca y lo visualiza
        if len(barcos) > 0:
            print('\nBarcos disponibles:', barcos)
        while len(barcos) > 0:
            try:
                dimensiones = input('Qué barco desea posicionar? Ingrese la dimensión del barco a colocar: (2 a 5)')
                if int(dimensiones) in barcos:
                    func_posicion_fila()
                    func_posicion_columna()
                    func_orientacion()

                    if orientacion == 'h':
                        if np.all(tablero_agua[int(posicion_fila)-1, int(posicion_columna)-1:int(posicion_columna)+int(dimensiones)-1] != '#'):
                            if int(posicion_columna)+int(dimensiones)-1 > 10:
                                print('Te has salido del tablero!')
                                ubicar_barcos()
                            else:
                                tablero_agua[int(posicion_fila)-1, int(posicion_columna)-1:int(posicion_columna)+int(dimensiones)-1] = '#'
                                visualizar_tablero_agua()
                        else:
                            print('Ya hay un barco en ese sitio!')
                            ubicar_barcos()
                    elif orientacion == 'v':
                        if np.all(tablero_agua[int(posicion_fila)-1:int(posicion_fila)+int(dimensiones)-1, int(posicion_columna)-1] != '#'):
                            if int(posicion_fila)+int(dimensiones)-1 > 10:
                                print('Te has salido del tablero!')
                                ubicar_barcos()
                            else:
                                tablero_agua[int(posicion_fila)-1:int(posicion_fila)+int(dimensiones)-1, int(posicion_columna)-1] = '#'
                                visualizar_tablero_agua()
                        else:
                            print('Ya hay un barco en ese sitio!')
                            ubicar_barcos()
                else:
                    print('No dispones de barcos de dimensión ' + dimensiones)
                    ubicar_barcos()
                if len(barcos) > 0:
                    barcos.remove(int(dimensiones))
                    print('\nBarcos disponibles:', barcos)
            except Exception:
                print ('Ingresa un número válido')
        print('Ya has colocado todos los barcos!! A JUGAR !!')
        return tablero_agua

    def create_ships(board, ships):
        for ship in range(0, len(ships)):
            # genera coordenadas aleatorias y valida su posición
            valid = False
            while not valid:
                x = randint(1, 10 - ships[ship])-1
                y = randint(1, 10 - ships[ship])-1
                o = randint(0, 1)
                if o == 0:
                    ori = "v"
                else:
                    ori = "h"
                valid = validate(board,ships[ship],x,y,ori)
            #coloca el barco
            board = place_ship(board,ships[ship],ori,x,y)
        return board

    def place_ship(board, ship, ori, x, y):
        #coloca el barco basado en la orientación
        if ori == "v":
            for i in range(0, ship):
                board[x+i][y] = 1
        elif ori == "h":
            for i in range(ship):
                board[x][y+i] = 1
        return board

    def validate(board, ship, x, y, ori):
        if ori == "v" and x+ship > 10:
            return False
        elif ori == "h" and y+ship > 10:
            return False
        else:
            if ori == "v":
                for i in range(0, ship):
                    if board[x+i][y] != 0:
                        return False
            elif ori == "h":
                for i in range(0, ship):
                    if board[x][y+i] != 0:
                        return False
        return True

    def probability_hunt(board, ships, size, hit):
            prob = np.zeros((size, size))
            for ship in ships:
                verify = []
                verify.append(['~'] * ship)
                for row in range(0, len(board[0])):
                    for k in range(0, len(board[0]) - ship + 1):
                        if 'O' not in board[row][k:k + ship]:
                            prob[row, k:k + ship] += 1
                for col in range(0, len(board[0])):
                    column = []
                    for row in range(0, len(board[0])):
                        column.append(board[row][col])
                    for j in range(0, len(board[0]) - ship + 1):
                        if 'O' not in column[j:j + ship]:
                            prob[j:j + ship, col] += 1
            prob = np.divide(prob, np.amax(prob))
            for i in hit:
                prob[i[0], i[1]] = 0.1
            for row in range(0, len(board[0])):
                for i in range(0, len(board[0])):
                    if board[row][i] == 'X':
                        prob[row, i] = 0
            return prob

    def distance(hit, i):
        if hit.index(i) == (len(hit) - 1):
            dist = 0.1
            return dist
        else:
            horizontal = i[0] - hit[hit.index(i) + 1][0]
            vertical = i[1] - hit[hit.index(i) + 1][1]
            dist = sqrt(horizontal ** 2 + vertical ** 2)
            return dist

    def probability_attack(board, hit, ships, size):
        prob = np.zeros((size, size))
        for ship in ships:
            for row in range(0, len(board[0])):
                for i in hit:
                    if i[0] == row:
                        for k in range(i[1] - ship + 1, i[1] + 1):
                            if k >= 0:
                                if 'O' not in board[row][k:k + ship]:
                                        if (k + ship) < len(board[0]):
                                            prob[row, k:k + ship] += (1 - 0.1 * (1.5 * distance(hit, i) - hit.index(i)))
            for col in range(0, len(board[0])):
                column = []
                for i in hit:
                    if i[1] == col:
                        for k in range(i[0] - ship + 1, i[0] + 1):
                            if k >= 0:
                                for row in range(0, len(board[0])):
                                    column.append(board[row][col])
                                if 'O' not in column[k:k + ship]:
                                        if (k + ship) < len(board[0]):
                                            prob[k:k + ship, col] += (1 - 0.1 * (1.5 * distance(hit, i) - hit.index(i)))
        for i in hit:
            prob[i[0], i[1]] = 0
        for row in range(0, len(board[0])):
            for i in range(0, len(board[0])):
                if board[row][i] == 'X':
                    prob[row, i] = 0
        return prob

    def probability_mixed(board, hit, ships, size):
        prob = probability_attack(board, hit, ships, size)
        prob2 = probability_hunt(board, ships, size, hit)
        count = 0
        if len(hit) > 1 and hit[-2][0] == hit[-1][0] and sum(prob[hit[-1][0], :]) == 0:
            count = 1
        elif len(hit) > 1 and hit[-2][1] == hit[-1][1] and sum(prob[:, hit[-1][ 1]]) == 0:
            count = 1
        elif len(hit) > 2 and ((hit[-1][0] != hit[-2][0] and hit[-2][0] == hit[-3][0])\
        or hit[-1][1] != hit[-2][1] and hit[-2][1] == hit[-3][1]):
            count = 1
        elif len(hit) > 1 and hit[-2][0] == hit[-1][0]:
            prob[hit[-1][0], :] = np.prod([prob[hit[-1][0], :], 3])
        elif len(hit) > 1 and hit[-2][1] == hit[-1][1]:
            prob[:, hit[-1][1]] = np.prod([prob[:, hit[-1][1]], 3])
        elif np.amax(prob) > 0:
            prob = np.divide(prob, np.amax(prob))
        prob = prob * (1 - (1/2) * count)
        prob2 = prob2 * (1/2) * count
        prob3 = np.add(prob, prob2)
        return prob3

    def computer(level, status, ships):
        guess_row = []
        guess_col = []
        change = False
        if level == 0:
            guess_row = choice(range(0, size))
            guess_col = choice(range(0, size))
            while board[guess_row][guess_col] != '~':
                guess_row = choice(range(0, size))
                guess_col = choice(range(0, size))
            return [guess_row, guess_col]
        elif level == 1:
            if status == 1 and miss <= 3:
                prob = probability_mixed(board, hit, ships, size)
            elif status == 1 and miss > 3:
                change = True
                prob = probability_hunt(board, ships, size, hit)
            else:
                prob = probability_hunt(board, ships, size, hit)
            maximum = np.argwhere(prob == np.amax(prob))
            if np.amax(prob) != 0:
                index = choice(range(0, maximum.shape[0]))
                guess_row = maximum[index, 0]
                guess_col = maximum[index, 1]
            else:
                guess_row = choice(range(0, size))
                guess_col = choice(range(0, size))
                while board[guess_row][guess_col] != '~':
                    guess_row = choice(range(0, size))
                    guess_col = choice(range(0, size))

        return [guess_row, guess_col, change]

    def check_points(board, size):
        #loop para checkear las celdas del 2º tablero
        #si alguna celda no tiene '~', retorna False.
        for i in range(size):
            for j in range(size):
                if board[i][j] != 0:
                    return False
        return True



    board_ships = []
    board2_ships = []
    board2 = []
    board = []

    for x in range(size):
        board2.append(['~'] * size)

    for x in range(size):
        board2_ships.append([0] * size)

    ships = [5, 4, 4, 3, 3, 3, 2, 2, 2, 2]
    barcos = [2, 3]

    ships_comp = create_ships(board2_ships, ships)
    

    system('cls||clear')
    print('Hay 10 barcos en cada tablero. \n Uno de 5x1, dos de 4x1, tres de 3x1 y cuatro de 2x1 \n Tu meta es hundir la flota enemiga\'s antes de que él hunda la tuya')
    print('En cada tablero, "agua" se marca con "O" \n y "tocado" con "X".')
    input('Pulsa Enter para continuar...')
    tablero_agua = np.full((10,10), '~')
    visualizar_tablero_agua()
    ubicar_barcos()
    ships_human = ubicar_barcos()
    system('cls||clear')
    print('Hola, Soy The Computer y soy más inteligente que tú, humano. \n ¡Vamos a jugar!. \n Te permitiré empezar.')
    input('Pulsa Enter para continuar...')
    system('cls||clear')

    turn = 1
    status = 0
    miss = 0
    hit = []
    comp_guess = []
    points_human = 0
    points_comp = 0
    while turn > 0:
        system('cls||clear')
        print('Turno', turn)
        print('Tablero de The Computer:')
        print_board(board2)

        valid = False
        while not valid:
            guess_row = input("Elige fila: ")
            while not isint(guess_row):
                guess_row = input('Debería ser un entero... ')
            guess_row = int(guess_row) - 1
            guess_col = input("Elije columna: ")
            while not isint(guess_col):
                guess_col = input('Debería ser un entero... ')
            guess_col = int(guess_col) - 1
            complete = False

            if (guess_row < 0 or guess_row > (size - 1)) or (guess_col < 0 or guess_col > (size - 1)):
                print("Vaya... Eso ni siquiera está dentro del océano.")
            elif board2[guess_row][guess_col] != '~':
                print("Lo has adivinado...")
            else:
                    valid = True
            input('Pulsa Enter para continuar...')

        if ships_comp[guess_row][guess_col] == 1:
            print("¿Cómo osas, humano? ¡Le has dado a uno de mis barcos!")
            board2[guess_row][guess_col] = 'X'
            ships_comp[guess_row][guess_col] = 0 # probar si vale == '~'
            print_board(board2)
            input('Pulsa Enter para continuar...')
        else:
            print("Has fallado, ¡idiota!")
            board2[guess_row][guess_col] = 'O'
            print_board(board2)
            input('Pulsa Enter para continuar...')
                    
        print('The Computer observa tu tablero:')
        print_board(ships_human) # Debería mostrar nuestro tablero # Original: board

        comp_guess = computer(level, status, ships)

        if comp_guess[-1]:
            status = 0
            hit = []
            miss = 0

        guess_row2 = comp_guess[0]
        guess_col2 = comp_guess[1]
        complete = False

        if ships_human[guess_row2][guess_col2] == '#':
            print("¡Ajá! ¡Le di a uno de tus barcos!")
            board[guess_row2][guess_col2] = 'X'  # ships_human por board
            ships_human[guess_row2][guess_col2] = 0 # probar si vale == '~'
            hit.append([guess_row2, guess_col2])
            print_board(board) # Debería mostrar nuestro tablero
            status = 1
            miss = 0
            complete = True
        if not complete:
            print("The Computer falló. Simplemente mala suerte...")
            board[guess_row2][guess_col2] = 'O'
            print_board(board) # Debería mostrar nuestro tablero
            miss += 1
        points_human = check_points(ships_comp, size)
        points_comp = check_points(ships_human, size)
        if points_comp and not points_human:
            system('cls||clear')
            print('JAJAJAJAJA *ríe como un robot* ¡Gané! ¡Sabía que lo haría!')
            input('Pulsa Enter para continuar...')
            input('Pulsa Enter para salir...')
            break
        elif not points_comp and points_human:
            system('cls||clear')
            print('¡Felicidades humano! Ganaste por pura suerte....')
            input('Pulsa Enter para continuar...')
            input('Pulsa Enter para salir...')
            break
        elif points_comp and points_human:
            system('cls||clear')
            print('¡Es un empate!')
            input('Pulsa Enter para continuar...')
            input('Pulsa Enter para salir...')
            break
        else:
            input('Pulsa Enter para continuar...')

        turn += 1

