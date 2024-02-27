from tabulate import tabulate
import modulos.gestion_productos as gest_prod
import modulos.act_stock as stock
import modulos.ganancia_pot as gan_pot

registro_prod = []


def menu_principal():
    titulo = """
+++++++++++++++++++++++++++++++++++
+          INVENTARIADO           +
+++++++++++++++++++++++++++++++++++
    """
    print(titulo)
   
    
    listaproducto = []
    nombre = []

    menu = [["1.","Registre un producto"], ["2.","Buscar productos"], ['3','Actualiza stock'], ['4', 'Informe crítico'], ['5', 'Calculo ganancia potencial'] ]
    print(tabulate(menu,tablefmt="grid"))

    opcion = int(input("Ingrese el número de la opción que desea realizar: "))

    inventariado = {}

    if opcion == 1:
        listaproducto = []
        gest_prod.añadir_producto(listaproducto)
        menu_principal()
    elif opcion == 2:
        stock.tabular(inventariado) 
        input('Presiona enter para continuar...')
    elif opcion == 3:
        stock.administracion_stock(inventariado) 
        menu_principal
        input('Presiona enter para continuar...')
    elif opcion == 4:
        stock.crit(inventariado) 
        menu_principal()
        input('Presiona enter para continuar...')
    elif opcion == 5:
        gan_pot.ganancias(inventariado) 
        gan_pot.ganancias_totales(inventariado) 
        menu_principal()
        input('Presiona enter para continuar...')
    elif opcion == 6:
        return False 

if __name__=='__main__':
      menu_principal()




#     inventariado={}
#     working=True
#     while working:
#         opcion = menu
#         if opcion ==1:
#             is_working=True
#             while is_working:
#                 gest_prod.añadir_producto(listaproducto)
#         if opcion ==2:
#             stock.tabular(inventariado)
#             stock.os.system('pause')
#         if opcion ==3:
#             isstock=True
#             while isstock:
#                 stock.administracion_stock(inventariado)
#                 isstock=bool(input('Para ingresar: S, para eliminar producto: enter'))
#             stock.os.system('pause')
#         if opcion ==4:
#             stock.crit(inventariado)
#             stock.os.system('pause')
#         if opcion ==5:
#             gan_pot.ganancias(inventariado)
#             gan_pot.ganancias_totales(inventariado)
#             gan_pot.os.system('pause')
#         if opcion ==6:
#             working=False     

# if __name__=='__main__':
#     menu_principal()

   