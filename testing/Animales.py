class Animales(object):
    nombre = ""
    genero = ""
    edad = ""
    raza = ""
    
    def metodos_animales(self,comer,accion,sonidoemitido):
        self.comer=comer
        self.accion=accion
        self.sonidoemitido=sonidoemitido


    def comer(self, comidaanimales):
        comidaAnimales=input("Ingrese Alimento del animal Animales: ")
        return comidaAnimales

    def sonidoemitido(self, sonidoemitidoAnimales):
        sonidoemitidoAnimales=input("sonido emitido del animal Animales: ")
        return sonidoemitidoAnimales

    def accion(self, accionAnimales):
        accionAnimales=input("accion del animal Animales: ")
        return accionAnimales


