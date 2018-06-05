from MontyHall import MontyHall

opciones = {
    '1': 'Normal',
    '2': 'Patron',
    '3': 'Repetido',
    '4': 'Sesgado',
    '5': 'SALIR'
}


while True:
    print ()
    for k in sorted(opciones.keys()):
        print ("{}. {}".format(k, opciones[k]))
    generador_entrenamiento = None
    while not generador_entrenamiento:
        generador_entrenamiento = opciones.get(raw_input('Elija el generador de entrenamiento: '))
        if not generador_entrenamiento:
            print("Opcion no valida")
    if generador_entrenamiento == "SALIR":
        break
    generador_competencia = None
    while not generador_competencia:
        generador_competencia = opciones.get(raw_input('Elija el generador de competencia: '))
        if not generador_competencia:
            print("Opcion no valida")
    if generador_competencia == "SALIR":
        break
    rondas_entrenamiento = 0
    while rondas_entrenamiento <= 0 or rondas_entrenamiento % 2:
        rondas_entrenamiento = int(raw_input('Defina la cantidad de rondas de entrenamiento (debe ser par): '))
        if rondas_entrenamiento <= 0 or rondas_entrenamiento % 2:
            print("Valor no valido")
    rondas_competencia = 0
    while rondas_competencia <= 0:
        rondas_competencia = int(raw_input('Defina la cantidad de rondas de competencia: '))
        if rondas_competencia <= 0:
            print("Valor no valido")
    montyHall = MontyHall(generador_entrenamiento.lower(), rondas_entrenamiento, generador_competencia.lower(), rondas_competencia)
    print()
    montyHall.iniciar_entrenamiento()
    montyHall.iniciar_competencia()
