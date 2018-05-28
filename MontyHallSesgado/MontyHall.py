from collections import defaultdict
from ImpresoraDeResultados import ImpresoraDeResultados
from GeneradorPuertas import GeneradorPuertas
from GeneradorPuertasSesgado import GeneradorPuertasSesgado
from GeneradorPuertasRepetido import GeneradorPuertasRepetido
from GeneradorPuertasPatron import GeneradorPuertasPatron
from GeneradorSeleccion import GeneradorSeleccion


class MontyHall:

    impresora_de_resultados = None
    generador_puertas = None
    generador_seleccion = None

    def __init__(self, tipo_generador_puertas):
        self.impresora_de_resultados = ImpresoraDeResultados()
        self.generador_puertas = self.obtener_generador_puertas(tipo_generador_puertas)
        self.generador_seleccion = GeneradorSeleccion()
        self.resultados_al_no_cambiar = defaultdict(int)
        self.resultados_al_cambiar = defaultdict(int)
    
    def obtener_generador_puertas(self, tipo):
        if tipo == 'normal':
            return GeneradorPuertas()
        elif tipo == 'sesgado':
            return GeneradorPuertasSesgado()
        elif tipo == 'repetido':
            return GeneradorPuertasRepetido()
        elif tipo == 'patron':
            return GeneradorPuertasPatron()
    
    def practicar_rondas(self, cantidad, cambiar):
        for i in range(cantidad):
            puertas = self.generador_puertas.generar_coche()
            eleccion = self.generador_seleccion.generar_seleccion_aleatoria()
            puerta_mostrada = self.generador_puertas.mostrar_puerta(eleccion)
            #selecciona aleatoriamente una puerta hasta que encuentra la que no es ni la mostrada ni la elegida en
            #un principio. Revisar
            eleccion_antigua = eleccion
            if not cambiar:
                self.resultados_al_no_cambiar[puertas[eleccion] == 'COCHE'] += 1
            else:
                while eleccion == eleccion_antigua or eleccion == puerta_mostrada:
                    eleccion = self.generador_seleccion.generar_seleccion_aleatoria()
                #fin de le seleccion de la puerta por la que cambio
                self.resultados_al_cambiar[puertas[eleccion] == 'COCHE'] += 1
            if (puertas[eleccion] == 'COCHE'):
                resultado = "triunfo"
            else:
                resultado = "derrota"
            self.generador_seleccion.computar_resultado(eleccion_antigua, eleccion, puerta_mostrada, resultado)
            self.generador_puertas.reiniciar_puertas()

    def iniciar_entrenamiento(self):
        RONDAS = 10000
        print("Cantidad total de rondas: {}\n".format(RONDAS*2))

        self.practicar_rondas(10000, False)
        self.practicar_rondas(10000, True)

        self.generador_seleccion.actualizar_probabilidades()
        self.impresora_de_resultados.imprimir(self.resultados_al_no_cambiar, self.resultados_al_cambiar)

        for tup, prob in sorted(self.generador_seleccion.probabilidades.items(), key=lambda l: (l[0][0], l[0][1], l[0][2])):
            print("Probabilidad de triunfo al elegir la puerta {}, mostrarse la puerta {} y {}: {}".format(
                tup[0]+1, tup[1]+1, "cambiar" if tup[2] else "quedarse", "{0:.04f}".format(prob)
            ))

    def iniciar_competencia(self):
        RONDAS = 10000
        cantidad_triunfos = 0
        cantidad_derrotas = 0
        seleccion_inicial = -1

        print("\nCantidad total de rondas: {}".format(RONDAS))

        for h in range(1):
            coches_por_puerta = [0, 0, 0]
            for i in range(10000):
                puertas = self.generador_puertas.generar_coche()
                eleccion = self.generador_seleccion.generar_seleccion_aleatoria() if seleccion_inicial == -1 else seleccion_inicial
                puerta_mostrada = self.generador_puertas.mostrar_puerta(eleccion)
                eleccion_final = self.generador_seleccion.generar_seleccion_probabilistica(eleccion, puerta_mostrada) if seleccion_inicial == -1 else seleccion_inicial
                if(puertas[eleccion_final] == 'COCHE'):
                    cantidad_triunfos += 1
                else:
                    cantidad_derrotas += 1
                coches_por_puerta[puertas.index('COCHE')] += 1
                self.generador_puertas.reiniciar_puertas()
                seleccion_inicial = -1
            seleccion_inicial = coches_por_puerta.index(max(coches_por_puerta))
        
        porcentaje_victorias = cantidad_triunfos / (cantidad_triunfos + cantidad_derrotas)
        print ("\nPorcentaje de victorias: " + str(porcentaje_victorias))
