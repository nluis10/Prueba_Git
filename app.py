#print("aaaaaa")

numero = int(input("Ingrese el numero: "))

#print("El numero es numero:", numero)

cont = 0
for i in range(1, numero+1):
    if numero % i == 0:
        cont += 1

print(cont)
