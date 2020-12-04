#Calcular el mayor de 3 numeros mediante los 3 tipos de estructuras condicionales
#Condicional Simple
n1cs=0
n2cs=0
n3cs=0
nmcs=0
#Condicional Compuesta
n1cc=0
n2cc=0
n3cc=0
#Condicional Anidada
n1ca=0
n2ca=0
n3ca=0
#Lectura de datos
n1cs=input("Ingrese un nuemero (simple):")
n1cc=input("Ingrese un numero  (compuesta): ")
n1ca=input("Ingrese un numero  (anidada): ")

n2cs=input("Ingrese otro numero (simple): ")
n2cc=input("Ingrese otro numero (compuesta): ")
n2ca=input("Ingrese otro numero (anidada: ")

n3cs=input("Ingrese el ultimo numero (simple): ")
n3cc=input("Ingrese el ultimo numero (compuesta): ")
n3ca=input("Ingrese el ultimo numero (anidada) ")

#Proceso
#Condicional (Simple)

nmcs=n1cs
if n1cs<=n2cs:
    nmcs=n2cs
if  n2cs<=n3cs:
    nmcs=n3cs

#Condicional (Compuesta)
    if n1cc >= n2cc and n1cc >= n3cc:
        print(f"El numero mayor es {n1cc}")
    else:
        if n2cc >= n1cc and n2cc > n3cc:
            print(f"El numero mayor es: {n2cc}")
        else:
            print(f"El numero mayor es: {n3cc}")



#Condicional anidada

if n1ca>n2ca:
    if n1ca>n3ca:
        print(f"El numero mayor es: {n1ca}")
    else:
        print(f"El numero mayor es: {n3ca}")
else:
    if n2ca>n3ca:
        print(f"El numero mayor es: {n2ca}")
    else:
        print(f"El numero mayor es: {n3ca}")


print(f"El numero mayor es: {nmcs}")