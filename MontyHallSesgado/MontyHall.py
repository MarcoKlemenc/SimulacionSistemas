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
            resultado = " "
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

        self.generador_seleccion.generar_probabilidades()
        self.impresora_de_resultados.imprimir(resultados_al_no_cambiar, resultados_al_cambiar)

        print("Probabilidad de triunfo dado: Puerta elegida = 1, Puerta mostrada = 2, Decision = Quedarse : " +
              str(self.generador_seleccion.probabilidad_triunfo_puerta1_dado_puerta2))
        print("Probabilidad de triunfo dado: Puerta elegida = 1, Puerta mostrada = 2, Decision = Cambio : " +
              str(self.generador_seleccion.probabilidad_triunfo_puerta1_dado_puerta2_cambio))
        print("Probabilidad de triunfo dado: Puerta elegida = 1, Puerta mostrada = 3, Decision = Quedarse : " +
              str(self.generador_seleccion.probabilidad_triunfo_puerta1_dado_puerta3))
        print("Probabilidad de triunfo dado: Puerta elegida = 1, Puerta mostrada = 3, Decision = Cambio : " +
              str(self.generador_seleccion.probabilidad_triunfo_puerta1_dado_puerta3_cambio))
        print("Probabilidad de triunfo dado: Puerta elegida = 2, Puerta mostrada = 1, Decision = Quedarse : " +
              str(self.generador_seleccion.probabilidad_triunfo_puerta2_dado_puerta1))
        print("Probabilidad de triunfo dado: Puerta elegida = 2, Puerta mostrada = 1, Decision = Cambio : " +
              str(self.generador_seleccion.probabilidad_triunfo_puerta2_dado_puerta1_cambio))
        print("Probabilidad de triunfo dado: Puerta elegida = 2, Puerta mostrada = 3, Decision = Quedarse : " +
              str(self.generador_seleccion.probabilidad_triunfo_puerta2_dado_puerta3))
        print("Probabilidad de triunfo dado: Puerta elegida = 2, Puerta mostrada = 3, Decision = Cambio : " +
              str(self.generador_seleccion.probabilidad_triunfo_puerta2_dado_puerta3_cambio))
        print("Probabilidad de triunfo dado: Puerta elegida = 3, Puerta mostrada = 1, Decision = Quedarse : " +
              str(self.generador_seleccion.probabilidad_triunfo_puerta3_dado_puerta1))
        print("Probabilidad de triunfo dado: Puerta elegida = 3, Puerta mostrada = 1, Decision = Cambio : " +
              str(self.generador_seleccion.probabilidad_triunfo_puerta3_dado_puerta1_cambio))
        print("Probabilidad de triunfo dado: Puerta elegida = 3, Puerta mostrada = 2, Decision = Quedarse : " +
              str(self.generador_seleccion.probabilidad_triunfo_puerta3_dado_puerta2))
        print("Probabilidad de triunfo dado: Puerta elegida = 3, Puerta mostrada = 2, Decision = Cambio : " +
              str(self.generador_seleccion.probabilidad_triunfo_puerta3_dado_puerta2_cambio))

    def iniciar_competencia(self):
        RONDAS = 10000
        cantidad_triunfos = 0.0
        cantidad_derrotas = 0.0

        print("\n\nCantidad total de rondas: " + str(RONDAS) + " \n")

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
        print ("\n Porcentaje de victorias: " + str(porcentaje_victorias))
