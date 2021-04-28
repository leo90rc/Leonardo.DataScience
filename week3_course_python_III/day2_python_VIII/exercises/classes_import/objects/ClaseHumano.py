class Humano:
    def __init__(self, nombre, armadura, nivel, ataque, ojos=2, piernas=2, dientes=32, salud=30):

        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes
        self.salud = salud

    def atacar(self, orco):
        orco.salud = orco.salud - (self.ataque - orco.armadura)
        return orco.salud

    def no_vivo(self, salud):
        if self.salud <=0:
            return True
        else:
            return False

    def atributos_humano(self):
        print('Nombre:', str(self.nombre), '\nArmadura:', str(self.armadura), '\nNivel:', str(self.nivel), '\nAtaque:', str(self.ataque),
         '\nOjos:', str(self.ojos), '\nPiernas:', str(self.piernas), '\nDientes:', str(self.dientes), '\nSalud:', str(self.salud))

