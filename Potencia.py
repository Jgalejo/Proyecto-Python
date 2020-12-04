#Potencia

print("Programa que permite obtener la potencia de un numero")
#Declarar e inicializar variables

base=0
pot=0
cont=1
resul=1

#Ingresar los datos
base=int(input("Ingresar la base de la potencia:  "))

pot=int(input("Ingresar la potencia: "))

#Ciclo repetitivo que obtiene la potencia de un numero
while cont<=pot:
    resul=resul*base
    cont=cont+1

#Presentar el resultado
print(f"La potencia de: {base} elevado a {pot} es: {resul} ")

