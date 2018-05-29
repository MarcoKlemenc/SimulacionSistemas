from random import randint


class GeneradorPuertasAleatoria:

    puertas = None

    def __init__(self):
        self.puertas = ['CABRA', 'CABRA', 'CABRA']

    def generar_coche(self):
        self.puertas[randint(0, 2)] = 'COCHE'
        return self.puertas

    def mostrar_puerta(self, eleccion):
        puerta_a_mostrar = randint(0, 2)
        while(self.puertas[puerta_a_mostrar] == 'COCHE' or puerta_a_mostrar == eleccion):
            puerta_a_mostrar = randint(0, 2)
        return puerta_a_mostrar

    def reiniciar_puertas(self):
        self.puertas = ['CABRA', 'CABRA', 'CABRA']

    def get_puerta_ganadora(self):
        return self.puertas.index('COCHE')
