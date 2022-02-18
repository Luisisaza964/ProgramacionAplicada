##from Animales_Terrestres import Animales


class Animales(object):
    nombre = ""
    genero = ""
    edad = ""
    raza = ""
    comida=False

    def __init__(self):
        pass 
    

    def comer(self,comida):
        comida=True
        
    def nombre(self,_nombre,accion,sonidoemitido):
        self._nombre=_nombre
        self.accion=accion
        self.sonidoemitido=sonidoemitido

class Terrestres(Animales):
    nombre = ""
    genero = ""
    edad = ""
    raza = ""
    pelaje = ""
    limpieza = ""
    agresividad = ""
    vacunas = ""

    def __init__(self):
        pass

    
    def metodoterrestre(self,comer,accion,sonidoemitido,metodoalimentacion,desplazamiento,metododiversion):
        self.accion=accion
        self.sonidoemitido=sonidoemitido
        self.metodoalimentacion=metodoalimentacion
        self.desplazamiento=desplazamiento


    def metodoalimentacion(self, alimentoterrestre):
        alimentoterrestre=input("Ingrese Alimento: ")
        return alimentoterrestre

    def desplazamiento(self, movimientoterrestre):
        movimientoterrestre=input("Como se Muve el animal Terrestre: ")
        return movimientoterrestre

    def metododiversion(self, metododiversionterrestre):
        metododiversionterrestre=input("Con que juega el animal Terrestre: ")
        return metododiversionterrestre

