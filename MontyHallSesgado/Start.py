#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from MontyHall import MontyHall
from sys import argv

ans=True
while ans:
    print ("""
    1.Aleatoria
    2.Patron
    3.Repeticion
    4.Sesgada
    5.SALIR
    """)
    ans=raw_input('Elija opción: ')
    if ans=='1':
      montyHall = MontyHall('normal')
    elif ans=='2':
      montyHall = MontyHall('patron')
    elif ans=='3':
      montyHall = MontyHall('repetido')
    elif ans=='4':
      montyHall = MontyHall('sesgado')
    elif ans=='5':
      exit()
    elif ans !='':
      print("\n Opción no válida!")
    montyHall.iniciar_entrenamiento()
    montyHall.iniciar_competencia()

#montyHall = MontyHall(argv[1])
