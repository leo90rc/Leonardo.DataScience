import os, sys
print('-')
ruta_y = __file__
print(ruta_y)
print('--')
print('---')
for x in range(2):
    ruta_y = os.path.dirname(ruta_y)
    print(ruta_y)
print('----')
sys.path.append(ruta_y)
print(sys.path)
from a.x import f1x, f2x, x1, x2
def f1y():
    f1x()
    return 'f1y'
def f2y():
    f2x()
    return 'f2y'
y1 = 3
y2 = 4
print(x1)