#Factura
limite1=200
limite2=500
subtotal=0
descuento=0
print("Programa para calcular el valor total de una factura con descuentos")

#Datos de entrada
subtotal=float(input("Ingrese el subtotal de la compra: "))

#Proceso para determinar el descuento en base al subtotal de  compra
if subtotal>=limite1 and subtotal<limite2:
    descuento=0.10
else:
    if subtotal>=limite2:
       descuento=0.15
if subtotal<limite1:
    print("No hay descuento por su compra por ser menor a 200 dolares")
total=subtotal-(subtotal*descuento)

#Presenta la salida de resultados
print(f"El total de la factura es {total} con un descuento de {descuento}  ")