print("Programa que permita el calculo de un poligono compuesto\n")

#Lectura de datos
b=float(input("Ingrese la base:"))
a=float(input("Ingrese la altura:"))
A=float(input("Ingrese el area del triangulo:"))
B=float(input("Ingrese el area del rectangulo "))

#Proceso
A = b * a / 2
B = b * a
P = A + B

#Salida de datos
print(f"El area total es: {P}")
