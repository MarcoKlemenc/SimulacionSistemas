from MontyHall import MontyHall

while True:
    print ("\n1. Aleatoria")
    print ("2. Patron")
    print ("3. Repeticion")
    print ("4. Sesgada")
    ans=input('Elija una opcion: ')
    montyHall = None
    if ans=='1':
        montyHall = MontyHall('normal')
    elif ans=='2':
        montyHall = MontyHall('patron')
    elif ans=='3':
        montyHall = MontyHall('repetido')
    elif ans=='4':
        montyHall = MontyHall('sesgado')
    else:
        print("Opcion no valida")
    print()
    if montyHall:
        montyHall.iniciar_entrenamiento()
        montyHall.iniciar_competencia()
