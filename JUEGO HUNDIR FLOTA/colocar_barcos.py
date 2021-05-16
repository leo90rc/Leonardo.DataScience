import random
import numpy as np
from os import system

# DEFINIENDO FUNCIONES

def visualizar_tablero_agua():   # MUESTRA el tablero creado con los índices y columnas
    print('   1 2 3 4 5 6 7 8 9 10')
    for i in range(len(tablero_agua)):
        if i < 9:
            print(str(i+1)+ '  ' + ' '.join(tablero_agua[i]))
        elif i == 9:
            print(str(i+1)+ ' ' + ' '.join(tablero_agua[i]))


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

barcos = [5, 4, 4, 3, 3, 3, 2, 2, 2, 2]
tablero_agua = np.full((10,10), '~')
visualizar_tablero_agua()
ubicar_barcos()