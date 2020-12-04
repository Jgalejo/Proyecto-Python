#Calculadora
#Ya que el switch no existe en  en python se realizara de otra manera
print("Calculadora de operaciones basica\n")

num1=float(input("Ingrese el valor del numero 1: "))
num2=float(input("Ingrese el valor del numero 2: "))
#Menu de opciones
opc=int(input("Escoja una de las siguientes opciones"
              "\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Divison\n"))

if opc==1:
    suma=num1+num2
    print(f"\nLa suma es: {suma}")
elif opc==2:
    resta=num1-num2
    print(f"\nLa resta es: {resta}")
elif opc==3:
    multiplicacion=num1*num2
    print(f"\nLa multiplicacion es: {multiplicacion}")
elif opc==4:
    division=num1/num2
    print(f"\nLa division es: {division}")
else:
    print("\nOpcion invalida")

