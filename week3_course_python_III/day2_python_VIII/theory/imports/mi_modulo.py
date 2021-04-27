import sys, os

def suma_2(a, b):
    return a + b

def resta_2(a, b):
    return a - b

x = 2
# Cuando estamos en '.py' --> utilizamos '__file__'

# Cuando estamos en '.ipynb' --> utilizamos 'os.getcwd()'

# Ruta al fichero en el que estoy
print('--')
print(__file__)

import sys, os

# En '.py' las barras pueden aparecen hacia el otro lado.
print('-------------------------')
ruta = __file__
print(ruta)
print('###')
N = 5  # Mi carpeta raiz está 5 carpetas por encima de mi fichero actual
for i in range(N):
    ruta = os.path.dirname(ruta)
    print(ruta)
print("---------")
sys.path.append(ruta)
print(sys.path)
print('-')