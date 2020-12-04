#Determinar edad de una persona

#Lectura de datos

an=int(input("Ingrese su año de nacimiento: "))
aa=int(input("Ingrese el año actual: "))
mn=int(input("Ingrese su mes de nacimiento: "))
ma=int(input("Ingrese el mes actual: "))
dn=int(input("Ingrese su dia de nacimiento: "))
da=int(input("Ingrese el dia actual: "))

#Proceso
if aa>an:
    aa=aa-an
if ma>mn:
    ma=ma-mn
if da>dn:
    da=da-dn
print(f"Su edad es {aa} años con {ma} meses y {da} dias")