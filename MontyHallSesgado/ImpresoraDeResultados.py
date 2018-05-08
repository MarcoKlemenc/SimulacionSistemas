class ImpresoraDeResultados:

    def imprimir(self, resultados_al_no_cambiar, resultados_al_cambiar):
        total_partidas_con_decision = sum(v for k, v in resultados_al_no_cambiar.items())
        for k, v in sorted(resultados_al_no_cambiar.items(), key=lambda l: (l[0])):
            porcentaje = '{0:.02f}'.format(100 * v / total_partidas_con_decision)
            print("{} al no cambiar: {} ({}%)".format("Victorias" if k else "Derrotas", v, porcentaje))
        print("")

        total_partidas_con_decision = sum(v for k, v in resultados_al_cambiar.items())
        for k, v in sorted(resultados_al_cambiar.items(), key=lambda l: (l[0])):
            porcentaje = '{0:.02f}'.format(100 * v / total_partidas_con_decision)
            print("{} al cambiar: {} ({}%)".format("Victorias" if k else "Derrotas", v, porcentaje))
        print("")