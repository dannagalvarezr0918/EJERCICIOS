import os
import tabulate

def titulo():
    titulo = """
    ++++++++++++++++++++++++++
    +     CALCULA TU IMC     +
    ++++++++++++++++++++++++++
"""
    os.system
    print(titulo)


def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def categorias_imc(imc, categorias):
    if 18.5 <= imc <= 24.9:
        category = 'Normal'
        categorias[0]+=1
    elif 25 <= imc <= 29.9:
        category = 'Sobrepeso'
        categorias[1]+=1
    elif 30 <= imc <= 34.9:
        category = 'Obesidad 1'
        categorias[2]+=1
    elif 35 <= imc <= 39.9:
        category = 'Obesidad 2'
        categorias[3]+=1
    elif imc >= 40:
        category = 'Obesidad 3'
        categorias[4]+=1
    else:
        category = 'No califica'
        categorias[5]+=1
    return category, categorias
        

def main():
    categorias = [0,0,0,0,0,0]
    titulo()
    estudiantes = []
    for i in range(2):
        estudiante = []
    
        nombre = input('Ingrese el nombre del estudiante : ')
        edad = int(input('Ingrese la edad del estudiante : '))
        peso = float(input('Ingrese el peso del estudiante : '))
        altura = float(input('Ingrese la altura del estudiante : '))
        imc = calcular_imc(peso, altura)
        category = categorias_imc(imc, categorias)
        estudiante.append([nombre, edad, imc, category])
        print(tabulate.tabulate(estudiante, headers=["Nombre", "Edad", "IMC", "Categoría"], tablefmt='grid'))
        estudiantes.append(estudiante)

        print(f'Estudiantes con peso NORMAL: {categorias[0]}')
        print(f'Estudiantes con SOBREPESO: {categorias[1]}')
        print(f'Estudiantes con OBESIDAD I: {categorias[2]}')
        print(f'Estudiantes con OBESIDAD II: {categorias[3]}')
        print(f'Estudiantes con OBESIDAD III: {categorias[4]}')
        print(f'Estudiantes sin calificación: {categorias[5]}')

if __name__ == "__main__":
    main()
     


