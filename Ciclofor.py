#Cilo For
i=0
n=0
primero=0
segundo=1
fibo=0
suma=0
suma1=0
n=int(input("Ingrese el limite de la serie Fibonacci:  "))
print("\n")


for i in range(i,n):
    if i<2:
        print(f"{i}+{primero}")
        print(f"{i+1}+{segundo}")
        suma=primero+segundo
        i+=1
    else:
        fibo=primero+segundo
        suma=suma+fibo
        primero=segundo
        segundo=fibo
        print(f"{i}+{fibo}")


print(f"\nPRIMERA SUMA: {suma}")
print(f"\nSEGUNDA SOLUCION")

primero=0
segundo=1
fibo=0

for i in range(i,n):
    print(f"{i}+{primero}")

    suma1=suma1+primero
    fibo=primero+segundo
    primero=segundo
    segundo=fibo

print(f"\nSEGUNDA SUMA {suma1}")









