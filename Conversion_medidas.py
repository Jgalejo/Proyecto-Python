print("Programa que permita la conversion de metros a centimetros,kilometros,pies y pulgadas ")

#Lectura de datos
m=float(input("Ingrese la cantidad en metros: "))

#Proceso

cm = m*100/1
km = m*1/1000
ps = m*3.280/1
pg = m*39.37/1

#Salida de datos
print(f"El resultado en centimetros es: {cm}")
print(f"El resultado en kilometros es: {km}")
print(f"El resultado en pies es: {ps}")
print(f"El resultado en pulgadas es: {pg}")

