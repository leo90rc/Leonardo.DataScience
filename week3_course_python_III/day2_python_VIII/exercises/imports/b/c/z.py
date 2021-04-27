import os, sys
print(__file__)
ruta_z = __file__
for x in range(3):
    ruta_z = os.path.dirname(ruta_z)
    print(ruta_z)
print('---')
sys.path.append(ruta_z)
print(sys.path)
print('--------')
from a.x import f1x, f2x, x1, x2
from b.y import f1y
def f1z():
    f1y()
    return 'f1z'
def f2z():
    f2x()
    return 'f2z'
z1 = 5
z2 = 6
print(x2)
