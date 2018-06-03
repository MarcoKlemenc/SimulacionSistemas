from collections import defaultdict
from ImpresoraDeResultados import ImpresoraDeResultados
from GeneradorPuertasAleatoria import GeneradorPuertasAleatoria
from GeneradorPuertasSesgado import GeneradorPuertasSesgado
from GeneradorPuertasRepetido import GeneradorPuertasRepetido
from GeneradorPuertasPatron import GeneradorPuertasPatron
from GeneradorSeleccion import GeneradorSeleccion


class MontyHall:

    impresora_de_resultados = None
    generador_seleccion = None

    def __init__(self, generador_entrenamiento, rondas_entrenamiento, generador_competencia, rondas_competencia):
        self.impresora_de_resultados = ImpresoraDeResultados()
        self.generador_inicial = self.obtener_generador_puertas(generador_entrenamiento)
        self.generador_final = self.obtener_generador_puertas(generador_competencia) if generador_competencia != generador_entrenamiento else self.generador_inicial
        self.cantidad_entrenamiento = int(rondas_entrenamiento/2)
        self.cantidad_competencia = rondas_competencia
        self.generador_seleccion = GeneradorSeleccion()
        self.resultados_al_no_cambiar = defaultdict(int)
        self.resultados_al_cambiar = defaultdict(int)
    
    def obtener_generador_puertas(self, tipo):
        if tipo == 'normal':
            return GeneradorPuertasAleatoria()
        elif tipo == 'sesgado':
            return GeneradorPuertasSesgado()
        elif tipo == 'repetido':
            return GeneradorPuertasRepetido()
        elif tipo == 'patron':
            return GeneradorPuertasPatron()
    
    def practicar_rondas(self, cantidad, cambiar):
        for i in range(cantidad):
            puertas = self.generador_inicial.generar_coche()
            eleccion = self.generador_seleccion.generar_seleccion_aleatoria()
            puerta_mostrada = self.generador_inicial.mostrar_puerta(eleccion)
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
            self.generador_seleccion.computar_resultado(eleccion_antigua, eleccion, puerta_mostrada, self.generador_inicial.get_puerta_ganadora())
            self.generador_inicial.reiniciar_puertas()

    def iniciar_entrenamiento(self):
        self.practicar_rondas(self.cantidad_entrenamiento, False)
        self.practicar_rondas(self.cantidad_entrenamiento, True)

        self.generador_seleccion.actualizar_probabilidades()
        self.generador_seleccion.encontrar_patron()

        self.impresora_de_resultados.imprimir(self.resultados_al_no_cambiar, self.resultados_al_cambiar)
        for tup, prob in sorted(self.generador_seleccion.probabilidades.items(), key=lambda l: (l[0][0], l[0][1], l[0][2])):
            print("Probabilidad de triunfo al elegir la puerta {}, mostrarse la puerta {} y {}: {}".format(
                tup[0]+1, tup[1]+1, "cambiar" if tup[2] else "quedarse", "{0:.04f}".format(prob)
            ))
        print()

    def iniciar_competencia(self):
        cantidad_triunfos = 0
        cantidad_derrotas = 0
        seleccion_inicial = -1

        for h in range(1):
            coches_por_puerta = [0, 0, 0]
            for i in range(self.cantidad_competencia):
                eleccion_patron = self.generador_seleccion.generar_seleccion_por_patron()
                puertas = self.generador_final.generar_coche()
                if eleccion_patron == -1:
                    eleccion = self.generador_seleccion.generar_seleccion_aleatoria() if seleccion_inicial == -1 else seleccion_inicial
                else:
                    eleccion = eleccion_patron
                puerta_mostrada = self.generador_final.mostrar_puerta(eleccion)
                if eleccion_patron == -1:
                    eleccion_final = self.generador_seleccion.generar_seleccion_probabilistica(eleccion, puerta_mostrada) if seleccion_inicial == -1 else seleccion_inicial
                else:
                    eleccion_final = eleccion_patron
                if(puertas[eleccion_final] == 'COCHE'):
                    cantidad_triunfos += 1
                else:
                    cantidad_derrotas += 1
                coches_por_puerta[puertas.index('COCHE')] += 1
                self.generador_final.reiniciar_puertas()
                seleccion_inicial = -1
            seleccion_inicial = coches_por_puerta.index(max(coches_por_puerta))
        
        self.impresora_de_resultados.imprimir_competencia(cantidad_triunfos, cantidad_derrotas)
