from random import randint


class GeneradorPuertas:

    puertas = None

    def __init__(self):
        self.puertas = ['CABRA', 'CABRA', 'CABRA']

    def generar_coche(self, posicion_coche=False):
        self.puertas[posicion_coche or randint(0, 2)] = 'COCHE'
        return self.puertas

    def mostrar_puerta(self, eleccion):
        puerta_a_mostrar = randint(0, 2)
        while(self.puertas[puerta_a_mostrar] == 'COCHE' or puerta_a_mostrar == eleccion):
            puerta_a_mostrar = randint(0, 2)
        return puerta_a_mostrar

    def reiniciar_puertas(self):
        self.puertas = ['CABRA', 'CABRA', 'CABRA']

    def get_puerta_ganadora(self):
        posicion = -1
        for x in range(0, 3):
            if self.puertas[x] == 'COCHE':
                posicion = x
        return posicion