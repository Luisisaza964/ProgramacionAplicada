class AnimalesTerrestre(object):
    nombre = ""
    genero = ""
    edad = ""
    raza = ""
    pelaje=""
    limpieza=""
    agresividad=""
    vacunas=""
    
    def __init__(self):
        pass 
    
    def metodos_terrestres(self,comer,sonidoemitido,accion,metododealimentacion,desplazamiento,metododedivercion):
        self.comer=comer
        self.sonidoemitido=sonidoemitido
        self.accion=accion
        self.metododealimentacion=metododealimentacion
        self.desplazamiento=desplazamiento
        self.metododedivercion=metododedivercion

    def comer(self, comidaterrestre):
        comidaterrestre=input("Ingrese Alimento del animal terrestre: ")
        return comidaterrestre

    def sonidoemitido(self, sonidoemitidoterrestre):
        sonidoemitidoterrestre=input("sonido emitido del animal terrestre: ")
        return sonidoemitidoterrestre

    def accion(self, accionterrestre):
        accionterrestre=input("accion del animal Terrestre: ")
        return accionterrestre

    def metododealimentacion(self, metododealimentacionterrestre):
        metododealimentacionterrestre=input("cual es el metodo de alimentarce: ")
        return metododealimentacionterrestre
        
    def desplazamiento(self, metododedespazamientoterrestre):
       metododedespazamientoterrestre=input("como se desplaza el animal terrestre")
       return metododedespazamientoterrestre

    def metododedivercion(self, metododedivercionterrestre):
        metododedivercionterrestre=input("como se divierte el animal terrestre: ")
        return metododedivercionterrestre
        

