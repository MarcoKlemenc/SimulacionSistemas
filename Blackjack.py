from collections import defaultdict
from random import randint

RONDAS = 5000000

resultados = defaultdict(lambda: [0, 0, 0])
cantidad = 0

while (cantidad < RONDAS):
    manos_jugador = []
    mano_jugador = 0
    mano_casa = 0
    mano_jugador += randint(1, 10)
    mano_jugador += randint(1, 10)
    mano_casa += randint(1, 10)
    mano_casa += randint(1, 10)
    while(mano_jugador < 11):
        mano_jugador += randint(1, 10)
    pedir = randint(0, 1)
    while(pedir):
        manos_jugador.append((mano_jugador, pedir))
        mano_jugador += randint(1, 10)
        pedir = randint(0, 1)
    manos_jugador.append((mano_jugador, pedir))
    while(mano_casa < 17):
        mano_casa += randint(1, 10)
    if(mano_jugador > 21 and mano_casa > 21 or mano_jugador == mano_casa):
        resultado = 0
    elif(mano_jugador <= 21 and (mano_casa > 21 or mano_jugador > mano_casa)):
        resultado = 1
    elif(mano_casa <= 21 and (mano_jugador > 21 or mano_jugador < mano_casa)):
        resultado = -1
    posicion = resultado * (-1) + 1
    for mano in manos_jugador:
        resultados[mano][posicion] += 1
    cantidad += 1
    porcentaje = 100*cantidad/RONDAS
    if(porcentaje.is_integer()):
        print("{}%".format(int(porcentaje)))
for k, v in sorted(resultados.items(), key=lambda x: (x[0][0], x[0][1])):
    if(k[0] <= 21):
        print("{} {}: {}-{}-{} ({}%)".format("P" if k[1] else "Q", str(k[0]).zfill(2), v[0], v[1], v[2], '{0:.02f}'.format((v[0]+v[1])*100/(v[0]+v[1]+v[2]))))