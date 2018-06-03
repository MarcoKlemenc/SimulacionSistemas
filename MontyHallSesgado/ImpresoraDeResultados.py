class ImpresoraDeResultados:

    def imprimir(self, resultados_al_no_cambiar, resultados_al_cambiar):
        total_partidas_con_decision = sum(v for k, v in resultados_al_no_cambiar.items())
        for k, v in sorted(resultados_al_no_cambiar.items(), key=lambda l: (l[0]), reverse=True):
            porcentaje = '{0:.02f}'.format(100 * v / total_partidas_con_decision)
            print("{} al no cambiar: {} ({}%)".format("Triunfos" if k else "Derrotas", v, porcentaje))
        print()

        total_partidas_con_decision = sum(v for k, v in resultados_al_cambiar.items())
        for k, v in sorted(resultados_al_cambiar.items(), key=lambda l: (l[0]), reverse=True):
            porcentaje = '{0:.02f}'.format(100 * v / total_partidas_con_decision)
            print("{} al cambiar: {} ({}%)".format("Triunfos" if k else "Derrotas", v, porcentaje))
        print()
    
    def imprimir_entrenamiento(self, generador):
        for tup, prob in sorted(generador.probabilidades.items(), key=lambda l: (l[0][0], l[0][1], l[0][2])):
            print("Triunfos al elegir la puerta {}, mostrarse la puerta {} y {}: {} ({}%)".format(
                tup[0]+1, tup[1]+1, "cambiar" if tup[2] else "quedarse", generador.triunfos.get(tup) or "0", "{0:.02f}".format(100*prob)
            ))
        print()
    
    def imprimir_competencia(self, triunfos, derrotas):
        porcentaje = '{0:.02f}'.format(100 * triunfos / (triunfos + derrotas))
        print ("Triunfos: {} ({}%)".format(triunfos, porcentaje))
        porcentaje = '{0:.02f}'.format(100 * derrotas / (triunfos + derrotas))
        print ("Derrotas: {} ({}%)".format(derrotas, porcentaje))