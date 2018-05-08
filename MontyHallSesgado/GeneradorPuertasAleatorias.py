from random import randint


class GeneradorPuertasAleatorias:

    puertas = None

    def __init__(self):
        self.puertas = ['CABRA', 'CABRA', 'CABRA']

    def generar(self):
        coche = randint(0, 2)
        self.puertas[coche] = 'COCHE'
        return self.puertas

    def mostrar_puerta(self, eleccion):
        puerta_a_mostrar = randint(0, 2)
        while(self.puertas[puerta_a_mostrar] == 'COCHE' or puerta_a_mostrar == eleccion):
            puerta_a_mostrar = randint(0, 2)
        return puerta_a_mostrar

    def reiniciar_puertas(self):
        self.puertas = ['CABRA', 'CABRA', 'CABRA']
