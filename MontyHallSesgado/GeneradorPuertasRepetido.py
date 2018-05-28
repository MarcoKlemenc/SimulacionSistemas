from random import randint


class GeneradorPuertasRepetido:

    puertas = None

    def __init__(self):
        self.puertas = ['CABRA', 'CABRA', 'CABRA']

    def generar_coche(self):
        self.puertas[2] = 'COCHE'
        return self.puertas

    def mostrar_puerta(self, eleccion):
        if eleccion == 0:
            return 1
        elif eleccion == 1:
            return 0
        elif eleccion == 2:
            return randint(0, 1)

        return -1

    def reiniciar_puertas(self):
        self.puertas = ['CABRA', 'CABRA', 'CABRA']

    def get_puerta_ganadora(self):
        return self.puertas.index('COCHE')