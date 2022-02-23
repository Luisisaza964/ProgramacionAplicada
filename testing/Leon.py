class AnimalesTerrestreLeon(object):
    nombre = ""
    genero = ""
    edad = ""
    limpieza = ""
    agrecividad = ""
    

    def __init__(self):
        pass 


    def metodos_terrestreleon(self,comer,sonidoemitido,metododedivercion,metododealimentacion,accion,rapidez,metododecaza):
        self.comer=comer
        self.sonidoemitido=sonidoemitido
        self.metododedivercion=metododedivercion
        self.metododealimentacion=metododealimentacion
        self.accion=accion
        self.rapidez=rapidez
        self.metododecaza=metododecaza


    def comer(self, comidaterrestreleon):
        comidaterrestreleon=input("Ingrese comida: ")
        return comidaterrestreleon

    def sonidoemitido(self, sonidoterrestreleon):
        sonidoterrestreleon=input("ingresar sonido: ")
        return sonidoterrestreleon

    def metododedivercion(self, juegoterrestreleon):
        juegoterrestreleon=input("ingresar juego: ")
        return juegoterrestreleon

    def metododealimentacion(self, alimentacionterrestreleon):
        alimentacionterrestreleon=input("ingresar alimento: ")
        return alimentacionterrestreleon

    def accion(self, accionterrestreleon):
        accionterrestreleon=input("ingresar accion: ")
        return accionterrestreleon

    def rapidez(self, rapidezterrestreleon):
        rapidezterrestreleon=input("ingresar rapidez: ")
        return rapidezterrestreleon

    def metododecaza(self, metododecazaterrestreleon):
        metododecazaterrestreleon=input("ingresar metodo: ")
        return metododecazaterrestreleon

