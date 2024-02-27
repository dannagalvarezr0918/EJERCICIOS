from tabulate import tabulate

from . import menu as mn
from .condiciones import condicional_edad

listado_jugadores = []
listado_categoria = {"Novato": [], "Intermedio": [], "Avanzado": []}

def buscar_jugador(nombre:str):
  for jugador in listado_jugadores:
    if jugador["nombre"] == nombre:
      return jugador

def puntuar(jugador1, jugador2):
  nombre1 = jugador1["nombre"]
  nombre2 = jugador2["nombre"]
  puntos_jugador1 = int(input(f"Cuántos puntos hizo {nombre1}"))
  puntos_jugador2 = int(input(f"Cuántos puntos hizo {nombre2}"))

  jugador1["PJ"] += 1
  jugador2["PJ"] += 1

  if puntos_jugador1 > puntos_jugador2:
    jugador1["PG"] += 1
    jugador1["TP"] += 2
    jugador1["PA"] += (puntos_jugador1 - puntos_jugador2)
    jugador2["PP"] += 1
  elif puntos_jugador2 > puntos_jugador1:
    jugador2["PG"] += 1
    jugador2["TP"] += 2
    jugador2["PA"] += (puntos_jugador2 - puntos_jugador1)
    jugador1["PP"] += 1
  else:
    jugador1["TP"] += 1
    jugador2["TP"] += 1
def agregar_categoria(jugador:dict):
  nombre = jugador["nombre"]
  categoria = jugador["categoria"]

  if categoria == "Novato":
    listado_categoria["Novato"].append(nombre)
  elif categoria == "Intermedio":
    listado_categoria["Intermedio"].append(nombre)
  elif categoria == "Avanzado":
    listado_categoria["Avanzado"].append(nombre)

def agregar_jugador():
  mn.borrar_pantalla()
  titulo = """
  ++++++++++++++++++++++++++++++++++++
  +  SISTEMA REGISTRO jugadores  +
  ++++++++++++++++++++++++++++++++++
  """
  print(titulo)
  try:
    nombre = input("Ingrese el nombre del jugador: ").title()
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    categoria = input(f"Ingrese la categoria de {nombre} (Novato, Intermedio, Avanzado): ").capitalize()
    if condicional_edad(edad, categoria) == False:
      agregar_jugador()
    nuevo_jugador = {
      "nombre": nombre,
      "edad": edad,
      "categoria": categoria,
      "puntuacion": {
        "PJ": 0,
        "PG": 0,
        "PP": 0,
        "PA": 0,
        "TP": 0
        }
      }
    listado_jugadores.append(nuevo_jugador)
    agregar_categoria(nuevo_jugador)

    print(f"{nombre} registro exitoso, quieres ingresar otro jugador? S(si) enter(no)")
    opcion = input("\n>> ").upper()
    if opcion == "S":
      agregar_jugador()
    else:
      mn.menu_principal()
  except ValueError:
    input("Valor no valido. Presiona enter para volver")
    mn.menu_principal()

def registar_fecha():
  mn.borrar_pantalla()
  titulo = """
  +++++++++++++++++++++++++++++++++++
  +  REGISTRO DE FECHAS DEL TORNEO  +
  +++++++++++++++++++++++++++++++++++
  """
  print(titulo)
  print(tabulate([["1.", "Novato"], ["2.","Intermedio"], ["3.","Avanzado"]], tablefmt="grid"))
  opcion = input("\n>> ")
  if opcion == "1":
    definir_fecha("Novato")
  elif opcion == "2":
    definir_fecha("Intermedio")
  elif opcion == "3":
    definir_fecha("Avanzado")
  else:
    registar_fecha()

def definir_fecha(categoria:str):
  if len(listado_categoria[categoria]) < 5:
    input("Todavía faltan jugadores para iniciar los partidos en esta categoría.\nPresiona enter para voler.")
    mn.menu_principal()
  else:
    print(tabulate([listado_categoria[categoria]],tablefmt="grid"))
    jugador1 = input("Ingresa el nombre del primer jugador: ").title()
    jugador2 = input("Ingresa el nombre del segundo jugador: ").title()
    atleta1 = buscar_jugador(jugador1)
    atleta2 = buscar_jugador(jugador2)
    if atleta1["categoria"] != categoria or atleta2["categoria"] != categoria:
      input("Alguno de tus deportistas no hace parte de la categoría.\nPresiona enter para voler.")
      mn.menu_principal()
    puntuar(atleta1, atleta2)
    mn.borrar_pantalla()
    print(tabulate([jugador1, jugador2], headers="keys",tablefmt="grid"))
    input("Presiona enter para volver.")
    mn.menu_principal()