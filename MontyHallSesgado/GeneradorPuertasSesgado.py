from random import randint


class GeneradorPuertasSesgado:

    puertas = None

    def __init__(self):
        self.puertas = ['CABRA', 'CABRA', 'CABRA']

    def generar_coche(self):
        self.puertas[randint(0, 2)] = 'COCHE'
        return self.puertas

    """
    Casos:
    Seleccion   Ganadora    Mostrada
    1           1           3
    1           2           3
    1           3           2
    2           1           3
    2           2           3
    2           3           1
    3           1           2
    3           2           1
    3           3           1
    """
    def mostrar_puerta(self, eleccion):
        puerta_ganadora = self.get_puerta_ganadora()
        eleccion_y_ganadora = [eleccion, puerta_ganadora]
        eleccion_y_ganadora.sort()

        if eleccion_y_ganadora in [[1, 2], [2, 2]]:
            return 0
        elif eleccion_y_ganadora == [0, 2]:
            return 1
        elif eleccion_y_ganadora in [[0, 0], [0, 1], [1, 1]]:
            return 2

        return -1

    def reiniciar_puertas(self):
        self.puertas = ['CABRA', 'CABRA', 'CABRA']

    def get_puerta_ganadora(self):
        return self.puertas.index('COCHE')