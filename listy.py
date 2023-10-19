lista = []

lista.extend([10 , 3, 5, 6, 7])

print(lista[0])

print(lista[-1])

lista.append(12)
print(lista[-1])

lista.pop(1)
print(lista)

print(len(lista))

sprawdz = int(input("Wybierz liczbę do sprawdzenia: "))
print(sprawdz in lista)

odwroc = []
for i in range(len(lista)-1,-1,-1):
    odwroc.append(lista[i])
lista=odwroc
print(lista)

kopia=lista
print(kopia)

lista.sort()
print(lista)

for i in range(-1,len(lista),3):
    print(lista[i])