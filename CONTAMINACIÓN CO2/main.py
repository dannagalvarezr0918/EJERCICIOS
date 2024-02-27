from tabulate import tabulate
import modulos.registro_dependecias as regdepend
import modulos.results as results
import os

print("""
    ++++++++++++++++++++++++++++++++
    +      PRODUCCIÓN DE CO2       +
    ++++++++++++++++++++++++++++++++
    """)

def main ():
    anotherone = {}
    total_dic = {}

    while True:
        print("\nMENU:")
        print("1. Registrar Dependencia")
        print("2. Registrar Consumo Dependencia")
        print("3. Ver CO2 producido")
        print("4. Dependencia que produce mayor CO2")
        print("5. Salir")
        opcion = int(input("Ingrese el número de la opción que desea realizar: "))

    
        if opcion == 1:
            regdepend.registro_dependencia(anotherone)
        elif opcion == 2:
            dependencia = input('Ingrese el nombre de la dependencia que desea registrar el consumo: ')
            submenu_registros(anotherone,dependencia)
        elif opcion == 3:
            results.view_table(anotherone,total_dic)
        elif opcion == 4:
            results.find_max(total_dic)
        elif opcion == 5:
            print('Saliendo del programa...')
            break

        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.")

def solicitar_opcion(mensaje):
        while True:
            try:
                opcion = int(input(mensaje))
                return opcion
            except ValueError:
                print("Opcion invalida")

def submenu_registros(anotherone,dependencia):
    
 print("""
    ++++++++++++++++++++++++
    + REGISTRO DEPENDENCIA +
    ++++++++++++++++++++++++
    """)
 while True:
        print("\nMENU:")
        print("1. Registrar consumo electricidad")
        print("2. Registrar consumo transporte")
        print("3. Registrar consumo por dispositivo")
        print("4. Salir")
        opcion = int(input("Ingrese el número de la opción que desea realizar: "))
        
        
        if opcion == 1:
            regdepend.registro_electricidad(anotherone,dependencia)
        elif opcion == 2:
            regdepend.registro_transporte(anotherone,dependencia)
        elif opcion == 3:
            regdepend.registro_dispositivo(anotherone,dependencia)
        elif opcion == 4:
            print('Saliendo del programa...')
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.")


if __name__ == "__main__":
    main()

