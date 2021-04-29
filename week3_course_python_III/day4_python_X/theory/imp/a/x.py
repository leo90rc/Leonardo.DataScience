import os, sys

ruta = __file__
for i in range(2):
    ruta = os.path.dirname(ruta)
print("Ruta:", ruta)
sys.path.append(ruta)


def x1():
    
    print("x1")
    #y.y1()
    y1()



print("El name de x.py -->:", __name__)
if __name__ == "__main__":
    # Cuando importo un archivo de la forma que sea --> se interpreta TODO el archivo
    #import b.y as y
    from b.y import y1
    x1()