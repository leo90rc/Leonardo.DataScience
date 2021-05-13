def _protegida():
    print("Soy protegida")
    
def __privada():
    print("Soy privada")
    
class Clase:
    def _protegida_dentro_clase(self):
        print("Soy protegida")
    
    def __privada_dentro_clase(self):
        print("Soy privada")