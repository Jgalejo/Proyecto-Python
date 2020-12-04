#Programa que permita ir introduciendo una serie indeterminada de numeros mientras su suma no supere el valor de
#100000.Cuando esto ultimo ocurra, se debe mostrar el total acumulado, el contador de numeros introducido y la media
num=0
suma=0
media=0
Nvalores=0
j=0

while suma<100000:
    j = int(input("Ingresa distintos valores:\n"))
    if j==0:
        print("Ingresa un valor mayor a 0")
    elif j>100000:
        print("Ingresa un valor menor a 100000")
    suma=j+suma
    Nvalores +=1

media=suma/Nvalores
print(f"Ingresaste  {Nvalores}  numeros")
print(f"La media es: {media} ")
print(f"La suma de valores ingresados es: {suma} ")


