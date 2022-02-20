class AnimalesAcuaticosDelfin(object):
    nombre = ""
    genero = ""
    edad = ""
    raza = ""
    color=""
    habitad=""
    temperatura=""
    alimentacion=""
    
    def __init__(self):
        pass 
    
    def metodos_acuaticosdelfin(self,comer,sonidoemitido,accion,velocidad,metodocaza,metododefensa,socializacion):
        self.comer=comer
        self.sonidoemitido=sonidoemitido
        self.accion=accion
        self.velocidad=velocidad
        self.metodocaza=metodocaza
        self.metododefensa=metododefensa
        self.socializacion=socializacion

    def comer(self, comidaacuaticosdelfin):
        comidaacuaticosdelfin=input("Ingrese Alimento: ")
        return comidaacuaticosdelfin

    def sonidoemitido(self, sonidoemitidoacuaticosdelfin):
        sonidoemitidoacuaticosdelfin=input("Sonido Emitido del Delfin: ")
        return sonidoemitidoacuaticosdelfin

    def accion(self, accionacuaticosdelfin):
        accionacuaticosdelfin=input("Accion del Delfin: ")
        return accionacuaticosdelfin

    def velocidad(self, velocidadacuaticosdelfin):
        accionacuaticosdelfin=input("Cual es la velocidad del Delfin: ")
        return velocidadacuaticosdelfin

    def metodocaza(self, metodocazaacuaticosdelfin):
        metodocazaacuaticosdelfin=input("Como caza el delfin: ")
        return metodocazaacuaticosdelfin

    def metododefensa(self, metododefensaacuaticosdelfin):
        metododefensaacuaticosdelfin=input("Como se defienden los delfines: ")
        return metododefensaacuaticosdelfin

    def socializacion(self, metododefensaacuaticosdelfin):
        socializacion=input("Que tan frecuente socializan los Delfines: ")
        return socializacion
