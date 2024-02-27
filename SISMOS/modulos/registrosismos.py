def registrar_ciudad(ciudades, sismos_por_ciudad, num_sismos):
    ciudad = input("Ingrese el nombre de la ciudad: ")
    ciudades.append(ciudad)
    sismos_ciudad = []
    for i in range(num_sismos):
        sismo = float(input(f"Ingrese la magnitud del sismo {i + 1} para {ciudad}: "))
        sismos_ciudad.append(sismo)
    sismos_por_ciudad.append(sismos_ciudad)

def registrar_sismo(ciudades, sismos_por_ciudad):
    ciudad = input("Ingrese el nombre de la ciudad: ")
    if ciudad in ciudades:
        indice_ciudad = ciudades.index(ciudad)
        sismo = float(input("Ingrese la magnitud del sismo: "))
        sismos_por_ciudad[indice_ciudad].append(sismo)
    else:
        print("La ciudad no está registrada.")

def buscar_sismos_por_ciudad(ciudades, sismos_por_ciudad):
    ciudad = input("Ingrese el nombre de la ciudad: ")
    if ciudad in ciudades:
        indice_ciudad = ciudades.index(ciudad)
        print(f"Los sismos registrados en {ciudad} son: {sismos_por_ciudad[indice_ciudad]}")
    else:
        print("La ciudad no está registrada.")

def informe_de_riesgo(ciudades, sismos_por_ciudad, num_sismos):
    for i in range(len(ciudades)):
        promedio_sismos = sum(sismos_por_ciudad[i]) / num_sismos
        print(f"El promedio de sismos en {ciudades[i]} es: {promedio_sismos}")
        if promedio_sismos < 2.5:
            print("Clasificación: Amarillo (Sin riesgo)")
        elif 2.6 <= promedio_sismos <= 4.5:
            print("Clasificación: Naranja (Riesgo medio)")
        else:
            print("Clasificación: Rojo (Riesgo alto)")
