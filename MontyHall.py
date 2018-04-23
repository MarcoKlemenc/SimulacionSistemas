from collections import defaultdict
from random import randint

RONDAS = 10000
print("Cantidad total de rondas: {}\n".format(RONDAS*2))
resultados_al_no_cambiar = defaultdict(int)
resultados_al_cambiar = defaultdict(int)

for i in range(RONDAS):
    puertas = ['CABRA', 'CABRA', 'CABRA']
    cabras = [0, 1, 2]
    coche = randint(0, 2)
    puertas[coche] = 'COCHE'
    cabras.remove(coche)
    eleccion = randint(0, 2)
    descubierta = eleccion
    while descubierta == eleccion and puertas[descubierta] != 'CABRA':
        descubierta = randint(0, 2)
    resultados_al_no_cambiar[puertas[eleccion] == 'COCHE'] += 1

for i in range(RONDAS):
    puertas = ['CABRA', 'CABRA', 'CABRA']
    cabras = [0, 1, 2]
    coche = randint(0, 2)
    puertas[coche] = 'COCHE'
    cabras.remove(coche)
    eleccion = randint(0, 2)
    descubierta = eleccion
    while descubierta == eleccion and puertas[descubierta] != 'CABRA':
        descubierta = randint(0, 2)
    eleccion_antigua = eleccion
    while eleccion == eleccion_antigua and eleccion == descubierta:
        eleccion = randint(0, 2)
    resultados_al_cambiar[puertas[eleccion] == 'COCHE'] += 1

total_partidas_con_decision = sum(v for k, v in resultados_al_no_cambiar.items())
for k, v in sorted(resultados_al_no_cambiar.items(), key=lambda l: (l[0])):
    porcentaje = '{0:.02f}'.format(100*v / total_partidas_con_decision)
    print("{} al no cambiar: {} ({}%)".format("Victorias" if k else "Derrotas", v, porcentaje))
print("")

total_partidas_con_decision = sum(v for k, v in resultados_al_cambiar.items())
for k, v in sorted(resultados_al_cambiar.items(), key=lambda l: (l[0])):
    porcentaje = '{0:.02f}'.format(100*v / total_partidas_con_decision)
    print("{} al cambiar: {} ({}%)".format("Victorias" if k else "Derrotas", v, porcentaje))
print("")
