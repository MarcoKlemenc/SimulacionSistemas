from random import randint


class GeneradorPuertasSesgado:

    puertas = None

    def __init__(self):
        self.puertas = ['CABRA', 'CABRA', 'CABRA']

    def generar_coche(self, posicion_coche=False):
        self.puertas[posicion_coche or randint(0, 2)] = 'COCHE'
        return self.puertas

    """
    Casos:
    *Seleccion = 1
        -Puerta ganadora = 1 --> Puerta mostrada = 3
        -Puerta ganadora = 2 --> Puerta mostrada = 3
        -Puerta ganadora = 3 --> Puerta mostrada = 2
    *Seleccion = 2
        -Puerta ganadora = 1 --> Puerta mostrada = 3
        -Puerta ganadora = 2 --> Puerta mostrada = 3
        -Puerta ganadora = 3 --> Puerta mostrada = 1
    *Seleccion = 3
        -Puerta ganadora = 1 --> Puerta mostrada = 2
        -Puerta ganadora = 2 --> Puerta mostrada = 1
        -Puerta ganadora = 3 --> Puerta mostrada = 1
    """
    def mostrar_puerta(self, eleccion):
        puerta_ganadora = self.get_puerta_ganadora()
        puerta_a_mostrar = -1

        if(eleccion == 0):
            if(puerta_ganadora == 0):
                puerta_a_mostrar = 2
            elif(puerta_ganadora == 1):
                puerta_a_mostrar = 2
            elif(puerta_ganadora == 2):
                puerta_a_mostrar = 1

        if (eleccion == 1):
            if (puerta_ganadora == 0):
                puerta_a_mostrar = 2
            elif (puerta_ganadora == 1):
                puerta_a_mostrar = 2
            elif (puerta_ganadora == 2):
                puerta_a_mostrar = 0

        if (eleccion == 2):
            if (puerta_ganadora == 0):
                puerta_a_mostrar = 1
            elif (puerta_ganadora == 1):
                puerta_a_mostrar = 0
            elif (puerta_ganadora == 2):
                puerta_a_mostrar = 0

        return puerta_a_mostrar

    def reiniciar_puertas(self):
        self.puertas = ['CABRA', 'CABRA', 'CABRA']

    def get_puerta_ganadora(self):
        posicion = -1
        for x in range(0, 3):
            if self.puertas[x] == 'COCHE':
                posicion = x
        return posicion