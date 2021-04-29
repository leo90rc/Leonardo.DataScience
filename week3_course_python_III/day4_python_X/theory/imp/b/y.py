import os, sys
ruta = __file__
for i in range(2):
    ruta = os.path.dirname(ruta)
print("Ruta:", ruta)
sys.path.append(ruta)

import a.x as x

def y1():
    print("y1")
    
def y2():
    print("y2")
    x.x1()

# La variable '__name__' de cualquier archivo '.py' será '__main__' si es el archivo que se está ejecutando
if __name__ == "__main__":
    print("El name de y.py -->:", __name__)
    import a.x as x
    print("Está debajo de la condición __main__")
    #y1()
    y2()