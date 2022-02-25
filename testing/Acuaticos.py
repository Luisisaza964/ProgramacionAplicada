#from turtle import color


class AnimalesAcuaticos(object):
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
    