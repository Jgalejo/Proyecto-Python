#Verificar Primo
cont=1
cont1=1
num=0
divisor=0
n=int(input("Ingrese el limite de numeros  a verificar si es primo: "))
while cont<=n:
    num=int(input("Ingrese el numero a verificar:  "))
    while cont1<=num:
        if num%cont1==0:
            divisor=divisor+1

        cont1=cont1+1

    if divisor==2:
        print(f"{num} es primo")
        print(f"-------------------")
    else:
        print(f"{num} no es primo")
        print(f"-------------------")

    #Termina de verificar los numeros y tenicio de los contadores
    cont1=1
    divisor=0
    cont=cont+1







