import os, sys
ruta_x = __file__
print(ruta_x)
for j in range(2):
    ruta_x = os.path.dirname(ruta_x)
    print(ruta_x)
from b.c.z import f2z
def f1x():
    return 'f1x'
def f2x():
    f2z()
    return 'f2x'
x1 = 1
x2 = 2