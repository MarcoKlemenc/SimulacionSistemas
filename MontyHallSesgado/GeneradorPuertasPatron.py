from random import randint


class GeneradorPuertasPatron:

    puertas = None
    patron = "000001111122222"

    def __init__(self):
        self.puertas = ['CABRA', 'CABRA', 'CABRA']
        self.contador = 0

    def generar_coche(self):
        self.puertas[int(self.patron[self.contador])] = 'COCHE'
        self.contador += 1
        if self.contador == len(self.patron):
            self.contador = 0
        return self.puertas

    def mostrar_puerta(self, eleccion):
        puerta_a_mostrar = randint(0, 2)
        while self.puertas[puerta_a_mostrar] == 'COCHE' or puerta_a_mostrar == eleccion:
            puerta_a_mostrar = randint(0, 2)
        return puerta_a_mostrar

    def reiniciar_puertas(self):
        self.puertas = ['CABRA', 'CABRA', 'CABRA']

    def get_puerta_ganadora(self):
        for x in range(0, 3):
            if self.puertas[x] == 'COCHE':
                return x
        return -1
