print("Programa que permita el calculo de un poligono compuesto\n")


#Lectura de Datos

lc=float(input("Ingrese el lado del cuadrado:"))
at=float(input("Ingrese la altura del triangulo:"))
ar=float(input("Ingrese la altura del rectangulo:"))

#Proceso

A=lc**2
B=(lc-at)/7
ats=B*3
D=lc*ar
area= A+ats+D

#Salida de Datos
print(f"El area del poligono compuesto es: {area} compuesto por un cuadrado de lado\n{lc}"
      f" y un rectangulo de altura {ar} y una altura de triangulo {at} ")
