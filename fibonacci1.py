#Fibonacci1
n=0
primero=0
segundo=1
fibo=0
i=1

n=int(input("Ingrese el limite de la serie fibonacci 2: "))
print("\n")

for i in range(i,int(n/2+1)):
    print(f"{i},{primero}")
    print(f"{i},{segundo}")
    primero=primero+segundo
    segundo=primero+segundo

