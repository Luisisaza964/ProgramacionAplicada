class AnimalesTerrestreMico(Terrestre):
    nombre = ""
    genero = ""
    edad = ""
    raza = ""
    limpieza = ""
    pelaje = ""
    agresividad = ""
    

    def __init__(self):
        pass 


    def metodos_terrestresmico(self,comer,metododedesplazamiento,sonidoemitido,accion,metododedivercion,metododealimentacion,metododedefensa):
        self.comer=comer
        self.metododedesplazamiento=metododedesplazamiento
        self.sonidoemitido=sonidoemitido
        self.accion=accion
        self.metododedivercion=metododedivercion
        self.metododealimentacion=metododealimentacion
        self.metododedefensa=metododedefensa


    def comer(self, comidaterrestremico):
        comidaterrestremico=input("Ingrese comida: ")
        return comidaterrestremico

    def metododedesplazamiento(self, desplazamientoterrestremico):
        desplazamientoterrestremico=input("ingresar metodo de despazamiento: ")
        return desplazamientoterrestremico

    def sonidoemitido(self, sonidoterrestremico):
        sonidoterrestremico=input("ingresar sonido: ")
        return sonidoterrestremico

    def accion(self, accionterrestremico):
        accionterrestremico=input("ingresar accion: ")
        return accionterrestremico

    def metododedivercion(self, juegoterrestremico):
        juegoterrestremico=input("ingresar juego:")
        return juegoterrestremico

    def metododealimentacion(self, alimentacionterrestremico):
        alimentacionterrestremico=input("ingresar alimentacion: ")

    def metododedefensa(self, defensaterrestremico):
        defensaterrestremico=input("ingresar metodo de defensa")
        return defensaterrestremico