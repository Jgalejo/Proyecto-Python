#Numero positivo o negativo

print("Programa que permita verificar si un numero es positivo o negativo")

n=float(input("Ingrese el numero: "))

#Proceso
if n>0:
    print("El numero es positivo")
elif n==0:
    print("El numero es neutro")
else:
    print("El numero es negativo")