from collections import defaultdict
from random import randint

RONDAS = 10000
print("RONDAS: " + str(RONDAS))
resultados = defaultdict(int)
cantidad = 0

for i in range(RONDAS):
    puertas = ['CABRA', 'CABRA', 'CABRA']
    cabras = [0, 1, 2]
    coche = randint(0,2)
    puertas[coche] = 'COCHE'
    cabras.remove(coche)
    eleccion = randint(0,2)
    descubierta = eleccion
    while descubierta == eleccion and puertas[descubierta] != 'CABRA':
        descubierta = randint(0,2)
    cambiar = randint(0,1)
    if cambiar:
        eleccion_antigua = eleccion
        while eleccion == eleccion_antigua and eleccion == descubierta:
            eleccion = randint(0, 2)
    resultados[(puertas[eleccion] == 'COCHE', cambiar)] += 1

a=resultados[(True,0)]
b=resultados[(False,1)]
c=resultados[(True,1)]
d=resultados[(False,0)]

for k, v in sorted(resultados.items(), key=lambda l: (l[0][1], l[0][0])):
    print("{} al {}cambiar: {}".format("Victorias" if k[0] else "Derrotas", "no " if not k[1] else "", v))

print("Porcentaje Victorias al NO haber cambiado: " +  str(a) + " / " + str(a+d) + " = " + str(round((float(a)/(a+d))*100, 2)))
print("Porcentaje Victorias al SI haber cambiado: " +  str(c) + " / " + str(b+c) + " = " + str(round((float(c)/(b+c))*100, 2)))
