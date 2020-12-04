#Conversion temperatura
print("Programa que permita convertir de grados centigrados a grados farenheit"
      "y a grados Kelvin\n")
#Entrada de Datos
gC=int(input("Ingrese los grados centigrados: "))

#Condicion para convertir de grados a temperatura
#Proceso
if gC>0:
   gF=(gC*9/5)+32
   gK=(gC+273.15)
#Salida
   print(f"La equivalencia en grados F es: {gF}")
   print(f"La equivalencia en grados K es: {gK}")

