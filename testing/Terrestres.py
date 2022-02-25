class AnimalesTerrestre(metodos_animales):
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


    class AnimalesTerrestresLeon(metodos_terrestres):
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


    class AnimalesTerrestresMico(metodos_terrestres):
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