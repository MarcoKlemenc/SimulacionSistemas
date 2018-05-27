from collections import defaultdict
from ImpresoraDeResultados import ImpresoraDeResultados
from GeneradorPuertas import GeneradorPuertas
from GeneradorPuertasSesgado import GeneradorPuertasSesgado
from GeneradorSeleccion import GeneradorSeleccion


class MontyHall:

    impresora_de_resultados = None
    generador_puertas = None
    generador_seleccion = None

    def __init__(self, tipo_generador_puertas):
        self.impresora_de_resultados = ImpresoraDeResultados()
        self.generador_puertas = self.obtener_generador_puertas(tipo_generador_puertas)
        self.generador_seleccion = GeneradorSeleccion()
    
    def obtener_generador_puertas(self, tipo):
        if tipo == 'normal':
            return GeneradorPuertas()
        elif tipo == 'sesgado':
            return GeneradorPuertasSesgado()

    def iniciar_entrenamiento(self):
        RONDAS = 10000
        print("Cantidad total de rondas: {}\n".format(RONDAS*2))
        resultados_al_no_cambiar = defaultdict(int)
        resultados_al_cambiar = defaultdict(int)

        for i in range(RONDAS):
            puertas = self.generador_puertas.generar_coche()
            # lo de abajo pone el coche siempre la puerta 3
            #puertas = self.generador_puertas.generar_coche(2)
            eleccion = self.generador_seleccion.generar_seleccion_aleatoria()
            puerta_mostrada = self.generador_puertas.mostrar_puerta(eleccion)
            resultados_al_no_cambiar[puertas[eleccion] == 'COCHE'] += 1
            if(puertas[eleccion] == 'COCHE'):
                resultado = "triunfo"
            else:
                resultado = "derrota"
            self.generador_seleccion.computar_resultado(eleccion, eleccion, puerta_mostrada, resultado)
            self.generador_puertas.reiniciar_puertas()

        for i in range(RONDAS):
            puertas = self.generador_puertas.generar_coche()
            #lo de abajo pone el coche siempre la puerta 3
            #puertas = self.generador_puertas.generar_coche(2)
            eleccion = self.generador_seleccion.generar_seleccion_aleatoria()
            puerta_mostrada = self.generador_puertas.mostrar_puerta(eleccion)
            #selecciona aleatoriamente una puerta hasta que encuentra la que no es ni la mostrada ni la elegida en
            #un principio. Revisar
            eleccion_antigua = eleccion
            while eleccion == eleccion_antigua or eleccion == puerta_mostrada:
                eleccion = self.generador_seleccion.generar_seleccion_aleatoria()
            #fin de le seleccion de la puerta por la que cambio
            resultados_al_cambiar[puertas[eleccion] == 'COCHE'] += 1
            if (puertas[eleccion] == 'COCHE'):
                resultado = "triunfo"
            else:
                resultado = "derrota"
            self.generador_seleccion.computar_resultado(eleccion_antigua, eleccion, puerta_mostrada, resultado)
            self.generador_puertas.reiniciar_puertas()

        self.generador_seleccion.actualizar_probabilidades()
        self.impresora_de_resultados.imprimir(resultados_al_no_cambiar, resultados_al_cambiar)

        for tup, prob in sorted(self.generador_seleccion.probabilidades.items(), key=lambda l: (l[0][0], l[0][1], l[0][2])):
            print("Probabilidad de triunfo al elegir la puerta {}, mostrarse la puerta {} y {}: {}".format(
                tup[0]+1, tup[1]+1, "cambiar" if tup[2] else "quedarse", "{0:.04f}".format(prob)
            ))

    def iniciar_competencia(self):
        RONDAS = 10000
        cantidad_triunfos = 0.0
        cantidad_derrotas = 0.0

        print("\nCantidad total de rondas: {}".format(RONDAS))

        for i in range(RONDAS):
            puertas = self.generador_puertas.generar_coche()
            #el caso de abajo se pone el coche siempre en la puerta 3
            #puertas = self.generador_puertas.generar_coche(2)
            eleccion = self.generador_seleccion.generar_seleccion_aleatoria()
            puerta_mostrada = self.generador_puertas.mostrar_puerta(eleccion)
            eleccion_final = self.generador_seleccion.generar_seleccion_probabilistica(eleccion, puerta_mostrada)
            if(puertas[eleccion_final] == 'COCHE'):
                cantidad_triunfos += 1
            else:
                cantidad_derrotas += 1
            self.generador_puertas.reiniciar_puertas()

        porcentaje_victorias = cantidad_triunfos / (cantidad_triunfos + cantidad_derrotas)
        print ("\nPorcentaje de victorias: " + str(porcentaje_victorias))
