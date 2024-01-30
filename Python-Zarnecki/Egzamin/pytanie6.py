liczba = int(input("Prosze wpisac liczbe: "))
lista_dzielnikow = []
for i in range(1,liczba+1):
    if liczba%i==0:
        lista_dzielnikow.append(i)
print(lista_dzielnikow)
if len(lista_dzielnikow)==2:
    print("Wpisana liczba jest liczbą pierwszą")
else:
    print("Wpisana liczba to NIE jest liczba pierwsza")