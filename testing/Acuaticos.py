#from turtle import color


class AnimalesAcuaticos(metodos_animales):
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
    
    def metodos_acuaticos(self,comer,sonidoemitido,accion,velocidad,metodocaza,metododefensa):
        self.comer=comer
        self.sonidoemitido=sonidoemitido
        self.velocidad=velocidad
        self.velocidad=metodocaza
        self.velocidad=metododefensa

    def comer(self, comidaacuaticos):
        comidaacuaticos=input("Ingrese Alimento: ")
        return comidaacuaticos

    def sonidoemitido(self, sonidoemitidoacuaticos):
        sonidoemitidoacuaticos=input("Como se Muve el animal Acuatico: ")
        return sonidoemitidoacuaticos

    def accion(self, accionacuaticos):
        accionacuaticos=input("Con que juega el animal Acuatico: ")
        return accionacuaticos

    def velocidad(self, velocidadacuaticos):
        accionacuaticos=input("Con que juega el animal Acuatico: ")
        return velocidadacuaticos

    def metodocaza(self, metodocazaacuaticos):
        metodocazaacuaticos=input("Con que juega el animal Acuatico: ")
        return metodocazaacuaticos

    def metodocaza(self, metododefensaacuaticos):
        metododefensaacuaticos=input("Con que juega el animal Acuatico: ")
        return metododefensaacuaticos
    

    class AnimalesAcuaticosDelfin(metodos_acuaticos):
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

    class AnimalesAcuaticosTiburon(metodos_acuaticos):
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