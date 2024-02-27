import sys
from os import system

from tabulate import tabulate
from .jugadores import agregar_jugador, registar_fecha
from .reportes import menu_reportes

def borrar_pantalla():
  if sys.platform == "linux" or sys.platform == "darwin":
    system("clear")
  else:
    system("cls")

def menu_principal():
  borrar_pantalla()
  titulo = """
  +++++++++++++++++++++++++++++
  +       TORNEO TENIS        +
  +++++++++++++++++++++++++++++
  """
  print(titulo)
  menu = [["1.", "Agregar jugador"], ["2.", "Registrar fecha"], ["3.","Reportes"], ["4.","Salir"]]
  print(tabulate(menu,tablefmt="grid"))
  opcion = input("\n>> ")
  if opcion == "1":
    agregar_jugador()
    menu_principal()
  elif opcion == "2":
    registar_fecha()
    menu_principal()
  elif opcion == "3":
    menu_reportes()
    menu_principal()
  elif opcion == "4":
    sys.exit("Hasta luego!")
  else:
    menu_principal()