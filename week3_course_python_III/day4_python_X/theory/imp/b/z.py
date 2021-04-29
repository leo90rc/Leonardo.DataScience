import os, sys
ruta = __file__
for i in range(2):
    ruta = os.path.dirname(ruta)
print("Ruta:", ruta)
sys.path.append(ruta)

#from a.x import x1
from y import y2
y2()