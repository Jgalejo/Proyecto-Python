#Verificar Numero
num=0
sumPar=0
sumImpar=0
sumPos=0
sumNeg=0
cont=0
#Ingresar datos de Entrada:limite

n=int(input("Ingrese el limite de numero a verificar: "))

#Crear el ciclo para verificar los numeros

while cont<=n:
    num=int(input("Ingrese el numero a verificar: "))

    if num%2==0:                     #Verificar si un numero es par o impar
        sumPar=sumPar+num            #Suma de los numeros Pares
    else:
        sumImpar=sumImpar+num        #Suma de los Impares
    if num>0:                        #Verificar si un numero es Positivo o Negativo
        sumPos=sumPos+num            #Suma de los Positivos
    else:
        sumNeg=sumNeg+num            #Suma de los Negativos

    cont=cont+1

    print(f"La suma de los pares es: {sumPar} ")
    print(f"La suma de los impares es: {sumImpar} ")
    print(f"La suma de los positivos es: {sumPos} ")
    print(f"La suma de los negstivos es: {sumNeg} ")

print(f"Sumas totales\n")
print(f"La suma de los pares es: {sumPar} ")
print(f"La suma de los impares es: {sumImpar} ")
print(f"La suma de los positivos es: {sumPos} ")
print(f"La suma de los negstivos es: {sumNeg} ")


