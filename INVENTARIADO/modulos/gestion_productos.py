import os

def añadir_producto(listaproducto:list):
    
      
         registro_nombre = input('Ingrese el nombre del producto: ')
         registro_codigo = int(input('Ingrese el código del producto: '))
         registro_valor_comp = int(input('Ingrese el valor de compra del producto: '))
         registro_valor_vent = int(input('Ingrese el valor de venta del producto: '))
         registro_stock_min = int(input('Ingrese el stock minimo del producto: '))
         registro_stock_max = int(input('Ingrese el stock maximo del producto: '))
         registro_proveedor = input('Ingrese el nombre del proveedor: ')

         productos = {
         'Nombre': registro_nombre,
         'Codigo': registro_codigo,
         'Valor compra': registro_valor_comp,
         'Valor venta': registro_valor_vent,
         'Stock mínimo': registro_stock_min,
         'Stock máximo': registro_stock_max,
         'Proveedor': registro_proveedor
        }
         
         listaproducto.append(productos)
         print(listaproducto)
         print('Enter para continuar')
         os.system('cls')
         
 
# def buscar_producto(listaproducto:list, nombre:str):

#     codigo=input('Codigo del producto: ').upper()
#     if codigo in listaproducto:
#             input('Producto ya registrado')
#             return
    
#     for producto in listaproducto:
#         if producto['Nombre'] == nombre or producto['Codigo'] == codigo:
#             return producto
#     n_producto = input("Ingrese nombre o codigo del producto: ")
#     listaproducto.index(n_producto)
#     if ValueError:
#           print('El producto no se encuentra')
#           return 



# producto = buscar_producto(lista  producto, n_producto)





    