from random import randint


class GeneradorSeleccion:

    cantidad_triunfos_puerta1_dado_puerta2 = None
    cantidad_derrotas_puerta1_dado_puerta2 = None
    cantidad_triunfos_puerta1_dado_puerta2_cambio = None
    cantidad_derrotas_puerta1_dado_puerta2_cambio = None
    probabilidad_triunfo_puerta1_dado_puerta2 = None
    probabilidad_triunfo_puerta1_dado_puerta2_cambio = None

    cantidad_triunfos_puerta1_dado_puerta3 = None
    cantidad_derrotas_puerta1_dado_puerta3 = None
    cantidad_triunfos_puerta1_dado_puerta3_cambio = None
    cantidad_derrotas_puerta1_dado_puerta3_cambio = None
    probabilidad_triunfo_puerta1_dado_puerta3 = None
    probabilidad_triunfo_puerta1_dado_puerta3_cambio = None

    cantidad_triunfos_puerta2_dado_puerta1 = None
    cantidad_derrotas_puerta2_dado_puerta1 = None
    cantidad_triunfos_puerta2_dado_puerta1_cambio = None
    cantidad_derrotas_puerta2_dado_puerta1_cambio = None
    probabilidad_triunfo_puerta2_dado_puerta1 = None
    probabilidad_triunfo_puerta2_dado_puerta1_cambio = None

    cantidad_triunfos_puerta2_dado_puerta3 = None
    cantidad_derrotas_puerta2_dado_puerta3 = None
    cantidad_triunfos_puerta2_dado_puerta3_cambio = None
    cantidad_derrotas_puerta2_dado_puerta3_cambio = None
    probabilidad_triunfo_puerta2_dado_puerta3 = None
    probabilidad_triunfo_puerta2_dado_puerta3_cambio = None

    cantidad_triunfos_puerta3_dado_puerta1 = None
    cantidad_derrotas_puerta3_dado_puerta1 = None
    cantidad_triunfos_puerta3_dado_puerta1_cambio = None
    cantidad_derrotas_puerta3_dado_puerta1_cambio = None
    probabilidad_triunfo_puerta3_dado_puerta1 = None
    probabilidad_triunfo_puerta3_dado_puerta1_cambio = None

    cantidad_triunfos_puerta3_dado_puerta2 = None
    cantidad_derrotas_puerta3_dado_puerta2 = None
    cantidad_triunfos_puerta3_dado_puerta2_cambio = None
    cantidad_derrotas_puerta3_dado_puerta2_cambio = None
    probabilidad_triunfo_puerta3_dado_puerta2 = None
    probabilidad_triunfo_puerta3_dado_puerta2_cambio = None

    #habria que crear un getter y setter para cada uno despues si anda se refactoriza y se agrega. Ahora lo resuelvo a lo rustico jaja
    def __init__(self):
        self.cantidad_triunfos_puerta1_dado_puerta2 = 0.0
        self.cantidad_derrotas_puerta1_dado_puerta2 = 0
        self.cantidad_triunfos_puerta1_dado_puerta2_cambio = 0.0
        self.cantidad_derrotas_puerta1_dado_puerta2_cambio = 0
        self.probabilidad_triunfo_puerta1_dado_puerta2 = 0.0
        self.probabilidad_triunfo_puerta1_dado_puerta2_cambio = 0.0

        self.cantidad_triunfos_puerta1_dado_puerta3 = 0.0
        self.cantidad_derrotas_puerta1_dado_puerta3 = 0
        self.cantidad_triunfos_puerta1_dado_puerta3_cambio = 0.0
        self.cantidad_derrotas_puerta1_dado_puerta3_cambio = 0
        self.probabilidad_triunfo_puerta1_dado_puerta3 = 0.0
        self.probabilidad_triunfo_puerta1_dado_puerta3_cambio = 0.0

        self.cantidad_triunfos_puerta2_dado_puerta1 = 0.0
        self.cantidad_derrotas_puerta2_dado_puerta1 = 0
        self.cantidad_triunfos_puerta2_dado_puerta1_cambio = 0.0
        self.cantidad_derrotas_puerta2_dado_puerta1_cambio = 0
        self.probabilidad_triunfo_puerta2_dado_puerta1 = 0.0
        self.probabilidad_triunfo_puerta2_dado_puerta1_cambio = 0.0

        self.cantidad_triunfos_puerta2_dado_puerta3 = 0.0
        self.cantidad_derrotas_puerta2_dado_puerta3 = 0
        self.cantidad_triunfos_puerta2_dado_puerta3_cambio = 0.0
        self.cantidad_derrotas_puerta2_dado_puerta3_cambio = 0
        self.probabilidad_triunfo_puerta2_dado_puerta3 = 0.0
        self.probabilidad_triunfo_puerta2_dado_puerta3_cambio = 0.0

        self.cantidad_triunfos_puerta3_dado_puerta1 = 0.0
        self.cantidad_derrotas_puerta3_dado_puerta1 = 0
        self.cantidad_triunfos_puerta3_dado_puerta1_cambio = 0.0
        self.cantidad_derrotas_puerta3_dado_puerta1_cambio = 0
        self.probabilidad_triunfo_puerta3_dado_puerta1 = 0.0
        self.probabilidad_triunfo_puerta3_dado_puerta1_cambio = 0.0

        self.cantidad_triunfos_puerta3_dado_puerta2 = 0.0
        self.cantidad_derrotas_puerta3_dado_puerta2 = 0
        self.cantidad_triunfos_puerta3_dado_puerta2_cambio = 0.0
        self.cantidad_derrotas_puerta3_dado_puerta2_cambio = 0
        self.probabilidad_triunfo_puerta3_dado_puerta2 = 0.0
        self.probabilidad_triunfo_puerta3_dado_puerta2_cambio = 0.0



    def generar_seleccion_aleatoria(self):
        return randint(0, 2)

    #habria que buscar un patron para esto. Va a ser una cosa fea de ifs. Despues lo hacemos
    def generar_seleccion_probabilistica(self, eleccion, puerta_mostrada):

        if(eleccion == 0):
            if(puerta_mostrada == 1):
                if(self.probabilidad_triunfo_puerta1_dado_puerta2 >= self.probabilidad_triunfo_puerta1_dado_puerta2_cambio):
                    return 0
                else:
                    return 2
            if (puerta_mostrada == 2):
                if (self.probabilidad_triunfo_puerta1_dado_puerta3 >= self.probabilidad_triunfo_puerta1_dado_puerta3_cambio):
                    return 0
                else:
                    return 1

        if (eleccion == 1):
            if (puerta_mostrada == 0):
                if (self.probabilidad_triunfo_puerta2_dado_puerta1 >= self.probabilidad_triunfo_puerta2_dado_puerta1_cambio):
                    return 1
                else:
                    return 2
            if (puerta_mostrada == 2):
                if (self.probabilidad_triunfo_puerta2_dado_puerta3 >= self.probabilidad_triunfo_puerta2_dado_puerta3_cambio):
                    return 1
                else:
                    return 0

        if (eleccion == 2):
            if (puerta_mostrada == 0):
                if (self.probabilidad_triunfo_puerta3_dado_puerta1 >= self.probabilidad_triunfo_puerta3_dado_puerta1_cambio):
                    return 2
                else:
                    return 1
            if (puerta_mostrada == 1):
                if (self.probabilidad_triunfo_puerta3_dado_puerta2 >= self.probabilidad_triunfo_puerta3_dado_puerta2_cambio):
                    return 2
                else:
                    return 0


    def computar_resultado(self, eleccion_inicial, eleccion_final, puerta_mostrada, resultado):
        if (eleccion_inicial == 0):
            if (puerta_mostrada == 1):
                if (eleccion_final == 0):
                    if(resultado == "triunfo"):
                        self.cantidad_triunfos_puerta1_dado_puerta2 += 1
                    else:
                        self.cantidad_derrotas_puerta1_dado_puerta2 += 1
                else:
                    if (resultado == "triunfo"):
                        self.cantidad_triunfos_puerta1_dado_puerta2_cambio += 1
                    else:
                        self.cantidad_derrotas_puerta1_dado_puerta2_cambio += 1
            if (puerta_mostrada == 2):
                if (eleccion_final == 0):
                    if(resultado == "triunfo"):
                        self.cantidad_triunfos_puerta1_dado_puerta3 += 1
                    else:
                        self.cantidad_derrotas_puerta1_dado_puerta3 += 1
                else:
                    if (resultado == "triunfo"):
                        self.cantidad_triunfos_puerta1_dado_puerta3_cambio += 1
                    else:
                        self.cantidad_derrotas_puerta1_dado_puerta3_cambio += 1

        if (eleccion_inicial == 1):
            if (puerta_mostrada == 0):
                if (eleccion_final == 1):
                    if(resultado == "triunfo"):
                        self.cantidad_triunfos_puerta2_dado_puerta1 += 1
                    else:
                        self.cantidad_derrotas_puerta2_dado_puerta1 += 1
                else:
                    if (resultado == "triunfo"):
                        self.cantidad_triunfos_puerta2_dado_puerta1_cambio += 1
                    else:
                        self.cantidad_derrotas_puerta2_dado_puerta1_cambio += 1
            if (puerta_mostrada == 2):
                if (eleccion_final == 1):
                    if(resultado == "triunfo"):
                        self.cantidad_triunfos_puerta2_dado_puerta3 += 1
                    else:
                        self.cantidad_derrotas_puerta2_dado_puerta3 += 1
                else:
                    if (resultado == "triunfo"):
                        self.cantidad_triunfos_puerta2_dado_puerta3_cambio += 1
                    else:
                        self.cantidad_derrotas_puerta2_dado_puerta3_cambio += 1

        if (eleccion_inicial == 2):
            if (puerta_mostrada == 0):
                if (eleccion_final == 2):
                    if(resultado == "triunfo"):
                        self.cantidad_triunfos_puerta3_dado_puerta1 += 1
                    else:
                        self.cantidad_derrotas_puerta3_dado_puerta1 += 1
                else:
                    if (resultado == "triunfo"):
                        self.cantidad_triunfos_puerta3_dado_puerta1_cambio += 1
                    else:
                        self.cantidad_derrotas_puerta3_dado_puerta1_cambio += 1
            if (puerta_mostrada == 1):
                if (eleccion_final == 2):
                    if(resultado == "triunfo"):
                        self.cantidad_triunfos_puerta3_dado_puerta2 += 1
                    else:
                        self.cantidad_derrotas_puerta3_dado_puerta2 += 1
                else:
                    if (resultado == "triunfo"):
                        self.cantidad_triunfos_puerta3_dado_puerta2_cambio += 1
                    else:
                        self.cantidad_derrotas_puerta3_dado_puerta2_cambio += 1

    def generar_probabilidades(self):
        if((self.cantidad_triunfos_puerta1_dado_puerta2 + self.cantidad_derrotas_puerta1_dado_puerta2) != 0):
            self.probabilidad_triunfo_puerta1_dado_puerta2 = self.cantidad_triunfos_puerta1_dado_puerta2 / (self.cantidad_triunfos_puerta1_dado_puerta2 + self.cantidad_derrotas_puerta1_dado_puerta2)
        if((self.cantidad_triunfos_puerta1_dado_puerta2_cambio + self.cantidad_derrotas_puerta1_dado_puerta2_cambio) != 0):
            self.probabilidad_triunfo_puerta1_dado_puerta2_cambio = self.cantidad_triunfos_puerta1_dado_puerta2_cambio / (self.cantidad_triunfos_puerta1_dado_puerta2_cambio + self.cantidad_derrotas_puerta1_dado_puerta2_cambio)

        if((self.cantidad_triunfos_puerta1_dado_puerta3 + self.cantidad_derrotas_puerta1_dado_puerta3) != 0):
            self.probabilidad_triunfo_puerta1_dado_puerta3 = self.cantidad_triunfos_puerta1_dado_puerta3 / (self.cantidad_triunfos_puerta1_dado_puerta3 + self.cantidad_derrotas_puerta1_dado_puerta3)
        if((self.cantidad_triunfos_puerta1_dado_puerta3_cambio + self.cantidad_derrotas_puerta1_dado_puerta3_cambio) != 0):
            self.probabilidad_triunfo_puerta1_dado_puerta3_cambio = self.cantidad_triunfos_puerta1_dado_puerta3_cambio / (self.cantidad_triunfos_puerta1_dado_puerta3_cambio + self.cantidad_derrotas_puerta1_dado_puerta3_cambio)

        if((self.cantidad_triunfos_puerta2_dado_puerta1 + self.cantidad_derrotas_puerta2_dado_puerta1) != 0):
            self.probabilidad_triunfo_puerta2_dado_puerta1 = self.cantidad_triunfos_puerta2_dado_puerta1 / (self.cantidad_triunfos_puerta2_dado_puerta1 + self.cantidad_derrotas_puerta2_dado_puerta1)
        if((self.cantidad_triunfos_puerta2_dado_puerta1_cambio + self.cantidad_derrotas_puerta2_dado_puerta1_cambio) != 0):
            self.probabilidad_triunfo_puerta2_dado_puerta1_cambio = self.cantidad_triunfos_puerta2_dado_puerta1_cambio / (self.cantidad_triunfos_puerta2_dado_puerta1_cambio + self.cantidad_derrotas_puerta2_dado_puerta1_cambio)

        if((self.cantidad_triunfos_puerta2_dado_puerta3 + self.cantidad_derrotas_puerta2_dado_puerta3) != 0):
            self.probabilidad_triunfo_puerta2_dado_puerta3 = self.cantidad_triunfos_puerta2_dado_puerta3 / (self.cantidad_triunfos_puerta2_dado_puerta3 + self.cantidad_derrotas_puerta2_dado_puerta3)
        if((self.cantidad_triunfos_puerta2_dado_puerta3_cambio + self.cantidad_derrotas_puerta2_dado_puerta3_cambio) != 0):
            self.probabilidad_triunfo_puerta2_dado_puerta3_cambio = self.cantidad_triunfos_puerta2_dado_puerta3_cambio / (self.cantidad_triunfos_puerta2_dado_puerta3_cambio + self.cantidad_derrotas_puerta2_dado_puerta3_cambio)

        if((self.cantidad_triunfos_puerta3_dado_puerta1 + self.cantidad_derrotas_puerta3_dado_puerta1) != 0):
            self.probabilidad_triunfo_puerta3_dado_puerta1 = self.cantidad_triunfos_puerta3_dado_puerta1 / (self.cantidad_triunfos_puerta3_dado_puerta1 + self.cantidad_derrotas_puerta3_dado_puerta1)
        if((self.cantidad_triunfos_puerta3_dado_puerta1_cambio + self.cantidad_derrotas_puerta3_dado_puerta1_cambio) != 0):
            self.probabilidad_triunfo_puerta3_dado_puerta1_cambio = self.cantidad_triunfos_puerta3_dado_puerta1_cambio / (self.cantidad_triunfos_puerta3_dado_puerta1_cambio + self.cantidad_derrotas_puerta3_dado_puerta1_cambio)

        if((self.cantidad_derrotas_puerta3_dado_puerta2 + self.cantidad_triunfos_puerta3_dado_puerta2) != 0):
            self.probabilidad_triunfo_puerta3_dado_puerta2 = self.cantidad_triunfos_puerta3_dado_puerta2 / (self.cantidad_derrotas_puerta3_dado_puerta2 + self.cantidad_triunfos_puerta3_dado_puerta2)
        if((self.cantidad_triunfos_puerta3_dado_puerta2_cambio + self.cantidad_derrotas_puerta3_dado_puerta2_cambio) != 0):
            self.probabilidad_triunfo_puerta3_dado_puerta2_cambio = self.cantidad_triunfos_puerta3_dado_puerta2_cambio / (self.cantidad_triunfos_puerta3_dado_puerta2_cambio + self.cantidad_derrotas_puerta3_dado_puerta2_cambio)