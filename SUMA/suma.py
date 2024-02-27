import os

def titulo(): """
      +++++++++++++++++++
      +    SUMA DE 3    +       
      +++++++++++++++++++
"""
os.system('cls')
print (titulo)

primer_num = int(input("Ingrese el primer número: "))
if primer_num <= 0:
    print ("No puedes ingresar un numero menor o igual a cero")
    
segundo_num = int(input("Ingrese el segundo numero: "))
if primer_num <= 0:
    print ("No puedes ingresar un numero menor o igual a cero")
    
tercer_num = int(input("Ingrese el tercer numero: "))
if primer_num <= 0:
    print ("No puedes ingresar un numero menor o igual a cero")
   

suma = primer_num + segundo_num + tercer_num
print(suma)

if __name__ == "__main__":  
    titulo()
        

