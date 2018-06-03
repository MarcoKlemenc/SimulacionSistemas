from random import randint
from collections import defaultdict


class GeneradorSeleccion:

    triunfos = defaultdict(int)
    derrotas = defaultdict(int)
    probabilidades = defaultdict(float)
    puertas = ""
    patron = None
    contador = 0

    def encontrar_patron(self):
        new_s = self.puertas
        patron = None
        while len(new_s) >= len(self.puertas)/2 and not patron:
            i = (new_s+new_s).find(new_s, 1, -1)
            patron = None if i == -1 else self.puertas[:i]
            new_s = new_s[:-1]
        if patron:
            self.patron = patron
            self.contador = len(self.puertas) - self.puertas.rfind(patron) - len(patron)
    
    def generar_seleccion_por_patron(self):
        if self.patron:
            seleccion = int(self.patron[self.contador])
            self.contador += 1
            if self.contador == len(self.patron):
                self.contador = 0
            return seleccion
        return -1

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

    def computar_resultado(self, eleccion_inicial, eleccion_final, puerta_mostrada, puerta_ganadora):
        if eleccion_final == puerta_ganadora:
            self.triunfos[(eleccion_inicial, puerta_mostrada, eleccion_inicial != eleccion_final)] += 1
        else:
            self.derrotas[(eleccion_inicial, puerta_mostrada, eleccion_inicial != eleccion_final)] += 1
        self.puertas += str(puerta_ganadora)
