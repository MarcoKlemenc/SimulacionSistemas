from collections import defaultdict
from random import randint
from ImpresoraDeResultados import ImpresoraDeResultados
from GeneradorPuertasAleatorias import GeneradorPuertasAleatorias
from GeneradorSeleccionAleatoria import GeneradorSeleccionAleatoria


class MontyHallSesgado:

    impresora_de_resultados = None
    generador_puertas_aleatorias = None
    generador_seleccion_aleatoria = None


    def __init__(self):
        self.impresora_de_resultados = ImpresoraDeResultados()
        self.generador_puertas_aleatorias = GeneradorPuertasAleatorias()
        self.generador_seleccion_aleatoria = GeneradorSeleccionAleatoria()

    def start_monty_hall_sesgado(self):
        RONDAS = 10000
        print("Cantidad total de rondas: {}\n".format(RONDAS*2))
        resultados_al_no_cambiar = defaultdict(int)
        resultados_al_cambiar = defaultdict(int)

        for i in range(RONDAS):
            puertas = self.generador_puertas_aleatorias.generar()
            eleccion = self.generador_seleccion_aleatoria.generar_seleccion()
            puerta_mostrada = self.generador_puertas_aleatorias.mostrar_puerta(eleccion)
            resultados_al_no_cambiar[puertas[eleccion] == 'COCHE'] += 1
            self.generador_puertas_aleatorias.reiniciar_puertas()

        for i in range(RONDAS):
            puertas = self.generador_puertas_aleatorias.generar()
            eleccion = self.generador_seleccion_aleatoria.generar_seleccion()
            puerta_mostrada = self.generador_puertas_aleatorias.mostrar_puerta(eleccion)
            #selecciona aleatoriamente una puerta hasta que encuentra la que no es ni la mostrada ni la elegida en
            #un principio. Revisar
            eleccion_antigua = eleccion
            while eleccion == eleccion_antigua or eleccion == puerta_mostrada:
                eleccion = randint(0, 2)
            #fin de le seleccion de la puerta por la que cambio
            resultados_al_cambiar[puertas[eleccion] == 'COCHE'] += 1
            self.generador_puertas_aleatorias.reiniciar_puertas()

        self.impresora_de_resultados.imprimir(resultados_al_no_cambiar, resultados_al_cambiar)


