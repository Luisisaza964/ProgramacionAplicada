class AnimalesAcuaticosTiburon(object):
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
    
    def metodos_acuaticostiburon(self,comer,sonidoemitido,accion,velocidad,metodocaza,metododefensa,socializacion):
        self.comer=comer
        self.sonidoemitido=sonidoemitido
        self.accion=accion
        self.velocidad=velocidad
        self.metodocaza=metodocaza
        self.metododefensa=metododefensa
        self.socializacion=socializacion

    def comer(self, comidaacuaticostiburon):
        comidaacuaticostiburon=input("Ingrese Alimento: ")
        return comidaacuaticostiburon

    def sonidoemitido(self, sonidoemitidoacuaticostiburon):
        sonidoemitidoacuaticostiburon=input("Sonido Emitido del Tiburon: ")
        return sonidoemitidoacuaticostiburon

    def accion(self, accionacuaticostiburon):
        accionacuaticostiburon=input("Accion del Tiburon: ")
        return accionacuaticostiburon

    def velocidad(self, velocidadacuaticostiburon):
        accionacuaticostiburon=input("Cual es la velocidad del Tiburon: ")
        return velocidadacuaticostiburon

    def metodocaza(self, metodocazaacuaticostiburon):
        metodocazaacuaticostiburon=input("Como caza el tiburon: ")
        return metodocazaacuaticostiburon

    def metododefensa(self, metododefensaacuaticostiburon):
        metododefensaacuaticostiburon=input("Como se defienden los tiburones: ")
        return metododefensaacuaticostiburon

    def socializacion(self, metododefensaacuaticostiburon):
        socializacion=input("Que tan frecuente socializan los Tiburones: ")
        return socializacion