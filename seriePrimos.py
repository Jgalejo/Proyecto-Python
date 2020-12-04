#Serie Primos
num=0
den=0
suma=0
n=0
primo=2
divisor=0
i=1
j=1
bandera=False
print("PROGRAMA PARA GENERAR LA SERIE"
      "1/2 - 2/3 + 3/5 - 4/7 + 5/11 - 6/13 +.... +n\n")

n=int(input("Ingrese el limite de la serie: "))

for i in range(i,n):
    num=num+1


    while bandera==False:
        for j in range(j,primo):
            if primo % j==0:
                divisor=divisor+1

        if divisor==2:
            bandera=True
            den=primo
            primo=primo+1
        else:
            primo=primo+1

        divisor=0

    if i % 2==0:
        print(f"{i}-{num} / {den}")
        suma=suma-float(num/den)
    else:
        print(f"{i}+{num} / {den} ")
        suma = suma +float(num / den)

print("")
print(f"La suma de la serie es: {suma} \n ")


