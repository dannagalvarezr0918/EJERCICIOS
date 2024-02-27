from tabulate import tabulate
import modulos.registrosismos as regsism
import os

print ("""
    ++++++++++++++++++++++++++++++++
    +      REGISTRO DE SISMOS      +
    ++++++++++++++++++++++++++++++++
    """)


def main():
    ciudades = []
    sismos_por_ciudad = []
    num_sismos = int(input("Ingrese la cantidad de sismos a registrar por ciudad: "))

    while True:
        print("\nMenú:")
        print("1. Registrar Ciudad")
        print("2. Registrar Sismo")
        print("3. Buscar sismos por ciudad")
        print("4. Informe de riesgo")
        print("5. Salir")
        opcion = int(input("Ingrese el número de la opción que desea realizar: "))

        

        if opcion == 1:
            regsism.registrar_ciudad(ciudades, sismos_por_ciudad, num_sismos)
        elif opcion == 2:
            regsism.registrar_sismo(ciudades, sismos_por_ciudad)
        elif opcion == 3:
            regsism.buscar_sismos_por_ciudad(ciudades, sismos_por_ciudad)
        elif opcion == 4:
            regsism.informe_de_riesgo(ciudades, sismos_por_ciudad, num_sismos)
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.")

if __name__ == "__main__":
    main()
