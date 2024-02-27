import os
def ganancias(inventariado:dict):
    for key,value in inventariado.items():
        unidad_ganancia=value['valor_venta']-value['valor_compra']
        gananciaTotal=unidad_ganancia*value['cantidad']
        print(f'{key}. {value["nombre"]}, obtendra una ganancia de: {gananciaTotal}')
    
def ganancias_totales(inventariado:dict):
    total=0
    for key,value in inventariado.items():
        ganancia_item=value['valor_venta']-value['valor_compra']
        total+=ganancia_item*value['cantidad']
    print(f'GANANCIAS TOTALES = {total}')


