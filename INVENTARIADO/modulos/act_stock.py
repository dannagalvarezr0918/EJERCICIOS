from tabulate import tabulate
import os
def menu_stock ():
    opciones=[1,2]
    listopciones=['1. Añade productos', '2. Elimina productos']
    for item in listopciones:
        print(item)
    try:
        op=int(input('->'))
        if op not in opciones:
            print('Opcion inexistente')
    except ValueError:
        print('Error')
    else:
        return op

def administracion_stock(inventariado:dict):
    print(f' Codigos ingresados: {inventariado.keys()}')
    codigo=input('Ingrese el codigo del producto: ').upper()
    for item,value in inventariado.items():
            if item==codigo:
                ops=int(menu_stock())
                if ops==1:
                            try:
                                añadir=int(input(f'Cantidad de productos a añadir a {inventariado[codigo]["nombre"]} : '))
                                if inventariado[codigo]["cantidad"]+añadir>inventariado[codigo]['stock_max']:
                                    print(f'no se puede ingresar esa cantidad de productos, debido a que la cantidad maxima que estan permitidas recibir en este momento es: {(inventariado[codigo]["stock_max"])-(inventariado[codigo]["cantidad"])}')
                                else:
                                    inventariado[codigo]['cantidad']+=añadir
                                    return
                            except ValueError:
                                print('Solo puedes ingresar números')
                                return
                if ops ==2:
                    try:
                        añadir=int(input(f'Cantidad de productos que desea eliminar a  {inventariado[codigo]["nombre"]} : '))
                        if inventariado[codigo]['cantidad']-añadir<0:
                            print(f'No se pueden retirar esa cantidad de productos, debido a que solo se cuenta con: {(inventariado[codigo]["cantidad"])} {inventariado[codigo]["nombre"]}s')
                        else:
                            inventariado[codigo]['cantidad']+=(-añadir)
                            if inventariado[codigo]["cantidad"]-añadir<inventariado[codigo]['stock_min']:
                                print(f'Tienes una cantidad {inventariado[codigo]["nombre"]} que es menor que el stock minimo permitido')
                            return
                    except ValueError:
                        print('Solo puedes ingresar números')
                        return       
    else:
        print('Producto no registrado')

def crit(inventariado:dict):
    for key,values in inventariado.items():
        if values['stock_min']>=values['cantidad']:
            print(f'{key}. {values["nombre"]}')

def tabular(inventariado):
    datos=[]
    for key,value in inventariado.items():
        datos.append(value)
    print(tabulate(datos,headers='keys',tablefmt='grid'))