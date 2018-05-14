from random import randint


class GeneradorPuertas:

    puertas = None

    def __init__(self):
        self.puertas = ['CABRA', 'CABRA', 'CABRA']

    def generar_aleatorio(self):
        posicion_coche = randint(0, 2)
        self.puertas[posicion_coche] = 'COCHE'
        return self.puertas


    def generar_en_la_puerta_3(self):
        posicion_coche = 2
        self.puertas[posicion_coche] = 'COCHE'
        return self.puertas

    def mostrar_puerta_aleatoria(self, eleccion):
        puerta_a_mostrar = randint(0, 2)
        while(self.puertas[puerta_a_mostrar] == 'COCHE' or puerta_a_mostrar == eleccion):
            puerta_a_mostrar = randint(0, 2)
        return puerta_a_mostrar

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
    def mostrar_puerta_con_sesgo(self, eleccion):
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