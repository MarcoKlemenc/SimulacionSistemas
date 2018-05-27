from random import randint
from collections import defaultdict


class GeneradorSeleccion:

    triunfos = defaultdict(int)
    derrotas = defaultdict(int)
    probabilidades = defaultdict(float)

    def generar_seleccion_aleatoria(self):
        return randint(0, 2)
    
    def actualizar_probabilidades(self):
        for tup in set(self.triunfos).union(set(self.derrotas)):
            if self.triunfos.get(tup) and self.derrotas.get(tup):
                self.probabilidades[tup] = self.triunfos[tup] / (self.triunfos[tup] + self.derrotas[tup])
            elif not self.triunfos.get(tup):
                self.probabilidades[tup] = 0
            else:
                self.probabilidades[tup] = 1

    def generar_seleccion_probabilistica(self, eleccion, puerta_mostrada):
        faltante = [item for item in [0, 1, 2] if item not in [eleccion, puerta_mostrada]][0]
        probabilidad_al_no_cambiar = self.probabilidades[(eleccion, puerta_mostrada, False)]
        probabilidad_al_cambiar = self.probabilidades[(eleccion, puerta_mostrada, True)]
        if probabilidad_al_no_cambiar == 0 and probabilidad_al_cambiar == 0:
            return self.generar_seleccion_aleatoria()
        if probabilidad_al_no_cambiar >= probabilidad_al_cambiar:
            return eleccion
        return faltante

    def computar_resultado(self, eleccion_inicial, eleccion_final, puerta_mostrada, resultado):
        if resultado == 'triunfo':
            self.triunfos[(eleccion_inicial, puerta_mostrada, eleccion_inicial != eleccion_final)] += 1
        else:
            self.derrotas[(eleccion_inicial, puerta_mostrada, eleccion_inicial != eleccion_final)] += 1
